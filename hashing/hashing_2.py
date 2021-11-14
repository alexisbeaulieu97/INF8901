# Fonction pour calculer l'emplacement
# de la valeur dans la table
def mod_hash(value, size):
    return value % size

# Initialisation de la taille de la table
table_size = 10

# Initialisation de la table
database = [None] * table_size

# Placement de la premiere valeur dans la table
value = 5
value_index = mod_hash(value, len(database))
database[value_index] = value
print(database) # [None, None, None, None, None, 5, None, None, None, None]

# Placement de la deuxieme valeur dans la table
value_2 = 15
value_2_index = mod_hash(value, len(database))
database[value_2_index] = value_2
print(database) # [None, None, None, None, None, 15, None, None, None, None]

# TODO ajouter le temps de hashing avec timeit