<div align="center">

# 💅 L'Atelier Nacré

### Site vitrine pour nail artist / prothésiste ongulaire

Un site **one-page** élégant, rapide et 100 % personnalisable —
sans base de données, sans framework, hébergeable **gratuitement** sur GitHub Pages.

</div>

---

## ✨ Aperçu

Un site clé en main pensé pour une prothésiste ongulaire indépendante :

- **Hero** accrocheur avec appel à la réservation
- **À propos** (bio + valeurs)
- **Prestations & tarifs** en cartes
- **Galerie filtrable** (pose gel, nail art, French, entretien)
- **Avis clientes**
- **FAQ** en accordéon
- **Contact / Réservation** (formulaire + coordonnées + horaires)
- **SEO** local (Open Graph + données structurées `NailSalon`)
- 100 % **responsive**, accessible, animations douces (respecte `prefers-reduced-motion`)

> Le contenu (nom « L'Atelier Nacré », photos, tarifs, avis) est une **démonstration**
> conçue pour être remplacée. Tout est expliqué dans le guide ci-dessous.

---

## 🚀 Démarrage rapide

**Voir le site en local** — aucune installation requise, ouvrez simplement `index.html`
dans un navigateur. Pour un rendu identique à la production (chemins, polices) :

```bash
# avec Python (déjà installé sur Mac/Linux)
python3 -m http.server 8000
# puis ouvrez http://localhost:8000
```

**Mettre en ligne** — voir [`GUIDE-PERSONNALISATION.md`](GUIDE-PERSONNALISATION.md) étape 6
(Settings → Pages → GitHub Actions). Le site se publie tout seul.

---

## 🎨 Le personnaliser

👉 **Tout est dans [`GUIDE-PERSONNALISATION.md`](GUIDE-PERSONNALISATION.md)** — pensé pour
une personne **non-technique**, modifiable directement depuis GitHub dans le navigateur.

En bref :

| Changer… | Fichier |
|---|---|
| Textes, tarifs, coordonnées | `index.html` |
| Couleurs & polices | `css/style.css` (section `:root`) |
| Photos | `assets/images/` |
| E-mail / réservation | `js/main.js` + `index.html` |

---

## 🗂️ Structure du projet

```
NailArtist/
├── index.html                    ← toutes les sections + contenu
├── css/style.css                 ← charte centralisée dans :root
├── js/main.js                    ← menu, filtres, FAQ, animations, formulaire
├── assets/images/                ← visuels (placeholders SVG à remplacer)
├── scripts/generate-placeholders.py   ← régénère les images de démo
├── docs/CAHIER-DES-CHARGES.md    ← vision, périmètre, critères de réussite
├── GUIDE-PERSONNALISATION.md     ← guide pas à pas (non-technique)
└── .github/workflows/deploy.yml  ← déploiement GitHub Pages automatique
```

---

## 🛠️ Technique

- **HTML / CSS / JavaScript** natifs, zéro dépendance, zéro build.
- Compatible tous navigateurs récents, mobile en premier.
- Images de démonstration générées en SVG (`scripts/generate-placeholders.py`).

---

## 📄 Licence

Projet libre d'utilisation et de modification pour l'artiste destinataire.
Fait avec soin 🤍
