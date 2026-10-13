---
name: ui-motion-design
description: Design and implement accessible web UI transitions and microinteractions using easing, durations and motion presets; use for buttons, cards, menus, modals, page transitions, CSS, Web Animations API and React.
---

# UI Motion Design

Use when asked to design, implement, adjust or reproduce the *behavior* of a UI animation.

## Workflow
1. Identify animated element, event trigger, start/end states, duration, easing, delay and repetition.
2. Read [presets.json](references/presets.json), [implementation.md](references/implementation.md) and [source-notes.md](references/source-notes.md).
3. Presets are **independently authored examples**, not exact source-site values. If given a source animation URL or recording, inspect it before claiming precise values.
4. Implement in the project's own frontend stack, using transform/opacity where possible.
5. Support keyboard/focus interactions and `prefers-reduced-motion`; prevent layout jumps and repeated-animation bugs.
6. Clearly distinguish measured settings from approximate settings.

## Data conventions
- `duration_ms` and `delay_ms`: milliseconds.
- `easing_css`: CSS easing function.
- `keyframes`: 0..1 normalized offsets and CSS-compatible property values.
- `source_status`: `original_example`, `user_verified`, or `site_verified`.

Never assert exact provenance from source-site DOM snapshots without checking their accuracy. Do not copy source artwork, videos or proprietary code.
