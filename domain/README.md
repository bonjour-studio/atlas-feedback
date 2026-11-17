# Custom-domain adapter

`worker.mjs` can serve this repository’s public GitHub Pages site at `atlas.bonjour.dev` without changing its existing proxied placeholder DNS record. The intended Worker route is **`atlas.bonjour.dev/*`**, with script name **`atlas-public-site`**. It does not match other Bonjour domains.

The owner authorized deployment on November 17, 2026. The Worker and route are active. Existing legal redirects run before the Worker on some legacy paths; the website uses `/legal/privacy/` and `/legal/terms/` to serve the published policies directly.

The adapter only accepts GET and HEAD, fixes the upstream to this public website, strips incoming headers/query strings, streams responses and rewrites only redirects within the website’s own upstream path. It does not handle app API calls or accept feedback submissions; those are linked to GitHub and private email support.

Run the focused request-handling checks with:

```sh
node --test domain/worker.test.mjs
```

Deployment uses compatibility date `2026-11-17`, enables Workers logs (10%) and traces (1%), disables invocation logs and redacts query strings. Keep API credentials out of this repository. The error log intentionally contains no incoming request URL, headers or exception details. Test the deployed Worker separately; the local checks cover portable Fetch behavior, not Cloudflare’s routing or runtime.

`SITE` in `tools/build_site.py` is `https://atlas.bonjour.dev`. The static site is published automatically by GitHub Pages from `main:/docs`; the Worker serves that fixed upstream without forwarding incoming credentials, cookies or query strings. Successful responses include `no-transform` to preserve email links without injected JavaScript.
