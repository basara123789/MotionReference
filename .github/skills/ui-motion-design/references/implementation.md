# Implementation recipes

These values are handcrafted examples; **not values extracted from the source site**.

## CSS card entrance

```css
.card { animation: card-enter 320ms cubic-bezier(.2,.8,.2,1) both; }
@keyframes card-enter {
  from { opacity: 0; transform: translateY(12px) scale(.985); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}
@media (prefers-reduced-motion: reduce) {
  .card { animation: none; }
}
```

## Web Animations API

```js
function reveal(el) {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  el.animate(
    [{ opacity: 0, transform: 'translateY(12px)' },
     { opacity: 1, transform: 'translateY(0)' }],
    { duration: 320, easing: 'cubic-bezier(.2,.8,.2,1)', fill: 'both' }
  );
}
```

Use separate enter/exit treatments. Avoid animated layout properties on frequently changing elements.
