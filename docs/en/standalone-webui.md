# Deploying the WebUI Separately

[中文](../zh/standalone-webui.md) | English

By default, the DiceFrame backend also serves its WebUI. Desktop builds, packaged Windows clients, and Docker deployments can keep using this same-origin mode. A standalone WebUI is only needed when the browser application should live on a static host such as Cloudflare Pages while the DiceFrame backend continues to run on a NAS, home computer, or server.

The standalone WebUI contains only frontend assets. It does not contain the DiceFrame backend, saves, or API keys. The browser still connects directly to the configured backend:

```text
Browser → HTTPS static WebUI → HTTPS DiceFrame backend → data/ and model services
```

## Prerequisites

- Use a DiceFrame version or source checkout that provides `npm run build:standalone`.
- Have Node.js and npm available, unless the static host performs the build.
- Give the DiceFrame backend a browser-reachable HTTPS address through a reverse proxy, Cloudflare Tunnel, or an equivalent service.
- Know the complete origin of the static WebUI, such as `https://diceframe.pages.dev`.

When the static WebUI uses HTTPS, browsers block requests to a plain HTTP backend. Enabling HTTPS only for the static site is not sufficient; the backend must also use HTTPS.

## Option 1: Cloudflare Pages

Connect the DiceFrame GitHub repository and use these build settings:

| Setting | Value |
| --- | --- |
| Root directory | `frontend-v2` |
| Build command | `npm run build:standalone` |
| Build output directory | `dist` |

The build does not need an API key. Never put the backend password, model credentials, or other secrets in Pages environment variables. After deployment, note the Pages domain. If a custom domain is enabled, use the domain that people actually open as the origin below.

## Option 2: Build for another static host

Run the following commands in a DiceFrame source checkout:

```bash
cd frontend-v2
npm ci
npm run build:standalone
```

Deploy the complete generated `frontend-v2/dist/` directory to an HTTPS-capable static host. Do not use the regular `npm run build`; that command produces the same-origin frontend served by the DiceFrame backend.

## Allow the frontend on the backend

The backend must explicitly allow the standalone WebUI origin. An origin contains only the scheme, host, and optional port, with no path.

The recommended interactive setup is to open the backend's built-in WebUI and enter the following under **Settings → Sharing address → Standalone Frontend CORS Allowlist**:

```text
https://diceframe.pages.dev
```

Separate multiple origins with commas or semicolons. Saving updates the backend's `data/config.json` and takes effect immediately.

Automated deployments can use an environment variable instead:

```env
TRPG_WEB_CORS_ORIGINS=https://diceframe.pages.dev,https://play.example.com
```

The environment variable takes precedence over the WebUI setting. Restart DiceFrame after changing it; the allowlist appears read-only in Settings while the variable is active. Enter the real frontend origins, not the backend address. Do not add paths or use `*`.

## First connection

1. Open the deployed standalone WebUI.
2. Enter the DiceFrame backend HTTPS address on the login page, for example `https://api.example.com`.
3. If the backend is behind a reverse-proxy subpath, include the complete path, for example `https://example.com/diceframe`.
4. Connect, then enter the DiceFrame access password.

The browser remembers the most recently used backend locally. Share links created from the standalone WebUI also carry the backend address, but never the access password or model API key.

## Upgrades and compatibility

- Packaged Windows builds, Docker, and `python web_server.py` keep their existing startup behavior. CORS configuration is not needed when the standalone WebUI is not used.
- Keep the standalone WebUI and backend on the same DiceFrame version when possible. Rebuild and redeploy the static assets when upgrading the backend to avoid frontend/backend API mismatches.
- Saves, settings, and plugin data remain in the backend's `data/` directory. Redeploying the static site does not migrate or erase them.

## Security guidance

- Allow only frontend origins you control. Never use the `*` wildcard.
- Protect an internet-facing backend with a DiceFrame access password and expose it through a trusted HTTPS reverse proxy or tunnel.
- Never bundle model API keys, the DiceFrame access password, or `.env` into `dist/`. Visitors can inspect every file on a static site.
- For local or LAN-only use, the WebUI served by the backend is usually simpler.

## Troubleshooting

### The page opens, but the server connection fails

Confirm that the backend address is reachable from the current browser, uses HTTPS, and includes any required reverse-proxy path. Opening `BACKEND_URL/api/config` directly should return a DiceFrame response rather than a proxy server's 404 page.

### The browser reports a CORS error

The allowlist must contain the static WebUI origin, such as `https://play.example.com`, not the backend address. Scheme, hostname, and port must match exactly, and the configured origin must not contain a path.

### The browser reports Mixed Content

The static WebUI uses HTTPS while the backend still uses HTTP. Add HTTPS to the backend first; relaxing CORS cannot fix mixed content.

### The page or a feature breaks after an upgrade

Rebuild and redeploy `dist/`, purge the static host cache, and verify that the frontend and backend use the same version. If the issue remains, open the backend's built-in WebUI to distinguish a static-deployment problem from a backend problem.
