from src.analysis.model.analysis import Analysis, RuleInfo
from src.rule.model.rule_executor import RuleExecutor


async def analysis_companies(rule_id: int, company_code: str, dataframe):
    is_matched_rule: bool = RuleExecutor().execute(dataframe)

    rule_info = RuleInfo(rule_id=rule_id, version=1)
    return await Analysis(code=company_code, rule_info=rule_info, is_matched_rule=is_matched_rule).insert()
