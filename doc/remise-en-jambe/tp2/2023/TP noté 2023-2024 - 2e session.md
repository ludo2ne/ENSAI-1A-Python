
# STID - Complément d'informatique

### TP Noté 2023-2024 - 2e session

* à rendre soit seul, soit par groupe de 2
* Déposez sous Moodle, vos 2 fichiers python nommés : 
    * `ex1.py`
    * `ex2.py`
* date limite : :construction: 
* Commentez et expliquez ce que font vos algorithmes


## :arrow_forward: Avant de commencer

* [ ] Créez sur votre disque P, un dossier TP2
* [ ] Ouvrez Visual Studio Code
    * [ ] File > Open Folder > TP2
* Dans le dossier TP2, créez 2 sous-dossiers
    * [ ] src : qui contient les sources Python
    * [ ] data : qui contient les fichiers de données
* [ ] Importez depuis Moodle les 2 fichiers de données et déposez les dans le sous-dossier `/data`
* [ ] Dans le sous-dossier `/src`, créer 2 fichiers : `ex1.py` et `ex2.py`
    * [ ] Indiquez en commentaire en haut des 2 fichiers vos noms et prénoms


## :arrow_forward: Exercice 1 

### Objectif

Ecrire une fonction qui : 
* prend en entrée une chaine de caractères qui sera composée
    * de plusieurs lignes
    * chaque ligne contenant des caractères alphabétiques (a...z et A...Z)
* pour chacune des lignes
    * coupe la chaine au milieu en 2 parties égales
    * recherche la lettre commune entre les 2 parties en respectant la casse
        * ce qui veut dire que "A" est différent de "a"
    * convertit cette lettre en entier
        * a = 1
        * b = 2
        * ...
        * z = 26
        * A = 27
        * B = 28
        * ...
        * Z = 52
* retourne la somme de toutes les valeurs trouvées sur les lignes

---

### Exemple

##### Entrée : 
```
ABcCaB
xyZpZq
abcdefABCDe
```

##### Algo

* ligne 1 : `ABcCaB`
    * on coupe en 2 : `ABc` et `CaB`
    * lettre commune : **B**
    * convertion en nombre : 28
* ligne 2 : `xyZpZq`
    * on coupe en 2 : `xyZ` et `pZq`
    * lettre commune : **Z**
    * convertion en nombre : 52
* ligne 3 : `abcdefABeCDA`
    * on coupe en 2 : `abcdef` et `ABeCDA`
    * lettre commune : **e**
    * convertion en nombre : 5

##### Sortie

* la fonction retourne la somme des nombres obtenus pour chaque ligne
    * 28 + 52 + 5 = **85**

---

### Consignes

* [ ] Écrivez la fonction décrite ci-dessus
* [ ] Appliquez cette fonction au fichier `data/items.txt`
    * [ ] Au préalable, chargez ce fichier dans une variable
    * [ ] Écrivez en commentaires le résultat que vous avez trouvé
* [ ] Écrivez une 2e fonction qui réalise le même travail que la première avec la restriction suivante. La convertion en nombre ne se fait que :
    * si la lettre commune est une MAJUCULE, sinon la ligne "vaut" 0
    * si la ligne contient au moins une fois la lettre "a" ou "A", sinon la ligne "vaut" 0
* [ ] Appliquez cette 2e fonction au fichier items.txt
    * [ ] Écrivez en commentaires le résultat que vous avez trouvé

Si l'on reprend l'exemple, en appliquant la 2e fonction, le résultat est **28** :

```
ABcCaB             -> 28 car B MAJUSCULE et la ligne contient au moins un "a"
xyZpZq             -> 0 car pas de a ni de A sur cette ligne
abcdefABCDe        -> 0 car la lettre commune "e" est une minuscule
```

---

## :arrow_forward: Exercice 2

### Objectif

Le but va être d'écrire une fonction qui : 

* prend en entrée une chaine de caractères
* pour chaque ligne, vérifie la validité de la ligne (voir exemple ci-dessous)
* retourne le nombre de lignes valides

### Exemple

```
1-2 a: abcdefgh
1-3 z: abcdef
2-4 x: xxxxxxx
```

Ce qui est avant les ":" représente la règle. Ce qui est après est la chaine sur laquelle on vérifie si la règle est respectée.

* ligne 1 : 
    * règle `1-2 a` : la chaine doit contenir entre 1 et 2 "a"
    * chaine `abcdefgh` contient 1 "a" donc est valide
* ligne 2 : 
    * règle `1-3 z` : la chaine doit contenir entre 1 et 3 "z"
    * chaine `abcdef` ne contient aucun "z" donc elle n'est pas valide
* ligne 3 : 
    * règle `2-4 x` : la chaine doit contenir entre 2 et 4 "x"
    * chaine `xxxxxxx` contient 7 "x" donc elle n'est pas valide


### Consignes

* [ ] Écrivez la fonction demandée ci-dessus
* [ ] Appliquez cette fonction au fichier `data/valid.txt`
    * [ ] Écrivez en commentaires le résultat que vous avez trouvé
* [ ] Écrivez une seconde fonction
    * qui repart du même principe que la première
    * compte les lignes valides uniquement si plusieurs lignes consécutives sont valides
    * c'est à dire qu'une ligne vaut 1 si :
        * elle est valide
        * la ligne précédente et/ou la ligne suivante est valide
    * une ligne invalide vaut 0
    * une ligne valide mais isolée vaut 0
* [ ] Appliquez cette 2e fonction au fichier `valid.txt`
    * [ ] Écrivez en commentaires le résultat que vous avez trouvé

Exemple pour la 2e fonction : 

```
1-2 a: a       
1-3 z: zzz     
1-4 t: tt      
3-4 x: ggggg   
1-2 b: b       
3-4 x: ggggg   
```

Le résultat attendu est **3** car : 

```
1-2 a: a               -> ligne valide avec voisine valide : 1
1-3 z: zzz             -> ligne valide avec voisine valide : 1
1-4 t: tt              -> ligne valide avec voisine valide : 1            
3-4 x: ggggg           -> ligne invalide                   : 0
1-2 b: b               -> ligne valide mais isolée         : 0
3-4 x: ggggg           -> ligne invalide                   : 0