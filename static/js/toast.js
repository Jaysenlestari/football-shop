function showToast(title, message, type = 'normal', duration = 3000) {
  const toastComponent = document.getElementById('toast-component');
  const toastTitle = document.getElementById('toast-title');
  const toastMessage = document.getElementById('toast-message');

  if (!toastComponent) return;

  // Reset base
  toastComponent.className =
    "fixed bottom-6 right-6 w-80 px-4 py-3 rounded-lg shadow-lg transform transition-all duration-300 opacity-0 translate-y-8 flex flex-col border";

  let borderColor, textColor, glow;

  if (type === 'success') {
    borderColor = 'border-emerald-500/60';
    textColor = 'text-emerald-400';
    glow = 'shadow-emerald-900/30';
  } else if (type === 'error') {
    borderColor = 'border-rose-500/60';
    textColor = 'text-rose-400';
    glow = 'shadow-rose-900/30';
  } else {
    borderColor = 'border-slate-700';
    textColor = 'text-slate-300';
    glow = 'shadow-slate-900/20';
  }

  // Apply style
  toastComponent.classList.add(
    'bg-slate-900',
    borderColor,
    glow,
    'text-slate-200'
  );

  // Set text manually per element
  toastTitle.className = `font-semibold text-base ${textColor}`;
  toastMessage.className = 'text-sm text-slate-400 leading-snug';

  toastTitle.textContent = title;
  toastMessage.textContent = message;

  // Fade in
  requestAnimationFrame(() => {
    toastComponent.classList.remove('opacity-0', 'translate-y-8');
    toastComponent.classList.add('opacity-100', 'translate-y-0');
  });

  // Fade out
  setTimeout(() => {
    toastComponent.classList.remove('opacity-100', 'translate-y-0');
    toastComponent.classList.add('opacity-0', 'translate-y-8');
  }, duration);
}
