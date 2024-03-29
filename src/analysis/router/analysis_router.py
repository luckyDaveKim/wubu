from typing import List, Optional

from fastapi import APIRouter
from fastapi.params import Query

from src.analysis.service import analysis_service
from src.company.model.company_info_filter_condition import CompanyInfoFilterCondition
from src.company.model.dailyPriceStrategy import StrategyExecutorFactory
from src.company.model.daily_price import DailyPrice
from src.company.model.daily_price_filter_condition import DailyPriceFilterCondition
from src.company.service import company_service
from src.rule.model.rule_executor import RuleExecutor

router = APIRouter()


@router.post("/api/analysis/rule/{rule_id}")
async def analysis_companies(rule_id: int,
                             company_code: Optional[str] = Query(None), company_codes: Optional[List[str]] = Query([]),
                             start_date: Optional[str] = Query(None), end_date: Optional[str] = Query(None)):
    condition = (CompanyInfoFilterCondition.builder()
                 .set_code(company_code)
                 .set_codes(company_codes)
                 .build())
    companies = await company_service.get_companies(condition)

    for company in companies:
        condition = (DailyPriceFilterCondition
                     .builder()
                     .set_code(company.code)
                     .set_start_date(start_date)
                     .set_end_date(end_date)
                     .build())

        daily_price_list = await company_service.get_company_daily_prices(condition)
        dataframe = DailyPrice.convert_to_dataframe(daily_price_list)
        calculated_dataframe = StrategyExecutorFactory(dataframe).execute_all(['bollingerBand'])
        await analysis_service.analysis_companies(rule_id, company.code, calculated_dataframe)

    return True

    # def get(self, request):
    #     condition = (MatchedRulesFilterCondition
    #                  .builder()
    #                  .set_code(request.GET.get('code', None))
    #                  .set_analysis_date(request.GET.get('analysisDate', None))
    #                  .set_start_analysis_date(request.GET.get('startAnalysisDate', None))
    #                  .set_end_analysis_date(request.GET.get('endAnalysisDate', None))
    #                  .build())
    #
    #
    #     # e = MatchedRulesModel()
    #     # e.code = '131313'
    #     # e.rules = 'good'
    #     # e.save()
    #
    #     MatchedRulesModel(code='121211', rules='hoho3323').save()
    #     # MatchedRulesModel.objects.create(code='121212', rules='hoho4')
    #
    #     # model = MatchedRulesModel(code='123121', rules='123123')
    #     # model.save()
    #     # MatchedRulesModel.objects.create(code='121213', rules='hoho')
    #     # MatchedRulesModel(code='123121', analysis_date=datetime.now(), rules="{'myrule': {'a': 'b'}}").save()
    #     queryset = MatchedRulesModel.objects.filter(*condition.get_filter())
    #     # queryset = MatchedRulesModel.objects.filter(*condition.get_filter()).order_by('code', '-analysis_date')
    #     # queryset = MatchedRulesModel.objects()
    #     # df = read_frame(queryset)
    #     # json_data = json.loads(df.to_json(orient='records'))
    #     # return Response(json_data)
    #     for person in queryset:
    #         print(person.code)
    #
    #     return Response(True)
    #
    # def post(self, request):
    #     target_date_text = request.GET.get('targetDate', datetime.now().strftime("%Y-%m-%d"))
    #     res = AnalysisService.analysis(target_date_text)
    #
    #     return Response(res)
