# Zain Hoda

Personal website for **zain-hoda.com**, hosted from this repository with GitHub Pages.

A custom, responsive Jekyll site with a small script for interactive company cards and no tracking scripts, external fonts, or theme dependency. The homepage introduces Zain's enterprise AI work and links to The AI Adoption Gap on Substack. Published technical posts retain their existing URLs and are linked from `/writing/`.

## Local development

Requires Ruby 3.1 or newer and Bundler.

```sh
bundle install
bundle exec jekyll serve
```

Open the local URL printed by Jekyll. The preview rebuilds when content or styles change; restart it after changing `_config.yaml`.

```sh
JEKYLL_ENV=production bundle exec jekyll build
```

The generated site is in `_site/`, which is excluded from Git.

## Content and links

- `index.html`: homepage copy and sections.
- `assets/css/site.css`: colors, typography, layouts, and responsive styles.
- `_config.yaml`: canonical domain, email address, booking link, and newsletter link.
- `_layouts/`: shared page shell and article layout.
- `_posts/`: the three original articles, with their existing URLs. Add YAML front matter with a title when creating a new post.

The newsletter button links to `https://zainhoda.substack.com/subscribe`. The “Let’s talk” buttons use `booking_url` in `_config.yaml` to open `https://cal.com/zainhoda/30min`. Direct email contact remains `zain@vanna.ai`.

## GitHub Pages and the domain

This site uses GitHub Pages' native Jekyll build from the `main` branch and root directory. No separate Node build or workflow is needed. Pushes to `main` publish automatically.

`CNAME`, the canonical URL, and the GitHub Pages custom domain are set to `zain-hoda.com`.

Cloudflare DNS is managed under **Zain Hoda Personal**, using `aisha.ns.cloudflare.com` and `sage.ns.cloudflare.com`:

| Type | Name | Target | Proxy status |
| --- | --- | --- | --- |
| CNAME | `@` | `zainhoda.github.io` | DNS only |
| CNAME | `www` | `zainhoda.github.io` | DNS only |

Cloudflare flattens the apex CNAME into GitHub Pages IP addresses. GitHub Pages handles the `www` redirect and TLS certificate. **Enforce HTTPS** is enabled in Pages settings; both HTTP and `www` requests redirect to `https://zain-hoda.com/`. The existing mail-related TXT records are preserved; the site's contact address is `zain@vanna.ai`.
