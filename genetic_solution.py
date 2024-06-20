# Python Lib Imports
import random


# Class declaration
class RouletteWheelSelection():


    def __init__(self):


        # List to store fitness values for each individual or genome
        self.fitness_totals = list()


        # Crossoverrate
        self.cross_rate = 0.0


        # Mutation rate
        self.mut_rate = 0.0


    # Func: returns random genome (bit string) of a given length
    # Genome: individual
    def randomGenome(self, length):


        # Generate genome of length 10 using 0 and 1 digits
        # E.g. [1,1,0,0,1,0,1,1,0,0]
        individual = [random.randint(0,1) for num in range(length)]


        # Return genome 10 bits long
        return individual
   
    # Func: returns a new randomly created population of the specified size, represented as a list of genomes of the specified length
    def makePopulation(self, size, length):


        # List to store randomly created population
        population = list()


        # Create no.of individuals for pop based on size param
        for i in range(size):


            # Using the length param, create random individuals using binary bits (1s and 0s)
            for j in range(length):


                # Call func to generate randomGenome / individual
                individual = self.randomGenome(length)


            population.append(individual)
       
        return population
   


    # Func: returns the fitness value of a genome
    def fitness(self, genome):


        # Calculate the fitness based on f(x) = number of ones in x, where x is a genome of length 10 (i.e. the sum of the genome)
        return sum(genome)
   
    # Func: returns a pair of values: the average fitness of the population as a whole and the fitness of the best individual in the population
    def evaluateFitness(self, population):


        self.fitness_totals.clear()


        pop = list()


        for individual in population:


            # Call fitness func to get fitness value for each individual of population
            fitness_val = self.fitness(individual)


            # Append value to population
            pop.append([individual, fitness_val])


            # Add calc fitness val to list
            self.fitness_totals.append(fitness_val)


        # Tally total fitness_totals then calc the avg
        total_fit = sum(self.fitness_totals)
        total_individuals = len(population)
        avg_fit = float("{:.2f}".format(total_fit / total_individuals))


        # Find the highest fitness value in list (i.e. the best individual from population fitness val)
        best_fit = float("{:.2f}".format(max(self.fitness_totals)))


        return [avg_fit, best_fit, pop]
   


    # Func: selects and returns two genomes from the given population using fitness-proportionate selection
    def selectPair(self, population):


        # Tally total fitness_totals
        total = sum(self.fitness_totals)


        # Calculate the probability for each fitness value and store as list
        probabilities = [fits / total for fits in self.fitness_totals]


        # Use roulette-wheel sampling selection
        # Choose randomly using the random.choice func
        selection = random.choices(
            range(len(population)), # 1-49 possibilities
            weights=probabilities, # using probability list as a weighted measure
            k=2 # return the k-size list of population elements chosen
        )


        # Return two genomes from population based on roulette-wheel sampling selection
        return population[selection[0]][0], population[selection[1]][0]
       


    # Func: returns two new genomes produced by crossing over the given genomes from the selectPair func at a random crossover point.
    def crossover(self, genome1, genome2):


        # List newly created offspring
        crossed_list = list()


        # Perform crossover if and only if random num generated (betwen 0 and 1) is less than 0.7 or whatever the rate is
        if random.random() <= self.cross_rate:


            # Select random crossover point between 1 and the length of the individual (10) - 1. The minus one is to prevent the crossover point from being at the end of the genome
            cross_point = random.randint(1, len(genome1) - 1)


            # Perform crossover procedure by taking the merging the 1st part of genome1 (beginning up until the cross point) with the later part of genome2 (from cross point to the end) - using the slicing methodology
            off_spring_1 = genome1[:cross_point] + genome2[cross_point:]
            # Perform crossover procedure by taking the merging the 1st part of genome2 (beginning up until the cross point) with the later part of genome1 (from cross point to the end) - using the slicing methodology
            off_spring_2 = genome2[:cross_point] + genome1[cross_point:]


            crossed_list.extend([off_spring_1, off_spring_2])


        else:


            # Else assign original parents individuals as the new offspring
            off_spring_1 = genome1
            off_spring_2 = genome2


            # Add offspring to cross_list
            crossed_list.extend([off_spring_1, off_spring_2])
       
        return crossed_list
   
    # Func: returns a new mutated version of the given genome.
    def mutate(self, genome, mutationRate):


        # Store mutated individuals
        mutated_list = list()


        for individual in genome:


            # For the length of the individual
            for i in range(len(individual)):


                # Check if random num generation is < 0.001, is so switch genome value from 1 to 0 or 0 to 1 at the index position of genome in which the condition occurs
                if random.random() < mutationRate:
                   
                    # Switch 1 to 0 and 0 to 1 => 1 - int(individual[i])
                    individual[i] = 1 - int(individual[i])
           
            mutated_list.append(individual)


        return mutated_list
   


    # Func: replace old population with new population based on fitness score
    def replacePopulation(self, generation, population):


        # Sort population to have lowest fitness scores first
        sorted_pop = sorted(population, key= lambda x:x[1])


        # For the length of the new generation, do the replacement
        for i in range(len(generation)):


            # If new generation individual's fitness > population individual's fitness
            if generation[i][1] > sorted_pop[i][1]:


                # Assign new generation individual fitness to replace population individual's fitness
                population[i][1] = generation[i][1]


                # Assign new generation individual to replace population individual
                population[i][1] = generation[i][1]


        return sorted_pop


def runGA(populationSize, crossoverRate, mutationRate):


    # Solution found
    found = False


    # Genome length
    genome_len = 10


    # Generation initialization
    generation = 0


    # Create obj of class
    wheelie = RouletteWheelSelection()


    print(f"Population size: {populationSize}\n")
    print(f"Genome length: {genome_len}\n")


    # Assign cross-over rate
    wheelie.cross_rate = crossoverRate


    # Assign mutation rate
    wheelie.mut_rate = mutationRate


    # Create initial population
    initial_population = wheelie.makePopulation(populationSize, length=genome_len)


    # Get initial population avg and best fitness scores
    avg, best, pop = wheelie.evaluateFitness(initial_population)


    # Output results
    print(f"Generation {generation}: Average fitness {avg}, best fitness {best}\n")


    while not found and generation < 29:

        # If best fitness score == 10 then individual == [1,1,1,1,1,1,1,1,1,1]
        if best == 10.0:


            print("Solution found!!!")
            found = True
            break


        else:


            # Make selection of parents
            gn1, gn2 = wheelie.selectPair(pop)


            # Perform crossover
            cross_genomes = wheelie.crossover(gn1, gn2)


            # Perform mutation
            muted_genomes = wheelie.mutate(cross_genomes, wheelie.mut_rate)


            # New generation
            new_generation = list()


            # Add new individual (muted) to new generation
            for mute in muted_genomes:
                new_generation.append(mute)


            # Get new gen population avg and best fitness scores
            avg_fit, best_fit, pop = wheelie.evaluateFitness(new_generation)


            # Perform Replacement
            updated_population = wheelie.replacePopulation(new_generation, pop)


            # Assigned updated population to pop
            pop = updated_population


            # Assign best_fit value to best to check if solution has been found
            best = best_fit


            # Increment generation
            generation +=1


            # Output results
            print(f"Generation {generation}: Average fitness {avg_fit}, best fitness {best}\n")
           


if __name__ == '__main__':
   
    print("Mutation with crossover results:\n ")
    runGA(50, 0.7, 0.001)
