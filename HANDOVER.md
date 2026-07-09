# 🤝 Plan de remise en main — « le site entre les mains de Margot »

Objectif : Margot possède **son** site et le gère seule via un **panneau d'admin**,
sans jamais avoir à toucher au code. Ce document est la feuille de route de la
passation, du plus important au plus optionnel.

---

## 1. Comment ça marche (en une image)

```
   Margot                    Panneau d'admin              Le site (public)
  (son tel)  ───────────▶   app.pagescms.org   ───────▶  son-domaine.fr
  ajoute une photo          (enregistre dans…)           (se met à jour seul)
                                   │
                                   ▼
                          GitHub (moteur invisible :
                          stockage + hébergement gratuit)
```

- Margot voit **2 choses** : son **site** et son **panneau**.
- GitHub travaille en coulisses — elle n'a pas besoin de le comprendre.
- Les **réservations** passent déjà par sa page **iara** (rien à gérer côté site).

---

## 2. Ce que Margot pourra gérer elle-même

| Aujourd'hui | Bientôt (phase 2, voir §6) |
|---|---|
| ✅ Ajouter / supprimer / réordonner ses **photos** | ⏳ Modifier ses **tarifs & prestations** |
| ✅ Écrire les **légendes** et catégories | ⏳ Modifier sa **bio** et les textes d'accueil |
| ✅ (via panneau, sans code) | ⏳ (via le même panneau) |

Réservations, avis : gérés automatiquement via **iara** (déjà branché).

---

## 3. La passation, étape par étape

### Étape A — Margot crée son compte GitHub (5 min, une seule fois)
GitHub sert de **propriété + clé du panneau**. Elle n'aura pas à s'en reservir ensuite.
→ github.com → Sign up (email + mot de passe).

### Étape B — Le site devient SA propriété
Deux options :
- **Transfert** du dépôt actuel vers son compte (Settings → Danger Zone → *Transfer ownership*), **ou**
- On recrée le dépôt sous son compte et on y pousse le site (je te guide).

→ Résultat : elle est **propriétaire** de son site.

### Étape C — Remettre le site en ligne sous son compte
Sur son dépôt : **Settings → Pages → Deploy from a branch** → branche `main` → `/(root)` → Save.
(1 à 2 min, la bannière verte donne l'adresse `sonpseudo.github.io/…`.)

### Étape D — Son adresse à elle (nom de domaine) — *recommandé*
Un domaine pro coûte ~10 €/an (ex. **orangeblossomnails.fr**).
- Acheter chez OVH / Gandi / Namecheap.
- Dans **Settings → Pages → Custom domain**, saisir le domaine + suivre les 2 lignes DNS indiquées.
- Le fichier `CNAME` (voir §5) fige l'adresse.
→ Résultat : plus de « github.io » — **son nom, son site**.

### Étape E — Son accès admin
→ **app.pagescms.org** → *Sign in with GitHub* (son compte) → autoriser le dépôt `NailArtist`.
C'est **son panneau**. Voir `GUIDE-ADMIN.md`.

### Étape F — Elle prend la main
Elle ajoute ses photos, on retire les visuels de démo, et le site vit tout seul.

---

## 4. Qui fait quoi

| Tâche | Qui | Où |
|---|---|---|
| Créer le compte GitHub de Margot | Toi + Margot | github.com |
| Transférer / recréer le dépôt | Toi (je te guide) | GitHub |
| Réactiver Pages | Toi | Settings → Pages |
| Acheter + brancher le domaine | Toi + Margot | Registrar + Settings → Pages |
| Connecter le panneau admin | Margot | app.pagescms.org |
| Gérer les photos au quotidien | **Margot, seule** | Panneau admin |
| Modifier le code / design | Moi (sur demande) | — |

---

## 5. Nom de domaine — fichier CNAME
Quand le domaine est choisi, créer à la racine un fichier **`CNAME`** contenant
uniquement le domaine, ex. :
```
orangeblossomnails.fr
```
(Le panneau *Settings → Pages → Custom domain* le crée automatiquement quand on
saisit le domaine — rien à faire à la main.)

---

## 6. Phase 2 — rendre les TEXTES et TARIFS modifiables au panneau
Aujourd'hui la galerie est « pilotée par données » (`content/gallery.json`) → gérable au panneau.
Prochaine étape : faire pareil pour les **prestations/tarifs**, la **bio** et l'**accroche**
(`content/site.json`) pour que Margot modifie **tout** depuis le panneau, sans code.
→ À faire sur simple demande (c'est déjà préparé côté architecture).

---

## 7. Variante « admin 100 % sans GitHub » (optionnelle)
Si tu veux que Margot se connecte au panneau avec **juste un email + mot de passe**
(zéro compte GitHub), il faut déménager l'hébergement sur **Netlify** (gratuit) et
utiliser **Decap CMS + Netlify Identity**. Même site, même panneau visuel, mais login par email.
Plus de mise en place ; à envisager seulement si le login GitHub la gêne vraiment.

---

## En résumé
1. Compte GitHub Margot → 2. Dépôt à son nom → 3. Pages activé → 4. Domaine perso →
5. Panneau admin connecté → 6. Elle gère ses photos seule. 🌸
Le tout **gratuit** (hors domaine ~10 €/an), et sans qu'elle ait jamais à coder.
