# Travelling Salesman problem implemented using Genetic Algorithm
import random
import numpy as np

# Define the cities as (x, y) coordinates
cities = {
    "A": (0, 0),
    "B": (2, 4),
    "C": (5, 2),
    "D": (7, 8),
    "E": (1, 9),
}

# Function to calculate the total distance of a tour
def calculate_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        total_distance += np.linalg.norm(np.array(cities[city1]) - np.array(cities[city2]))
    return total_distance

# Function to generate an initial population
def generate_initial_population(num_individuals, cities):
    population = []
    city_names = list(cities.keys())
    for _ in range(num_individuals):
        random.shuffle(city_names)
        population.append(city_names.copy())
    return population

# Function to select parents for crossover using tournament selection
def select_parents(population, k):
    selected_parents = []
    for _ in range(k):
        tournament = random.sample(population, 5)  # Select 5 random individuals
        tournament.sort(key=lambda x: calculate_distance(x))  # Sort by distance
        selected_parents.append(tournament[0])  # Choose the best individual
    return selected_parents

# Function to perform crossover (Order Crossover)
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = parent1[start:end]  # Extract a subset from parent 1
    remaining = [city for city in parent2 if city not in child]  # Remaining cities from parent 2
    child.extend(remaining)
    return child

# Function to perform mutation (Swap Mutation)
def mutate(individual):
    idx1, idx2 = random.sample(range(len(individual)), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Genetic Algorithm
def genetic_algorithm(num_generations, population_size):
    population = generate_initial_population(population_size, cities)
    
    for generation in range(num_generations):
        population.sort(key=lambda x: calculate_distance(x))
        best_individual = population[0]
        print(f"Generation {generation}: Best Distance = {calculate_distance(best_individual)}, Tour = {best_individual}")
        
        new_population = [best_individual]  # Keep the best individual
        
        while len(new_population) < population_size:
            parents = select_parents(population, 5)
            parent1, parent2 = parents[0], parents[1]
            child = crossover(parent1, parent2)
            
            if random.random() < 0.1:  # Apply mutation with a small probability
                mutate(child)
                
            new_population.append(child)
            
        population = new_population

    print("Final Best Tour:", population[0])

# Run the Genetic Algorithm
genetic_algorithm(num_generations=50, population_size=50)
