// Optional custom-domain adapter for the public GitHub Pages website.
// No app traffic, credentials or account data belong on this endpoint.
const HOST = "atlas.bonjour.dev";
const UPSTREAM = "https://bonjour-studio.github.io";
const PREFIX = "/atlas-feedback";

export async function serve(request, fetchPublicSite = fetch) {
  const url = new URL(request.url);
  if (url.hostname !== HOST) return new Response("Not found", { status: 404 });
  if (!["GET", "HEAD"].includes(request.method)) {
    return new Response("Method not allowed", {
      status: 405, headers: { Allow: "GET, HEAD" },
    });
  }
  // The website is static. Drop query strings and all incoming headers,
  // including cookies and authorization, before contacting GitHub Pages.
  const target = new URL(PREFIX + url.pathname, UPSTREAM);
  try {
    const upstream = await fetchPublicSite(target.href, {
      method: request.method,
      headers: { Accept: "*/*" },
      redirect: "manual",
    });
    const headers = new Headers(upstream.headers);
    headers.delete("set-cookie");
    const location = headers.get("location");
    if (location) {
      const next = new URL(location, target);
      if (next.origin !== UPSTREAM ||
          !(next.pathname === PREFIX || next.pathname.startsWith(PREFIX + "/"))) {
        return new Response("Unexpected website redirect", { status: 502 });
      }
      const publicURL = new URL(next.pathname.slice(PREFIX.length) || "/", url.origin);
      headers.set("location", publicURL.href);
    }
    headers.set("x-content-type-options", "nosniff");
    headers.set("referrer-policy", "strict-origin-when-cross-origin");
    headers.set("content-security-policy", "default-src 'self'; script-src 'none'; style-src 'self' 'unsafe-inline'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'");
    // Preserve static email links instead of injecting a JavaScript decoder.
    if (upstream.ok) headers.set("cache-control", "public, max-age=300, no-transform");
    return new Response(request.method === "HEAD" ? null : upstream.body, {
      status: upstream.status,
      statusText: upstream.statusText,
      headers,
    });
  } catch {
    // Keep URLs, request headers and upstream exception details out of logs.
    console.error(JSON.stringify({ event: "atlas_public_site_unavailable" }));
    return new Response("Atlas website is temporarily unavailable. Please try again shortly.", {
      status: 503,
      headers: { "retry-after": "60", "content-type": "text/plain; charset=utf-8" },
    });
  }
}

export default {
  fetch(request) { return serve(request); },
};
