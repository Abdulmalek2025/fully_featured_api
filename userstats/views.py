from django.shortcuts import render
from rest_framework.views import APIView
import datetime
from expences.models import Expense
from incomes.models import Income
from rest_framework import status, response
# Create your views here.

class ExpenseSummaryStats(APIView):

    def get_amount_for_category(self,expence_list,category):
        expenses = expence_list.filter(category=category)
        amount = 0
        for expense in expenses:
            amount+=expense.amount

        return {'amount':str(amount)}


    def get_category(self,expense):
        return expense.category

    def get(self,request):
        todays_date = datetime.date.today()
        year_ago = todays_date-datetime.timedelta(days=30*12)
        expenses = Expense.objects.filter(owner=request.user,date__gte=year_ago,date__lte=todays_date)
        final = {}
        categories = list(set(map(self.get_category,expenses)))
        for expense in expenses:
            for category in categories:
                final[category] = self.get_amount_for_category(expenses,category)
        return response.Response({'category_data':final},status=status.HTTP_200_OK)

class IncomeSummaryStats(APIView):
    def get_amount_for_resource(self,income_list,resource):
        incomes = income_list.filter(resource=resource)
        amount = 0
        for income in incomes:
            amount+=income.amount
        return {'amount':str(amount)}

    def get_resource(self,incomes):
        return incomes.resource
    def get(self,request):
        todays_data = datetime.date.today()
        year_ago = todays_data-datetime.timedelta(days=30*12)

        incomes = Income.objects.filter(owner=request.user,date__gte=year_ago,date__lte=todays_data)
        resources = list(set(map(self.get_resource,incomes)))
        final = {}
        for income in incomes:
            for resource in resources:
                final[resource] = self.get_amount_for_resource(incomes,resource)
        return response.Response({'resource_data':final},status=status.HTTP_200_OK)
