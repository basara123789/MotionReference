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
