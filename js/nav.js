/**
 * Progressive enhancement only — primary content is inlined HTML.
 * Mobile nav + active nav highlighting.
 */
(function () {
  function setActiveNav() {
    var page = document.body && document.body.dataset.page;
    if (!page) return;
    document.querySelectorAll('[data-nav]').forEach(function (link) {
      var isActive = link.dataset.nav === page;
      link.classList.toggle('text-ocean-600', isActive);
      link.classList.toggle('font-semibold', isActive);
      link.classList.toggle('text-gray-600', !isActive);
      if (isActive) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    });
  }

  function wireMobileNav() {
    var nav = document.querySelector('#site-nav nav') || document.querySelector('nav');
    if (!nav) return;
    var btn = nav.querySelector('button[aria-label="Open menu"], button[aria-label="Close menu"]');
    if (!btn) return;

    var panel = nav.querySelector('[data-mobile-panel]');
    if (!panel) {
      panel = document.createElement('div');
      panel.setAttribute('data-mobile-panel', 'true');
      panel.className = 'lg:hidden hidden border-t border-ocean-100 bg-white px-4 py-3';
      panel.innerHTML =
        '<div class="flex flex-col gap-1 text-sm font-medium">' +
        '<a href="/" class="py-2 text-gray-700 hover:text-ocean-600">Home</a>' +
        '<a href="/excursions/" class="py-2 text-gray-700 hover:text-ocean-600">Excursions</a>' +
        '<a href="/montego-bay-cruise-port-guide/" class="py-2 text-gray-700 hover:text-ocean-600">Port Guide</a>' +
        '<a href="/one-day-in-montego-bay-from-cruise-ship/" class="py-2 text-gray-700 hover:text-ocean-600">One Day</a>' +
        '<a href="/doctors-cave-beach-montego-bay/" class="py-2 text-gray-700 hover:text-ocean-600">Doctor\'s Cave</a>' +
        '<a href="/private-driver-montego-bay/" class="py-2 text-gray-700 hover:text-ocean-600">Private Driver</a>' +
        '<a href="/contact/" class="py-2 text-gray-700 hover:text-ocean-600">Contact</a>' +
        '</div>';
      nav.appendChild(panel);
    }

    function setOpen(open) {
      panel.classList.toggle('hidden', !open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }

    if (btn.dataset.wired === 'true') return;
    btn.dataset.wired = 'true';
    btn.setAttribute('aria-expanded', 'false');
    btn.addEventListener('click', function () {
      setOpen(panel.classList.contains('hidden'));
    });
    panel.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { setOpen(false); });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    setActiveNav();
    wireMobileNav();
  });
})();
