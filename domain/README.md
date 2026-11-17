# Optional custom-domain adapter

`worker.mjs` can serve this repository’s public GitHub Pages site at `atlas.bonjour.dev` without changing its existing proxied placeholder DNS record. The intended Worker route is **`atlas.bonjour.dev/*`**, with script name **`atlas-public-site`**. It does not match other Bonjour domains.

This adapter is prepared for review. Its presence in this repository does not mean it has been deployed or the route has been created. Cloudflare writes require the owner’s authorization; existing legal redirects must be checked after connecting the route because rules may run before the Worker.

The adapter only accepts GET and HEAD, fixes the upstream to this public website, strips incoming headers/query strings, streams responses and rewrites only redirects within the website’s own upstream path. It does not handle app API calls or accept feedback submissions; those are linked to GitHub and private email support.

Run the focused request-handling checks with:

```sh
node --test domain/worker.test.mjs
```

Deployment should use compatibility date `2026-11-17`, enable Workers logs and traces with sampling, and keep API credentials out of this repository. The error log intentionally contains no incoming request URL, headers or exception details. Test the deployed Worker separately; the local checks cover portable Fetch behavior, not Cloudflare’s routing or runtime.

Once the custom domain is verified, set `SITE` in `tools/build_site.py` to `https://atlas.bonjour.dev`, regenerate the pages and update the repository’s homepage URL. The static site is published automatically by GitHub Pages from `main:/docs`.
