from rest_framework import serializers
from expences.models import Expense
class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Expense
        fields = ['id','date','amount','description','category']