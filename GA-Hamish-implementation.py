import string
import random
from random import shuffle

# Identify test cases which have the highest coverage

# Input text file
with open('C:/Users/theha/OneDrive/Documents/repos/CS547/newbigfaultmatrix.txt') as f: lines = f.readlines()

matrix = lines

# Constants
random.seed(150) 
pop_size=50
crossover_rate = 0.75
mutation_rate = 0.005
n_iterations = 1000

# Processes input into usable state (Comma separated list)
def process_input(input:list):
    for i in range(len(input)):
        # Delimiting string by commas
        length = len(input[i])-1
        input[i] = (input[i][0:length]).split(',')
    return input


# Finds smallest test set which maximises number of faults
def size_fitness(suite:list):
    fitness = 0
    return fitness

# Finds the test set which exectues in the shortest amount of time
def time_fitness(suite:list):
    fitness = 0
    return fitness


# Generate random configuration of test case ordering
def gen_individual(matrix:list):
    test_set = random.sample(matrix, len(matrix))
    return test_set

# Generates a population of individuals
def gen_population(matrix:list):
    population = []
    for i in range(pop_size):
        individual = gen_individual(matrix)
        population.append([individual,0])
        #print("Individual: ", i, [individual,0])
    return population

def eval_population(population:list):
    for i in range(len(population)):
        #print("Iteration:", i)
        population[i][1] = fitness(population[i][0])
        #print("Individual: ",population[i][0])
    return population

def fittest_individual(population:list):
    max_value = max(population, key=lambda x: x[1])
    return max_value
    
def find_top_50(population:list):
    top_50 = []
    for i in range(int(len(population)/2)):
        top_50.append(fittest_individual(population))
        # remove old best from array 
        population.pop(population.index(fittest_individual(population)))
    return top_50

# One-point crossover
def crossover(parent1, parent2):
    ind1, _ = parent1
    ind2, _ = parent2
    
    # Choose a random crossover point
    crossover_point = random.randint(1, len(ind1) - 1)
    
    # Generate children by swapping segments at the crossover point
    child1 = ind1[:crossover_point] + ind2[crossover_point:]
    child2 = ind2[:crossover_point] + ind1[crossover_point:]
    
    # Return children with fitness initialized to 0
    return [child1, 0], [child2, 0]

def select_and_generate_new_population(population):
    child_pop = []
    selected_pop = find_top_50(population)
    for i in range(0,pop_size-1,2):
        parent_a = selected_pop[random.randint(0,len(selected_pop)-1)] 
        parent_b = selected_pop[random.randint(0,len(selected_pop)-1)]
        child_a , child_b = crossover(parent_a, parent_b)
        child_pop.append(child_a)
        child_pop.append(child_b)
    return child_pop

def mutate(population):
    for individual in population:
        individual_list = list(individual[0])
        
        for i in range(len(individual_list)):
            if random.uniform(0, 1) < mutation_rate:
                swap = random.randint(0,len(individual_list)-1)
                individual_list[i], individual_list[swap] = individual_list[swap],individual_list[i]

    return population

# Main GA loop
def genetic_algorithm():
    proc_matrix = process_input(matrix) # Process the input
    population = gen_population(proc_matrix) # Generate population from processed input
    scored_pop = eval_population(population)
    i = 0
    print("Generation",i)
    print(fittest_individual(scored_pop))
    for i in range(n_iterations):
        i += 1
        new_pop = []
        new_pop = select_and_generate_new_population(scored_pop)
        mutated_pop = mutate(new_pop)
        pop = mutated_pop
        scored_pop = eval_population(pop)
        print("Generation",i)
        print("Fittest individual", fittest_individual(scored_pop)[0][1][0], "APFD value:",fittest_individual(scored_pop)[1] )

genetic_algorithm()