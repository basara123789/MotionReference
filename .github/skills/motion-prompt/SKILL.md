---
name: motion-prompt
description: Offline-first library of 120 original Motion Prompt animation references, timing specifications and Canvas 2D source code. Use for animation discovery, UI microinteractions, camera moves, motion graphics, landing pages, and visual effects.
---
# Motion Prompt — Offline-first Copilot skill

**Never require an internet connection** for the bundled 120 references. Read the local files in this repository.

## Lookup
The skill lives in `.github/skills/motion-prompt/`. The bundled originals are at repository root `upstream/packs/`:
- `motion`: #001–#024
- `camera`: #025–#048
- `ui`: #049–#072
- `lp`: #073–#096
- `photo`: #097–#120

Each `upstream/packs/<pack>/meta.json` has names, descriptions, prompts, specs, and IDs. Each `upstream/packs/<pack>/pack.js` has all 24 original Canvas 2D implementations and shared helpers.

Run the local no-dependency search CLI from repository root:

```sh
python scripts/motion_lookup.py list
python scripts/motion_lookup.py search modal
python scripts/motion_lookup.py get 049
```

For arbitrary skill consumers, resolve the project repository root rather than assuming current working directory. For an exact implementation, inspect the pack's `pack.js` manually. The code uses `MotionPrompt.pack(...)` and shared kit constants; an individual cell is **not standalone**. If adapting to CSS / React / Remotion, port the behavior and parameters faithfully and state deviations.

## Agent workflow
1. Locate candidate motions with the local CLI or meta JSON; use real IDs only.
2. Read the selected `spec.en` or `spec.ja`, plus `ask`, `summary`.
3. Read matching Canvas 2D implementation and kit in `pack.js`.
4. Implement in user's framework; accommodate `prefers-reduced-motion` and accessibility needs.
5. Cite/reference the motion ID and original author, Shohei Ohtaki.

Do **not** fetch the live website as a prerequisite. This is a pinned snapshot, not an auto-updating upstream sync. Follow the copyright notices in `upstream/LICENSE-MIT.txt` and `upstream/THIRD-PARTY-NOTICES.md`.
