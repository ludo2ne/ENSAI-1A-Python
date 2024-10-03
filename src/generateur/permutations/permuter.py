import random
import string


def generate_random_mapping():
    # Liste des lettres minuscules de l'alphabet
    lowercase_letters = list(string.ascii_lowercase)

    # Mélanger les lettres pour obtenir un mapping aléatoire
    shuffled_lowercase = random.sample(lowercase_letters, len(lowercase_letters))

    # Créer le mapping pour les minuscules et ajouter les majuscules correspondantes
    mapping = {lower: shuffled for lower, shuffled in zip(lowercase_letters, shuffled_lowercase)}

    # Ajouter le mapping pour les majuscules en utilisant la même correspondance
    mapping.update(
        {
            lower.upper(): shuffled.upper()
            for lower, shuffled in zip(lowercase_letters, shuffled_lowercase)
        }
    )

    return mapping


def substitution_permutation(s, mapping, preserve_words):
    result = []

    # Découper la chaîne en lignes pour préserver les retours à la ligne
    lines = s.splitlines()

    for line in lines:
        # Découper chaque ligne en mots
        words = line.split()
        transformed_words = []

        for word in words:
            # Si le mot est dans la liste des mots à préserver, on le garde tel quel
            if word in preserve_words:
                transformed_words.append(word)
            else:
                # Sinon, on remplace chaque caractère du mot par son équivalent dans le mapping
                transformed_word = "".join([mapping.get(char, char) for char in word])
                transformed_words.append(transformed_word)

        # Reformater la ligne transformée et l'ajouter à la liste des résultats
        result.append(" ".join(transformed_words))

    # Rejoindre les lignes avec des retours à la ligne
    return "\n".join(result)


if __name__ == "__main__":

    from pathlib import Path

    # Générer un mapping aléatoire
    random_mapping = generate_random_mapping()

    # Import du fichier source
    folder_path = Path(__file__).resolve().parent
    text_input = open(folder_path / "input.txt", "r").read()

    # Exemple d'utilisation et génération du fichier de sortie
    result = substitution_permutation(
        text_input, random_mapping, preserve_words=["inc", "dec", "if"]
    )

    with open(folder_path / "output.txt", "w") as file:
        file.write(result)
