# ABS Consult

Static recreation of [absconsult.co.zw](https://absconsult.co.zw) for GitHub and Cloudflare Pages.

The site is plain HTML, CSS, and JavaScript. There is no build step required to deploy.

## Preview locally

From this folder:

```bash
python3 -m http.server 4173
```

Open [http://127.0.0.1:4173](http://127.0.0.1:4173).

`scripts/build_site.py` regenerates the HTML pages from the shared header, footer, and page copy. Run it after editing that script:

```bash
python3 scripts/build_site.py
```

## Deploy on Cloudflare Pages

1. Push this folder to a GitHub repository.
2. In Cloudflare, go to **Workers & Pages → Create → Pages → Connect to Git**.
3. Select the repository.
4. Use these build settings:
   - **Framework preset:** None
   - **Build command:** leave empty
   - **Build output directory:** `/`
5. Deploy.

The contact form opens the visitor’s email app addressed to `tax@absconsult.co.zw`. WhatsApp uses `+263 77 375 1230`.

`_redirects` maps the old WordPress paths (`/tax-consulting/`, `/about-us/`, `/contact-us/`, and the original article URLs) onto the new pages.

Optional CLI deploy, after [Wrangler](https://developers.cloudflare.com/workers/wrangler/) is logged in:

```bash
npx wrangler pages deploy . --project-name abs-consult
```
