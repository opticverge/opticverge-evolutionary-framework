from opticverge.core.enum.policy import Policy
from opticverge.core.log.logger import application_logger
from opticverge.core.solver.generic_ais import AIS
from opticverge.examples.machine_learning.regression.red_wine_quality.problem import RedWineQualityPredictionProblem
from opticverge.external.scikit.chromosome.regression.ensemble import GradientBoostingRegressorChromosome, \
    XGBRegressorChromosome
from opticverge.external.scikit.chromosome.regression.neighbor import KNeighborsRegressorChromosome
from opticverge.external.scikit.chromosome.regression.perceptron import MLPRegressorChromosome
from opticverge.external.scikit.enum.normaliser import Normaliser
from opticverge.external.scikit.enum.scoring_function import Scoring


def run():
    try:
        problem = RedWineQualityPredictionProblem(
            scoring_function=Scoring.MeanAbsoluteError,
            normaliser=Normaliser.RobustScaler,
            folds=3
        )

        """
        Regressor choices:
        - AdaBoostRegressorChromosome
        - DecisionTreeRegressorChromosome
        - GradientBoostingRegressorChromosome
        - KNeighborsRegressorChromosome
        - MLPRegressorChromosome
        - RandomForestRegressorChromosome
        - XGBRegressorChromosome
        """
        solver = AIS(
            chromosome=XGBRegressorChromosome(),
            problem=problem,
            population_size=20,
            epochs=-1,
            policies=[
                Policy.EnforceLimitedMutationAttempts,
                Policy.EnforceUniqueChromosome
            ],
            duration=None
        )

        best_chromosome = solver.run()

        problem.log_chromosome(best_chromosome, solver)

    except Exception as ex:
        application_logger.exception(msg="", exc_info=ex)


if __name__ == '__main__':
    run()
