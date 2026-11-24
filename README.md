# Diego Perez Ruiz — personal website

A [Quarto](https://quarto.org) website: deep-pine palette, density-curve motif,
Spectral / Public Sans / IBM Plex Mono, with a light/dark toggle.

## Branches

| Branch          | What it holds                                                    |
|-----------------|------------------------------------------------------------------|
| `source`        | **Edit here.** The Quarto files below.                           |
| `master`        | The built website. Written automatically — don't edit by hand.   |
| `old-hugo-site` | Backup of the previous Hugo Academic site.                       |

Every push to `source` runs `.github/workflows/publish.yml`, which renders the site
and publishes it to `master`. GitHub Pages serves `master`, so the site updates
a minute or two after each push.

## Structure

```
_quarto.yml            Site config: navbar, light/dark themes, footer
index.qmd              Home — hero with the density-curve graphic
about.qmd              About — profile card (photo) + bio, education, experience
projects/              Listing + one page per project
software.qmd           Software — R, Julia, and Apps subsections (repo cards)
teaching.qmd           Teaching (courses, workshops, materials)
podcast/               AI Podcast — listing + episodes/
publications/          Latest Publications (+ references.bib)
blog/                  Blog listing + posts/
contact.qmd            Contact links (+ optional Formspree form)
theme.scss             Light theme
theme-dark.scss        Dark theme (used by the navbar toggle)
styles.css             Custom components + dark-mode variables
assets/                Logo, profile photo, cv.pdf
```

## Still to fill in

1. Your real email in `contact.qmd` (replace `your.email@example.com`).
2. Publications in `publications/index.qmd`.
3. Teaching entries in `teaching.qmd`, repos in `software.qmd`, podcast episodes in `podcast/episodes/`.
4. Optionally a newer photo (`assets/profile.jpg`) and CV (`assets/cv.pdf`).

## Run it locally

```bash
quarto preview     # live preview at http://localhost:4200
```
