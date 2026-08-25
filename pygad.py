import random
import numpy as np


class GA:
    def __init__(
        self,
        num_generations,
        sol_per_pop,
        num_parents_mating,
        num_genes,
        fitness_func,
        gene_space=None,
        mutation_num_genes=1,
        save_best_solutions=False,
        on_generation=None,
        allow_duplicate_genes=True,
        **kwargs
    ):
        self.num_generations = num_generations
        self.sol_per_pop = sol_per_pop
        self.num_parents_mating = min(num_parents_mating, self.sol_per_pop)
        self.num_genes = num_genes
        self.fitness_func = fitness_func
        self.gene_space = gene_space
        self.mutation_num_genes = max(1, min(mutation_num_genes, num_genes))
        self.save_best_solutions = save_best_solutions
        self.on_generation = on_generation
        self.allow_duplicate_genes = allow_duplicate_genes

        self.population = None
        self.best_solutions = []

    # =========================
    # GENE SAMPLING
    # =========================

    def _get_gene_space(self, idx):
        if self.gene_space is None:
            return None
        if isinstance(self.gene_space, list) and len(self.gene_space) == self.num_genes:
            return self.gene_space[idx]
        return self.gene_space

    def _sample_gene(self, idx, used_values=None):
        g = self._get_gene_space(idx)

        if g is None:
            val = random.uniform(0, 1)
        elif isinstance(g, dict):
            val = random.uniform(g.get("low", 0), g.get("high", 1))
        elif isinstance(g, (list, tuple)):
            if len(g) == 0:
                val = 0
            else:
                val = random.choice(g)
        else:
            val = g

        # enforce uniqueness
        if not self.allow_duplicate_genes and used_values is not None:
            if isinstance(g, (list, tuple)):
                available = [x for x in g if x not in used_values]
                if available:
                    val = random.choice(available)

        return val

    def _random_solution(self):
        sol = []
        used = set()

        for i in range(self.num_genes):
            gene = self._sample_gene(i, used)
            sol.append(gene)
            if not self.allow_duplicate_genes:
                used.add(gene)

        return np.array(sol, dtype=float)

    # =========================
    # FITNESS
    # =========================

    def _fitness(self, sol, idx):
        return self.fitness_func(self, sol, idx)

    # =========================
    # GA CORE
    # =========================

    def run(self):
        # init population
        self.population = np.array(
            [self._random_solution() for _ in range(self.sol_per_pop)]
        )

        for gen in range(self.num_generations):
            fitness_vals = np.array(
                [self._fitness(sol, i) for i, sol in enumerate(self.population)]
            )

            # sort descending
            idxs = np.argsort(-fitness_vals)
            self.population = self.population[idxs]
            fitness_vals = fitness_vals[idxs]

            best_sol = self.population[0].copy()

            if self.save_best_solutions:
                self.best_solutions.append(best_sol)

            if self.on_generation:
                if self.on_generation(self) == "stop":
                    break

            parents = self.population[:self.num_parents_mating]

            new_pop = []

            # elitism
            for i in range(min(2, len(parents))):
                new_pop.append(parents[i].copy())

            # generate
            while len(new_pop) < self.sol_per_pop:
                if len(parents) >= 2:
                    p1, p2 = parents[np.random.choice(len(parents), 2, replace=False)]
                else:
                    p1 = p2 = parents[0]

                # crossover
                if self.num_genes > 1:
                    cut = random.randint(1, self.num_genes - 1)
                    child = np.concatenate([p1[:cut], p2[cut:]])
                else:
                    child = p1.copy()

                # mutation
                used = set(child.tolist()) if not self.allow_duplicate_genes else None

                for _ in range(self.mutation_num_genes):
                    idx = random.randint(0, self.num_genes - 1)
                    new_val = self._sample_gene(idx, used)
                    child[idx] = new_val

                    if not self.allow_duplicate_genes:
                        used.add(new_val)

                new_pop.append(child)

            self.population = np.array(new_pop)

    # =========================
    # BEST SOLUTION
    # =========================

    def best_solution(self):
        fitness_vals = np.array(
            [self._fitness(sol, i) for i, sol in enumerate(self.population)]
        )
        idx = np.argmax(fitness_vals)
        return self.population[idx].copy(), fitness_vals[idx], idx