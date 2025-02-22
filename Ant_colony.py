import numpy as np
import random

# Matrice des distances
distance_matrix = np.array([
    [0, 1, 1, 3, 4, 5, 6, 1, 7],
    [1, 0, 5, 4, 3, 6, 1, 9, 2],
    [2, 5, 0, 1, 6, 1, 9, 3, 7],
    [3, 4, 1, 0, 5, 9, 7, 2, 1],
    [4, 3, 6, 5, 0, 9, 1, 2, 1],
    [5, 6, 1, 9, 9, 0, 2, 1, 7],
    [6, 1, 9, 7, 1, 2, 0, 4, 5],
    [1, 9, 3, 2, 2, 1, 4, 0, 7],
    [7, 2, 7, 1, 1, 7, 5, 7, 0],
])

n_villes = distance_matrix.shape[0]
# Initialisation des phéromones : éviter la division par zéro pour la diagonale
pheromones = np.zeros_like(distance_matrix, dtype=float)
for i in range(n_villes):
    for j in range(n_villes):
        if i != j:
            pheromones[i, j] = 1 / distance_matrix[i, j]

# Paramètres
alpha = 1        # importance de la phéromone
beta = 2         # importance de la visibilité
rho = 0.5        # taux d'évaporation
n_fourmis = 4    # nombre de fourmis par itération
n_iterations = 100  # par exemple
Q = 1            # constante de dépôt

def choisir_ville(courante, non_visitees, pheromones, distance_matrix):
    # Calcul de la probabilité pour chaque ville non visitée
    numerateurs = []
    for j in non_visitees:
        tau = pheromones[courante, j] ** alpha
        eta = (1 / distance_matrix[courante, j]) ** beta
        numerateurs.append(tau * eta)
    somme = sum(numerateurs)
    probabilites = [num / somme for num in numerateurs]
    return random.choices(non_visitees, weights=probabilites)[0]

def construire_tour(depart, pheromones, distance_matrix):
    tour = [depart]
    non_visitees = list(range(n_villes))
    non_visitees.remove(depart)
    while non_visitees:
        prochaine = choisir_ville(tour[-1], non_visitees, pheromones, distance_matrix)
        tour.append(prochaine)
        non_visitees.remove(prochaine)
    return tour

def calculer_distance(tour, distance_matrix):
    distance = 0
    for i in range(len(tour)-1):
        distance += distance_matrix[tour[i], tour[i+1]]
    # On peut ajouter le retour à la ville de départ si besoin
    distance += distance_matrix[tour[-1], tour[0]]
    return distance

# Stocker la meilleure solution trouvée
meilleur_tour = None
meilleure_distance = float('inf')

for iteration in range(n_iterations):
    tours = []
    distances = []
    # Chaque fourmi construit un tour
    for k in range(n_fourmis):
        tour = construire_tour(depart=0, pheromones=pheromones, distance_matrix=distance_matrix)
        tours.append(tour)
        d = calculer_distance(tour, distance_matrix)
        distances.append(d)
        if d < meilleure_distance:
            meilleur_tour = tour
            meilleure_distance = d

    # Évaporation sur toutes les arêtes
    pheromones = (1 - rho) * pheromones

    # Dépôt de phéromones pour chaque tour
    for tour, d in zip(tours, distances):
        delta = Q / d
        for i in range(len(tour)-1):
            pheromones[tour[i], tour[i+1]] += delta
        # Ajout du dépôt pour le retour à la ville de départ (si nécessaire)
        pheromones[tour[-1], tour[0]] += delta

print("Meilleur tour trouvé :", meilleur_tour)
print("Distance :", meilleure_distance)
