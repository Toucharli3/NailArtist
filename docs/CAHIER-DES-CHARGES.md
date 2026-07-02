# Cahier des charges — Site vitrine pour Nail Artist

> Document de référence du projet. Il décrit **pourquoi** le site existe, **pour qui**,
> **ce qu'il contient** et **comment on juge qu'il est réussi**. Il sert aussi de guide
> à la personne qui reprendra le site (« se l'approprier »).

---

## 1. Contexte et objectif

Une prothésiste ongulaire / nail artist indépendante a besoin d'une **vitrine en ligne**
professionnelle pour :

- **Être trouvée** (recherche Google locale, lien en bio Instagram).
- **Rassurer et convaincre** de nouveaux clients (galerie de réalisations, avis, tarifs clairs).
- **Convertir** : faciliter la prise de rendez-vous (formulaire, téléphone, Instagram, DM).

Le site n'est **pas** une boutique e-commerce ni une plateforme de réservation complexe :
c'est une **carte de visite augmentée**, esthétique et rapide, qui met la main-d'œuvre en valeur.

### Objectif mesurable
Qu'une cliente potentielle puisse, en **moins de 30 secondes** et sur mobile :
comprendre le style de l'artiste, voir des exemples, connaître les tarifs et savoir comment réserver.

---

## 2. Cibles (personas)

| Persona | Besoin principal | Ce qu'elle regarde en premier |
|---|---|---|
| **La cliente régulière** | Reprendre RDV vite | Bouton « Réserver », horaires, tarifs |
| **La nouvelle cliente** | Se rassurer sur la qualité | Galerie, avis, à propos |
| **La curieuse Instagram** | Voir plus que le feed | Galerie, lien Insta, prestations |

**Appareil dominant : mobile.** Le site est conçu *mobile-first*.

---

## 3. Périmètre fonctionnel

### Inclus (V1)
- [x] Page unique (one-page) avec navigation ancrée
- [x] En-tête collant avec bouton d'appel à l'action (« Réserver »)
- [x] Section **Hero** (nom, accroche, CTA)
- [x] Section **À propos** (bio + portrait)
- [x] Section **Prestations & tarifs** (cartes de services)
- [x] Section **Galerie** filtrable (pose, nail art, French, entretien…)
- [x] Section **Avis clients**
- [x] Section **FAQ**
- [x] Section **Réservation / Contact** (formulaire, coordonnées, horaires, adresse)
- [x] Pied de page (réseaux sociaux, mentions, copyright)
- [x] Responsive (mobile / tablette / desktop)
- [x] Animations douces au défilement
- [x] SEO de base (title, meta description, Open Graph, données structurées LocalBusiness)
- [x] Accessibilité de base (contrastes, navigation clavier, `alt`, `aria`)

### Volontairement exclu de la V1 (évolutions possibles)
- [ ] Réservation en ligne avec paiement (intégration Planity/Treatwell/Calendly recommandée en V2)
- [ ] Blog / articles
- [ ] Multilingue
- [ ] Espace client / comptes
- [ ] Back-office de gestion de contenu (CMS)

---

## 4. Arborescence et contenu

Site **one-page**, sections dans cet ordre :

1. **Accueil (Hero)** — nom de la marque, accroche, 1 phrase de positionnement, CTA « Réserver » + « Voir la galerie ».
2. **À propos** — histoire, philosophie, hygiène/qualité, portrait.
3. **Prestations** — 4 à 8 prestations, chacune : titre, description courte, durée, prix « à partir de ».
4. **Galerie** — 8 à 12 visuels minimum, filtrables par catégorie.
5. **Avis** — 3 à 6 témoignages (prénom + note).
6. **FAQ** — 4 à 8 questions fréquentes (tenue, entretien, annulation, moyens de paiement…).
7. **Réservation / Contact** — formulaire + téléphone + Instagram + adresse + horaires.
8. **Footer** — réseaux, copyright, lien mentions légales.

---

## 5. Exigences non-fonctionnelles

| Critère | Cible |
|---|---|
| **Performance** | Chargement < 2 s en 4G ; images optimisées (WebP conseillé) |
| **Poids** | Site statique, aucune dépendance lourde, pas de framework |
| **Compatibilité** | Chrome, Safari, Firefox, Edge (2 dernières versions) ; iOS & Android |
| **Accessibilité** | Contraste AA, focus visible, structure sémantique, `prefers-reduced-motion` |
| **SEO** | Balises méta, titres hiérarchisés, `sitemap`/`robots`, JSON-LD LocalBusiness |
| **Maintenabilité** | 1 seul fichier de contenu HTML lisible + variables CSS pour la charte |
| **Hébergement** | GitHub Pages (gratuit, HTTPS) |
| **Coût** | 0 € (hors nom de domaine optionnel ~10 €/an) |

---

## 6. Charte graphique (proposition de départ)

Univers : **boutique, féminin, élégant, moderne, chaleureux** — pas enfantin, pas criard.

| Élément | Valeur par défaut | Où la changer |
|---|---|---|
| Fond crème | `#FBF7F4` | `css/style.css` → `:root` |
| Texte (encre) | `#2B2422` | idem |
| Nude / taupe | `#C9AE9E` | idem |
| Rose poudré (accent) | `#C98A8A` | idem |
| Prune profond | `#6E4555` | idem |
| Or (détails) | `#B8933F` | idem |
| Titres | Serif élégante (Cormorant Garamond) | `<head>` + CSS |
| Textes | Sans-serif lisible (Inter) | `<head>` + CSS |

> Toute la charte est centralisée dans les **variables CSS** (`:root`) en haut de `css/style.css`.
> Changer 6 couleurs suffit à re-brander tout le site.

---

## 7. Contenu à fournir par l'artiste (checklist)

Pour rendre le site réel, l'artiste remplace le contenu de démonstration par :

- [ ] Nom de la marque / du studio + logo (optionnel)
- [ ] 1 portrait + 8 à 12 photos de réalisations (carrées, bonne lumière)
- [ ] Texte « à propos » (5–8 lignes)
- [ ] Liste des prestations avec durées et tarifs réels
- [ ] 3 à 6 avis clients (avec accord des clientes)
- [ ] Coordonnées : téléphone, e-mail, Instagram, adresse, horaires
- [ ] Lien de réservation si outil externe (Planity, Treatwell, Calendly…)
- [ ] Mentions légales (statut, SIRET si applicable)

👉 Tout est expliqué pas à pas dans **`GUIDE-PERSONNALISATION.md`**.

---

## 8. Critères d'acceptation (« le site est réussi si… »)

1. Le site s'affiche correctement sur un iPhone et un ordinateur.
2. On peut naviguer entièrement au clavier ; le focus est visible.
3. Les tarifs et la façon de réserver sont visibles sans effort.
4. La galerie se filtre sans rechargement de page.
5. Le formulaire de contact fonctionne (ouvre l'e-mail pré-rempli, ou service externe).
6. Une personne non-technique peut changer une couleur, un texte et une photo
   en suivant le guide, sans casser le site.
7. Score Lighthouse mobile ≥ 90 en Performance et Accessibilité (objectif).

---

## 9. Évolutions prévues (roadmap)

- **V2** : réservation en ligne (Calendly/Planity intégré), Google Maps, WebP + lazy-loading avancé.
- **V3** : carte cadeau, mini-blog conseils, avis Google en direct, nom de domaine personnalisé.

---

## 10. Livrables

- Site statique complet (`index.html`, `css/`, `js/`, `assets/`)
- Ce cahier des charges (`docs/CAHIER-DES-CHARGES.md`)
- Guide de personnalisation (`GUIDE-PERSONNALISATION.md`)
- Workflow de déploiement GitHub Pages (`.github/workflows/deploy.yml`)
- `README.md` de prise en main
