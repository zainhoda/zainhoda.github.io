// Native details provide keyboard/touch toggling even without JavaScript.
document.querySelectorAll('.company-card').forEach((card) => {
  let pinned = false;
  let hovered = false;
  const summary = card.querySelector('summary');
  const canHover = window.matchMedia('(hover: hover) and (pointer: fine)');

  card.addEventListener('pointerenter', (event) => {
    if (canHover.matches && event.pointerType !== 'touch') {
      hovered = true;
      card.open = true;
    }
  });
  card.addEventListener('pointerleave', () => {
    hovered = false;
    if (!pinned && !card.contains(document.activeElement)) card.open = false;
  });
  card.addEventListener('focusout', (event) => {
    if (!pinned && !hovered && !card.contains(event.relatedTarget)) card.open = false;
  });
  summary.addEventListener('click', (event) => {
    event.preventDefault();
    pinned = !pinned;
    card.open = pinned;
  });
  card.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      pinned = false;
      card.open = false;
      summary.focus();
    }
  });
});
