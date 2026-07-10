# 🚀 Rendre le site 100 % pro & autonome — plan d'action

Objectif : Margot se connecte avec **email + mot de passe** sur **son-site/admin**,
modifie **tout** (bio, textes, tarifs, photos) dans un éditeur visuel, et ses **photos
Instagram** s'affichent automatiquement — le tout sans code et sans « bricolage ».

Deux briques choisies : **A. TinaCMS** (login + édition) · **B. Flux Instagram + coups de cœur**.

---

## A. Espace admin avec login email/mot de passe — TinaCMS

TinaCMS = un éditeur visuel qui se greffe sur le site actuel. Margot se connecte,
clique sur un texte ou une photo, modifie, et ça s'enregistre tout seul.

### Ce que TU/Margot faites (une fois, ~10 min)
1. Aller sur **app.tina.io** → créer un compte (email ou Google).
2. **New Project** → connecter le dépôt GitHub **NailArtist**.
3. Récupérer les 2 clés fournies : **Client ID** et **Token** (lecture) → me les donner
   (ou les coller dans les réglages du dépôt, je t'indique où).
4. Inviter Margot par **email** comme éditrice → elle aura **son login email/mot de passe**.

### Ce que JE fais
- J'ajoute la configuration Tina (les « champs » : bio, accroche, tarifs, galerie…).
- Je génère la page **/admin** visuelle.
- Je branche le contenu du site sur ces champs (textes déjà prêts en fichiers `content/`).

### Le résultat
Margot va sur **son-site/admin**, se connecte par **email/mot de passe**, et modifie
**bio, textes, tarifs, photos** au clic. ✨

> ⚠️ Honnêteté : je ne peux pas **tester le login** depuis mon environnement (réseau
> bloqué). Je mets tout en place, et on finalise ensemble en un court aller-retour.

---

## B. Photos : flux Instagram automatique + coups de cœur

### B1. Flux automatique (ses derniers posts)
Instagram interdit l'aspiration directe → on utilise un **widget officiel** (gratuit) :
1. Créer un compte sur **snapwidget.com** (ou lightwidget.com) → connecter **@orange.blossom.nails** (public).
2. Choisir une grille, copier le **code d'intégration**.
3. Me le donner → je l'insère dans une section « Sur Instagram » : la galerie se met à
   jour **toute seule** quand Margot poste. 🔄

### B2. Coups de cœur (choisis à la main)
Déjà en place : via l'admin, Margot **épingle** ses plus belles réalisations
(section « Galerie », qualité et ordre maîtrisés).

---

## C. Enlever tout ce qui reste « fictif »
- ✅ Textes : déjà **100 % réels** (bio Margot, 21 tarifs, ville, note 5/5).
- ⏳ **Visuels de démo** (galerie, portrait, hero) → remplacés par ses vraies photos via A/B.
- Dès qu'une vraie photo arrive, on retire le placeholder correspondant.

---

## D. Check-list « très pro » (au-delà de l'admin)
- [ ] **Nom de domaine** perso (ex. `orangeblossomnails.fr`) — son adresse à elle
- [ ] **Fiche Google Business Profile** (gratuit) — le levier n°1 pour être trouvée à Guidel
- [ ] **Mentions légales complètes** (SIRET, statut, adresse) — obligatoire
- [ ] **Vraies photos** en bonne qualité, format cohérent
- [ ] **Logo définitif** si Margot en a un (sinon le nôtre convient)
- [ ] Option : **carte cadeau**, mise en avant des **avis Google**, page **contact** enrichie
- [ ] Déjà OK : responsive, vitesse, SEO de base, réservation en ligne

---

## Ordre conseillé
1. **Créer le compte Tina** (débloque l'édition par Margot) → je branche l'admin.
2. **Widget Instagram** → photos automatiques.
3. **Compléter les infos légales** → je finalise les mentions.
4. **Nom de domaine** → je branche le `CNAME`.
5. **Fiche Google Business** → visibilité locale.

→ Étape 1 = créer le compte **app.tina.io**. Dis-moi quand c'est fait (ou si tu veux que
je te guide écran par écran), et je monte l'éditeur visuel.
