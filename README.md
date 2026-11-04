# Veritas: pre-release site

Static landing page for **Veritas**, "Master what you read." Launching December 2026.

- `index.html` + `assets/`: the built site. Host it anywhere that serves static files (GitHub Pages, Netlify, Cloudflare Pages).
- `src/page.html`: the single source of the page. `src/build_site.py` wraps it into `index.html` and copies `assets/`.

## Rebuild
Edit `src/page.html`, then run `python3 src/build_site.py` (see the script header for paths and the optional base URL).

## Waitlist
The form is a **placeholder**: it shows the success message and keeps the address only in the visitor's own browser. **Nothing is collected yet.**
To collect sign-ups, create a form with a service such as Formspree, Tally or Google Forms, and set `WAITLIST_ENDPOINT` near the top of the script in `src/page.html`, then rebuild.

## Films
`assets/pitch-film.mp4` is the final pitch film (voice only, 2:32). `assets/film.mp4` is the longer launch film the page's "Watch the launch film" section plays.
