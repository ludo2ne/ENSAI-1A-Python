from copy import copy

initial = [1, 2, "test", True, 4, 5]
second = initial
my_copy = copy(initial)

initial[0] = 42
initial[5] = "another"

print(initial)
print(second)
print(my_copy)


print("-" * 50)

remise_a_niveau = {
    "UE": "Informatique pour la data science",
    "module": "remise_a_niveau",
    "nb_eleve": 20,
    "eleves": ["Alice", "Benoit", "Camille"],
}

print(remise_a_niveau.keys())
remise_a_niveau["nb_eleve"] = 4
remise_a_niveau["annee"] = "2024-2025"

print(remise_a_niveau)
