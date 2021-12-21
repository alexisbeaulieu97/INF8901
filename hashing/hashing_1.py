# Fonction pour calculer l'emplacement
# de la valeur dans la table
def mod_hash(value, size):
    return value % size


# Initialisation de la taille de la table
table_size = 10

# Initialisation de la table
database = [None] * table_size

# Initialisation de la valeur a mettre dans la base de donnees
value = 5

# Recuperation de l'indice dans la table
value_index = mod_hash(value, len(database))

# Placer la valeur au bon endroit dans la table
database[value_index] = value
print(database)  # [None, None, None, None, None, 5, None, None, None, None]
