/* =====================================================================
   L'ATELIER NACRÉ — Interactions
   Vanilla JS, aucune dépendance. Chaque bloc est indépendant et commenté.
   ===================================================================== */
(function () {
  'use strict';

  /* ---------- 1. Année courante dans le footer ---------- */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- 2. En-tête : ombre au défilement ---------- */
  var header = document.querySelector('.site-header');
  var onScroll = function () {
    if (header) header.classList.toggle('scrolled', window.scrollY > 8);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---------- 3. Menu mobile (burger) ---------- */
  var toggle = document.getElementById('navToggle');
  var menu = document.getElementById('menu');
  if (toggle && menu) {
    var closeMenu = function () {
      menu.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Ouvrir le menu');
    };
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
    });
    // Fermer au clic sur un lien, ou avec Échap
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeMenu);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeMenu();
    });
  }

  /* ---------- 4. Galerie : rendu depuis content/gallery.json ----------
     Les photos sont une simple liste dans content/gallery.json — modifiable
     à la main ou via le panneau d'administration. Ajouter une photo = ajouter
     une entrée { image, caption, category } et déposer le fichier image.
  */
  function escapeHtml(s) {
    return String(s || '').replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function catLabel(cat) {
    return { gel: 'Pose gel', nailart: 'Nail art', french: 'French', entretien: 'Entretien' }[cat] || '';
  }
  function renderGallery(list) {
    var gallery = document.getElementById('gallery');
    if (!gallery || !Array.isArray(list)) return;
    gallery.innerHTML = list.map(function (it) {
      var cap = escapeHtml(it.caption);
      var tag = catLabel(it.category);
      return '<figure class="gallery-item" data-cat="' + escapeHtml(it.category) + '">' +
        '<img src="' + escapeHtml(it.image) + '" alt="' + (cap || 'Réalisation nail art') + '" loading="lazy" />' +
        (cap ? '<figcaption class="cap">' + (tag ? '<span class="tag">' + tag + '</span>' : '') + cap + '</figcaption>' : '') +
        '</figure>';
    }).join('');
  }
  var galleryEl = document.getElementById('gallery');
  if (galleryEl) {
    fetch('content/gallery.json', { cache: 'no-store' })
      .then(function (r) { return r.json(); })
      .then(renderGallery)
      .catch(function () { /* fetch indisponible (ouverture en local) : galerie vide */ });
  }

  /* ---------- 4c. Prestations : rendu depuis content/services.json ----------
     Tarifs modifiables à la main ou via le panneau d'administration.
  */
  function renderServices(list) {
    var el = document.getElementById('services');
    if (!el || !Array.isArray(list)) return;
    var cards = list.map(function (s) {
      return '<article class="service reveal in">' +
        '<div class="s-ic" aria-hidden="true">✦</div>' +
        '<h3>' + escapeHtml(s.title) + '</h3>' +
        '<p>' + escapeHtml(s.description) + '</p>' +
        '<div class="s-meta"><span class="price">' + escapeHtml(s.price) + '</span>' +
        '<span class="dur">' + escapeHtml(s.duration) + '</span></div></article>';
    }).join('');
    var cta = '<article class="service reveal in" style="justify-content:center; text-align:center; background:var(--c-plum); color:var(--c-cream);">' +
      '<h3 style="color:var(--c-white);">Et bien plus…</h3>' +
      '<p style="color:color-mix(in srgb, var(--c-cream) 82%, transparent);">Découvre l\'ensemble des soins et réserve ton créneau directement en ligne.</p>' +
      '<a class="btn btn-ghost" style="background:var(--c-white); border-color:var(--c-white);" href="https://iarabeauty.com/fr/pro/orangeblossomnails" target="_blank" rel="noopener">Voir tous les soins</a></article>';
    el.innerHTML = cards + cta;
  }
  var servicesEl = document.getElementById('services');
  if (servicesEl) {
    fetch('content/services.json', { cache: 'no-store' })
      .then(function (r) { return r.json(); })
      .then(renderServices)
      .catch(function () { /* fetch indisponible : section vide */ });
  }

  /* ---------- 4b. Filtres de la galerie ---------- */
  var filters = document.querySelectorAll('.filter');
  filters.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filters.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      var cat = btn.getAttribute('data-filter');
      document.querySelectorAll('.gallery-item').forEach(function (item) {
        var show = cat === 'all' || item.getAttribute('data-cat') === cat;
        item.classList.toggle('hide', !show);
      });
    });
  });

  /* ---------- 5. FAQ (accordéon accessible) ---------- */
  document.querySelectorAll('.faq-q').forEach(function (q) {
    q.addEventListener('click', function () {
      var item = q.closest('.faq-item');
      var answer = item.querySelector('.faq-a');
      var isOpen = item.classList.toggle('open');
      q.setAttribute('aria-expanded', String(isOpen));
      answer.style.maxHeight = isOpen ? answer.scrollHeight + 'px' : null;
    });
  });

  /* ---------- 6. Animations au défilement (reveal) ---------- */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var reveals = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    reveals.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  }

  /* ---------- 7. Formulaire de contact ----------
     Par défaut : ouvre l'e-mail pré-rempli du visiteur (aucun serveur requis).
     Pour recevoir les demandes directement dans votre boîte SANS ouvrir le
     client mail du visiteur, branchez un service comme Formspree :
     voir GUIDE-PERSONNALISATION.md, étape 6.
  */
  var DESTINATION_EMAIL = 'contact@atelier-nacre.fr'; // ✉️ Mettez VOTRE e-mail ici
  var form = document.getElementById('contactForm');
  var success = document.getElementById('formSuccess');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }

      var get = function (id) {
        var el = document.getElementById(id);
        return el ? el.value.trim() : '';
      };
      var sujet = 'Demande de rendez-vous — ' + (get('nom') || 'Site web');
      var corps =
        'Prénom & nom : ' + get('nom') + '\n' +
        'Téléphone : ' + get('tel') + '\n' +
        'E-mail : ' + get('email') + '\n' +
        'Prestation : ' + get('presta') + '\n\n' +
        'Message :\n' + get('message');

      window.location.href = 'mailto:' + DESTINATION_EMAIL +
        '?subject=' + encodeURIComponent(sujet) +
        '&body=' + encodeURIComponent(corps);

      if (success) {
        success.classList.add('show');
        success.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
      }
      form.reset();
    });
  }
})();
