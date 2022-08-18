from django.urls import path
from userstats.views import ExpenseSummaryStats, IncomeSummaryStats

urlpatterns = [
    path('expenses_category_data',ExpenseSummaryStats.as_view(),name='expense-category-summary'),
    path('income_resource_data',IncomeSummaryStats.as_view(),name='income-resource-summary')
]

