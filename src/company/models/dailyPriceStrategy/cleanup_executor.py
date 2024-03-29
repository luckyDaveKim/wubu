from src.company.models.dailyPriceStrategy.strategy_executable import StrategyExecutable


class CleanupExecutor(StrategyExecutable):
    def get_strategy_name(self):
        return 'cleanup'

    def execute(self, df):
        fields_to_remove = ['code', 'diff', 'volume']

        return df.drop(fields_to_remove, axis=1)
