
# router = APIRouter(prefix="/api/analysis")

# @router.get("/")
# async def get_companies():
#     condition = CompanyInfoFilterCondition.builder().set_market_type('KOSPI').build()
#
#     session = Session()
#     # TODO : condition 사용하기
#     # return session.query(CompanyInfo).filter(*condition.get_filter()).order_by("company").all()
#
#     # filter_data = {'poster_id': poster_id, 'referenced_politician_id': referenced_politician_id, 'referenced_bill_id': referenced_bill_id}
#     # filter_data = {key: value for (key, value) in filter_data.items() if value}
#     # posts = SocialPost.query.filter_by(**filter_data).order_by(SocialPost.id.desc()).all()
#
#     return session.query(CompanyInfo).filter(CompanyInfo.market_type == 'KOSPI').order_by("company").all()



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
