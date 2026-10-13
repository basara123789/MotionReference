# Motion Reference → GitHub Copilot Agent Skills

Reusable UI motion-design skill inspired by [MOTION MOVEMENT REFERENCE](https://motion-reference.takayustudio.jp/).

> **Data provenance:** This repository is **not an export or mirror** of the source site. The 10 starter presets are independently authored examples, **not verified parameters from that website**. The capture helper produces unverified local snapshots for manual review.

## Files

- `.github/skills/ui-motion-design/SKILL.md` — Copilot Agent Skill instructions.
- `.github/skills/ui-motion-design/references/presets.json` — 10 original reference presets.
- `.github/skills/ui-motion-design/references/implementation.md` — CSS and WAAPI examples.
- `.github/skills/ui-motion-design/references/source-notes.md` — source and license cautions.
- `scripts/capture_site.py` — interactive local Playwright capture helper.

## Use with Copilot

This skill can be discovered when Copilot Agent operates **inside this repository**. For use in another project, copy `.github/skills/ui-motion-design/` to that project's `.github/skills/` or install the skill to your supported personal skills directory.

Suggested prompt:

> Use the ui-motion-design skill to animate a modal opening, respecting prefers-reduced-motion and the current frontend stack.

## Optional local capture

```bash
pip install playwright
python -m playwright install chromium
python scripts/capture_site.py
```

Interactively select a motion reference in the browser and press Enter in the terminal to save a screenshot and DOM animation metadata in ignored `captures/`. DOM data is **not necessarily exact source animation parameters**; verify before importing.

## Rights

Respect the source author's terms and permission requirements. Do not publish bulk-copied source datasets, images or proprietary implementation code without authorization.
