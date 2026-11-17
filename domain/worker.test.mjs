import test from "node:test";
import assert from "node:assert/strict";
import { serve } from "./worker.mjs";

test("serves static content without forwarding credentials or query strings", async () => {
  const response = await serve(new Request("https://atlas.bonjour.dev/zh-Hans/?token=private", {
    headers: { Authorization: "Bearer private", Cookie: "session=private" },
  }), async (url, options) => {
    assert.equal(url, "https://bonjour-studio.github.io/atlas-feedback/zh-Hans/");
    assert.deepEqual(options.headers, { Accept: "*/*" });
    assert.equal(options.redirect, "manual");
    return new Response("Public content", { headers: { "content-type": "text/html", "set-cookie": "ignored=1" } });
  });
  assert.equal(response.status, 200);
  assert.equal(await response.text(), "Public content");
  assert.equal(response.headers.get("set-cookie"), null);
  assert.match(response.headers.get("content-security-policy"), /script-src 'none'/);
});

test("does not accept other hosts or write methods", async () => {
  const neverFetch = () => { throw new Error("Must not contact upstream"); };
  assert.equal((await serve(new Request("https://other.bonjour.dev/"), neverFetch)).status, 404);
  const response = await serve(new Request("https://atlas.bonjour.dev/", { method: "POST", body: "private" }), neverFetch);
  assert.equal(response.status, 405);
  assert.equal(response.headers.get("allow"), "GET, HEAD");
});

test("rewrites only redirects inside this site's upstream path", async () => {
  const response = await serve(new Request("https://atlas.bonjour.dev/feedback"), async () =>
    new Response(null, { status: 301, headers: { location: "https://bonjour-studio.github.io/atlas-feedback/feedback/" } }));
  assert.equal(response.headers.get("location"), "https://atlas.bonjour.dev/feedback/");
  for (const location of ["https://example.com/", "https://bonjour-studio.github.io/expose-feedback/"]) {
    const rejected = await serve(new Request("https://atlas.bonjour.dev/"), async () =>
      new Response(null, { status: 302, headers: { location } }));
    assert.equal(rejected.status, 502);
  }
});

test("preserves missing-page status and honors HEAD", async () => {
  assert.equal((await serve(new Request("https://atlas.bonjour.dev/missing"), async () =>
    new Response("Not found", { status: 404 }))).status, 404);
  const head = await serve(new Request("https://atlas.bonjour.dev/", { method: "HEAD" }), async (_, options) => {
    assert.equal(options.method, "HEAD");
    return new Response(null, { headers: { "content-type": "text/html" } });
  });
  assert.equal(head.status, 200);
  assert.equal(await head.text(), "");
});

test("upstream failure returns a bounded retry response without exception details", async () => {
  const messages = [];
  const previous = console.error;
  console.error = (message) => messages.push(message);
  try {
    const response = await serve(new Request("https://atlas.bonjour.dev/"), async () => { throw new Error("private exception"); });
    assert.equal(response.status, 503);
    assert.equal(response.headers.get("retry-after"), "60");
    assert.doesNotMatch(await response.text(), /private exception/);
    assert.deepEqual(messages, ['{"event":"atlas_public_site_unavailable"}']);
  } finally { console.error = previous; }
});
