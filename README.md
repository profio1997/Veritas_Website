# Veritas: pre-release site

Static landing page for **Veritas**, "Master what you read." Launching December 2026.

- `index.html` + `assets/`: the built site. Host it anywhere that serves static files (GitHub Pages, Netlify, Cloudflare Pages).
- `src/page.html`: the single source of the page. `src/build_site.py` wraps it into `index.html` and copies `assets/`.

## Rebuild
Edit `src/page.html`, then run `python3 src/build_site.py` (see the script header for paths and the optional base URL).

## Waitlist
Sign-ups post to a Formspree form (`WAITLIST_ENDPOINT` near the top of the script in `src/page.html`). Submissions arrive by email and in the Formspree dashboard, where they can be exported as CSV. To change service, replace that URL and rebuild.

## Film
`assets/pitch-film.mp4` is the final pitch film (voice only, 2:32); the page's film section plays it, with chapters.
