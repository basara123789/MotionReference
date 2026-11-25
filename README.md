# MotionReference — offline Copilot motion Skill library

**120 Motion Prompt references stored locally as original source code and specifications.** No network is required for browsing the catalog or reading the actual animations.

## Layout

- `.github/skills/motion-prompt/SKILL.md` — GitHub Copilot Agent skill.
- `upstream/packs/{motion,camera,ui,lp,photo}/pack.js` — **five original Canvas 2D animation packs, 24 each**.
- `upstream/packs/{motion,camera,ui,lp,photo}/meta.json` — motion names and parameter/specification data.
- `scripts/motion_lookup.py` — no-dependency local CLI, list / search / get.
- `upstream/LICENSE-MIT.txt` — original MIT license; `upstream/THIRD-PARTY-NOTICES.md` — upstream notices.

## Test offline from repo root

```sh
python scripts/motion_lookup.py list
python scripts/motion_lookup.py search "modal"
python scripts/motion_lookup.py get 049
```

The `pack.js` modules contain the original drawing code, not standalone individual HTML animations. Their `MotionPrompt.pack` registration depends on a runtime host for rendering; reading/searching/porting the originals does not.

## Use in other projects
Copy `.github/skills/motion-prompt`, **plus** `upstream/packs`, `upstream/LICENSE-MIT.txt`, `upstream/THIRD-PARTY-NOTICES.md`, and `scripts/motion_lookup.py` into the project, preserving relative paths.

Original author: **Shohei Ohtaki**, [Motion Prompt](https://github.com/showheyohtaki/motion-prompt). MIT license; copyright notices retained.

This is a snapshot of upstream, not an automatic mirror. The author's gallery is at https://showheyohtaki.github.io/motion-prompt/.


## Sakuga VFX branch (this branch only)

This `sakuga-vfx` branch preserves the existing Motion Prompt library from `main` and adds a separately vendored Sakuga VFX snapshot under `sakuga-vfx/`. **The `main` branch remains unchanged.**

- Original author: [finktheartist/sakuga-vfx](https://github.com/finktheartist/sakuga-vfx)
- Website: https://sakuga-vfx.vercel.app/gallery/
- License: MIT, retained in [sakuga-vfx/LICENSE](sakuga-vfx/LICENSE)
- Original, standalone Web Components: `button`, `toggle`, `slider`, `checkbox`, `radio`, `input`, `tabs`, `progress`, `rating`, `toast`, `tooltip` (**11 source files**; upstream README calls them 12 but lists only these 11)
- Agent Skill: [.github/skills/sakuga-vfx/SKILL.md](.github/skills/sakuga-vfx/SKILL.md), with its bundled `core.js`, `starter.html`, `look.mjs`
- Local preview: `cd sakuga-vfx && python -m http.server 8000` then open `http://localhost:8000/gallery/` (no CDN dependency; no internet required for stored source)
- Use an individual component by copying its `<component>/<component>.js` into your web project and loading it with a traditional `<script src="..."></script>` tag. Do not load as an ES module.

Upstream has a few separate source art assets, but each component embeds the necessary artwork/core according to the upstream README; binary original authoring assets are not mirrored. The included gallery and components can run with a browser, though real-device compatibility was not independently tested in this branch.

**Updating later:** refresh the vendored `sakuga-vfx/` files on this branch only after comparing new upstream content and preserving the original MIT license. Do not merge into `main` unless you specifically want both libraries on the main branch.
