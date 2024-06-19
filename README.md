# Genetic Algorithm using Python
Create a generic program whose population size = 50 (individuals), crossover-rate = 0.7 and mutation rate = (0.001). 

Each individual within the population was made up of binary bits of 1s and 0s and was 10 indexes long. Utilizing functions: randomGenome, makePopulation, fitness, evaluateFitness, selectPair, crossover, mutate and a supporting function of replacePopulation, the program ran until 30 generations were created or a best fitness score = 10.0 (i.e individual containing ten 1s was seen) was achieve, which ever one came first.

# How to run
1. Clone repo via cmdline
2. Navigate to cloned folder path
3. Type [python genetic_solution.py]

# Alter running without crossover element
1. Set runGA(50, 0.0, 0.001)

# Alter running with crossover element
1. Set runGA(50, 0.7, 0.001)
