def jour_semaine(jour, heure, minute) -> bool:
    liste_jour_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    return jour in liste_jour_semaine


def hors_heures_travail(jour, heure, minute) -> bool:
    if jour in ["Samedi", "Dimanche"]:
        return True
    elif heure < 8 or heure >= 18:
        return True
    else:
        return False


def vendredi_apres_18_30(jour, heure, minute) -> bool:
    if jour == "Vendredi":
        if (heure == 18 and minute >= 30) or heure > 18:
            return True
    return False


def pause_dej(jour, heure, minute) -> bool:
    if (heure == 12 and minute >= 30) or (heure == 13 and minute <= 45):
        return True
    return False


def jeudi_ou_15_18(jour, heure, minute):
    if jour == "Jeudi":
        return True
    elif 15 <= heure < 18:
        return True
    elif heure == 18 and minute <= 15:
        return True
    return False


if __name__ == "__main__":
    j = "Dimanche"
    h = 18
    m = 5

    # Appel des fonctions
    print(jour_semaine(j, h, m))
    print(jeudi_ou_15_18(j, h, m))
