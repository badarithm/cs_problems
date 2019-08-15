from __future__ import annotations
from typing import Tuple, List
from chapter_five.chromosome import Chromosome
from chapter_five.genetic_algorithm import GeneticAlgorithm
from random import randrange, random
from copy import deepcopy

# simple equation class solves equation 6x - x^2 + 4y - y^2
class SimpleEquation(Chromosome):
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def fitness(self) -> float:
        return 6 * self.x - self.x * self.x + 4 * self.y - self.y * self.y

    # static method
    @classmethod
    def random_instance(cls) -> SimpleEquation:
        return SimpleEquation(randrange(100), randrange(100))

    def crossover(self, other: SimpleEquation) -> Tuple[SimpleEquation, SimpleEquation]:
        child_one: SimpleEquation = deepcopy(self)
        child_two: SimpleEquation = deepcopy(other)

        child_one.y = other.y
        child_two.y = self.y
        return child_one, child_two

    def mutate(self) -> None:
        if random() > 0.5: # mutate x
            if random() > 0.5:
                self.x += 1
            else:
                self.x -= 1
        else : # oherwise mutate y, so x and y have equal chances for mutation
            if random() > 0.5:
                self.y += 1
            else:
                self.y -= 1

    def __str__(self) -> str:
        return f"X: {self.x} Y: {self.y} Fitness: {self.fitness()}"

# instead of __name__ == "__main__"
def test() -> None:
    initial_population: List[SimpleEquation] = [SimpleEquation.random_instance() for _ in range(20)]
    genetic_algorithm: GeneticAlgorithm[SimpleEquation] = GeneticAlgorithm(initial_population=initial_population, threshold=13.0, max_generations=100, mutation_chance=0.1, crossover_chance=0.7)
    result: SimpleEquation = genetic_algorithm.run()
    print(result)