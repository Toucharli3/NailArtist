# 📅 Réservation en ligne — Cal.com (indépendant, sans iara)

Le site a **son propre agenda de réservation**, intégré directement dans la page
(section « Réservation »). Il fonctionne avec **Cal.com** : gratuit, à Margot, sans iara.

---

## Mise en place (une fois, ~10 min) — par Margot

1. **Créer le compte** : va sur **cal.com** → *Sign up* (gratuit).
2. Choisir son **identifiant** (username), par ex. **`orange-blossom-nails`**.
   > C'est ce qui apparaîtra dans l'adresse : `cal.com/orange-blossom-nails`.
3. **Connecter son agenda** (Google Agenda / Apple) pour bloquer ses indispos.
4. Régler ses **disponibilités** (jours/horaires : mardi → samedi).
5. Créer ses **types de rendez-vous** (durées correspondant aux prestations,
   ex. « Pose Gel X — 1 h 30 »). On peut activer un **acompte** (via Stripe) et des
   **rappels** email/SMS.

---

## Brancher l'agenda sur le site

Il suffit de remplacer l'identifiant d'exemple par le vrai, à **2 endroits** dans `index.html` :

1. Cherche `orange-blossom-nails` (commentaire « 👈 identifiant Cal.com de Margot »).
2. Remplace-le par le **vrai username** choisi à l'étape 2.
   - Pour cibler un type de RDV précis : `identifiant/nom-du-type` (ex. `orange-blossom-nails/pose-gel-x`).
3. Enregistre → l'agenda s'affiche sur le site, dans la section « Réservation ».

> 💡 Dis-le-moi et je fais ce remplacement pour toi en 10 secondes dès que le compte
> Cal.com existe et que tu m'as donné l'identifiant.

---

## Ce que ça remplace
- ❌ Plus de **iara** (aucun lien, aucune dépendance).
- ✅ Réservation **sur le site**, agenda **à Margot**, aux couleurs du site (terracotta).
- ✅ Gratuit au départ ; options payantes (acomptes, SMS) seulement si elle les veut.

---

## Coût
- Cal.com : **0 €** (offre gratuite) ; options avancées ~selon besoins.
- Aucun surcoût d'hébergement (l'agenda est chez Cal.com, le site reste gratuit).
