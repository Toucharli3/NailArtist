# 💅 Guide de personnalisation — se l'approprier en 30 minutes

Ce site est **entièrement à vous**. Aucune compétence technique n'est nécessaire :
tout se modifie depuis le site GitHub, directement dans le navigateur, en cliquant
sur le petit **crayon ✏️** en haut à droite de chaque fichier, puis **Commit changes**.

> 💡 **Astuce** : faites une modification à la fois et regardez le résultat. Rien n'est cassable :
> tout l'historique est sauvegardé, on peut toujours revenir en arrière.

---

## Vue d'ensemble : où se trouve quoi

| Je veux changer… | Fichier à ouvrir |
|---|---|
| Les **textes** (nom, bio, prestations, avis, FAQ, contact) | `index.html` |
| Les **couleurs** et **polices** | `css/style.css` (tout en haut, section `:root`) |
| Les **photos** | dossier `assets/images/` |
| L'**e-mail** qui reçoit les demandes | `js/main.js` (variable `DESTINATION_EMAIL`) + `index.html` |
| Le **titre Google** et la description | `index.html` (balises `<title>` et `<meta name="description">`) |

---

## Étape 1 — Changer le nom et les textes

Ouvrez **`index.html`**. Tout le contenu visible est là, en français clair.
Utilisez la recherche du navigateur (`Ctrl/Cmd + F`) pour trouver le texte à remplacer.

À personnaliser en priorité :
- `L'Atelier Nacré` → votre nom de marque (apparaît plusieurs fois : en-tête, footer, SEO).
- `Camille` → votre prénom (section « À propos » + signature sur la photo).
- La bio dans la section **À propos**.
- Les **prestations** et **tarifs** (section `id="prestations"`).
- Les **avis** clients (section `id="avis"`).
- Les **questions/réponses** de la **FAQ**.
- Les **coordonnées** : téléphone, e-mail, Instagram, adresse, horaires (section `id="contact"`).

> Les zones importantes sont repérées par des commentaires `<!-- 📷 … -->` ou `<!-- 💶 … -->`.

---

## Étape 2 — Changer les couleurs (le « re-branding »)

Ouvrez **`css/style.css`**. Tout en haut, la section `:root` contient **6 couleurs**.
Changez-les, et toute l'ambiance du site change instantanément :

```css
:root {
  --c-cream:  #FBF7F4;   /* fond principal, crème */
  --c-ink:    #2B2422;   /* texte principal */
  --c-nude:   #C9AE9E;   /* nude / taupe */
  --c-blush:  #C98A8A;   /* rose poudré (accent) */
  --c-plum:   #6E4555;   /* couleur forte (boutons, titres) */
  --c-gold:   #B8933F;   /* touches dorées */
}
```

👉 Pour trouver de jolies combinaisons, cherchez un code couleur sur
[coolors.co](https://coolors.co) et collez-le (format `#RRGGBB`).

**Changer les polices** : dans `index.html`, ligne `<link ... fonts.googleapis.com ...>`,
remplacez `Cormorant+Garamond` (titres) et `Inter` (textes) par d'autres polices
[Google Fonts](https://fonts.google.com). Puis mettez à jour `--font-title` et
`--font-body` dans `css/style.css`.

---

## Étape 3 — Remplacer les photos

Les images de démonstration sont dans **`assets/images/`**. Deux méthodes :

**Méthode simple (recommandée)** — gardez les mêmes noms de fichiers :
1. Préparez vos photos en **carré** pour la galerie (`galerie-01` à `galerie-12`) et
   en **portrait** pour `hero` et `portrait`.
2. Nommez-les exactement comme les fichiers existants mais en `.jpg` (ex. `galerie-01.jpg`).
3. Uploadez-les dans `assets/images/` (bouton **Add file → Upload files** sur GitHub).
4. Dans `index.html`, remplacez les `.svg` par vos `.jpg` (ex. `galerie-01.svg` → `galerie-01.jpg`).

**Conseils photo** : lumière naturelle, fond neutre, format carré ~1000×1000 px,
poids < 300 Ko (compressez sur [squoosh.app](https://squoosh.app), format **WebP** idéal).

> La catégorie de chaque photo de galerie est définie par `data-cat="..."`
> (`gel`, `nailart`, `french`, `entretien`) — c'est ce qui pilote les filtres.

---

## Étape 4 — Recevoir les demandes de rendez-vous

Par défaut, le formulaire **ouvre l'e-mail** pré-rempli de la visiteuse. Simple, mais elle doit
avoir une messagerie configurée. Deux améliorations possibles :

**A. Juste changer l'e-mail de destination** (garde le fonctionnement par défaut) :
- Dans `js/main.js`, remplacez `contact@atelier-nacre.fr` par votre e-mail.
- Dans `index.html`, remplacez aussi les `mailto:` et le numéro affichés.

**B. Recevoir les messages sans que la cliente ouvre sa messagerie** (recommandé) —
avec [Formspree](https://formspree.io) (gratuit) :
1. Créez un compte, créez un formulaire, copiez son URL (`https://formspree.io/f/xxxx`).
2. Dans `index.html`, sur la balise `<form ...>`, ajoutez :
   `action="https://formspree.io/f/xxxx" method="POST"`.
3. Dans `js/main.js`, bloc « 7. Formulaire », commentez la partie `mailto` (ou supprimez le
   `e.preventDefault()`) pour laisser le formulaire s'envoyer normalement.

**C. Réservation en ligne** : ajoutez un bouton vers [Planity](https://www.planity.com),
[Treatwell](https://www.treatwell.fr) ou [Calendly](https://calendly.com). Remplacez la
cible des boutons « Réserver » (`href="#contact"`) par votre lien de réservation.

---

## Étape 5 — Soigner le référencement (Google)

Dans `index.html`, `<head>` :
- `<title>` : le titre affiché dans Google (nom + ville + spécialité fonctionne bien,
  ex. « L'Atelier Nacré — Nail Artist à Lyon »).
- `<meta name="description">` : la phrase sous le titre dans Google (~150 caractères).
- Bloc `application/ld+json` : renseignez votre **vrai nom, adresse, téléphone, horaires**.
  Cela aide Google à afficher votre fiche locale.

Pensez aussi à créer une **fiche Google Business Profile** (gratuit) — c'est le levier n°1
pour être trouvée localement.

---

## Étape 6 — Mettre le site en ligne (GitHub Pages)

Le site s'héberge **gratuitement** sur GitHub Pages :
1. Sur GitHub, allez dans **Settings → Pages**.
2. Dans **Build and deployment → Source**, choisissez **GitHub Actions**.
3. Le workflow `.github/workflows/deploy.yml` publie automatiquement à chaque modification.
4. Votre site sera en ligne sur `https://VOTRE-PSEUDO.github.io/NailArtist/`.

> Vous pouvez ensuite brancher un **nom de domaine** personnalisé
> (ex. `atelier-nacre.fr`, ~10 €/an) dans **Settings → Pages → Custom domain**.

---

## Récapitulatif express

1. Textes → `index.html`
2. Couleurs/polices → `css/style.css` (section `:root`) + lien Google Fonts
3. Photos → `assets/images/`
4. E-mail/réservation → `js/main.js` + `index.html`
5. SEO → balises `<head>` de `index.html`
6. Mise en ligne → Settings → Pages → GitHub Actions

Besoin d'aller plus loin ? Le **cahier des charges** (`docs/CAHIER-DES-CHARGES.md`)
décrit la vision complète et les évolutions possibles. Bonne appropriation ! 🤍
