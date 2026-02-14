// Minimal client-side behavior for result page
// - Press Escape to return home (start new diagnosis)
// - Focus the answer box for accessibility when page loads

document.addEventListener('DOMContentLoaded', () => {
  const answerPre = document.getElementById('answerPre');
  const newBtn = document.getElementById('newDiagnosisBtn');

  // Focus the answer container so screen readers start reading
  if (answerPre && typeof answerPre.focus === 'function') {
    answerPre.setAttribute('tabindex', '-1');
    // answerPre.focus();
  }

  // Escape key to go home
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      // navigate back to the diagnose page
      if (newBtn && newBtn.href) {
        window.location.href = newBtn.href;
      } else {
        window.location.href = '/';
      }
    }
  });
});