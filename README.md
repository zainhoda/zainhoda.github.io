# Zain Hoda

Personal website for **zain-hoda.com**, hosted from this repository with GitHub Pages.

A custom, responsive Jekyll site with no client-side JavaScript, tracking scripts, external fonts, or theme dependency. The homepage introduces Zain's enterprise AI work and links to The AI Adoption Gap on Substack. Published technical posts retain their existing URLs and are linked from `/writing/`.

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

The newsletter button links to `https://zainhoda.substack.com/subscribe`. Set `booking_url` in `_config.yaml` to enable direct scheduling. Until then, the call buttons open an email requesting a 30-minute conversation at `zain@vanna.ai`.

## GitHub Pages and the domain

This site uses GitHub Pages' native Jekyll build. In the repository's **Settings → Pages**, select the intended publishing branch and its root directory. No separate Node build or workflow is needed.

`CNAME` and the canonical URL are set to `zain-hoda.com`. Publishing the repository alone does not configure the domain's DNS: point the domain at GitHub Pages, add it in the Pages settings, and enable HTTPS after GitHub provisions the certificate. Verify that `zain@vanna.ai` receives email before launch.
