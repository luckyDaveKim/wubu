from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models.company_info_model import CompanyInfoModel
from .models.daily_price_model import DailyPriceModel
from .serializers.company_info_serializer import CompanyInfoSerializer
from .serializers.daily_price_serializer import DailyPriceSerializer

class CompaniesAPI(APIView):
    def get(self, request):
        market_type = 'KOSPI'
        queryset = CompanyInfoModel.objects.filter(market_type=market_type)
        print(queryset)
        serializer = CompanyInfoSerializer(queryset, many=True)
        return Response(serializer.data)

class DailyPriceAPI(APIView):
    def get(self, request, code):
        queryset = DailyPriceModel.objects.filter(code=code).order_by('date')
        print(queryset)
        serializer = DailyPriceSerializer(queryset, many=True)
        return Response(serializer.data)


def product_list(request):
    company_infos = CompanyInfoModel.objects.all()
    return render(request, 'company/company_list.html', {'company_infos': company_infos})


def product_detail(request, pk):
    print(pk)
    company_info = CompanyInfoModel.objects.get(pk=pk)
    return render(request, 'company/company_detail.html', {'company_info': company_info})
