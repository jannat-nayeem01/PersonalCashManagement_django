from rest_framework import serializers
from .models import *

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'user', 'description', 'amount', 'datetime', 'created_at']
        read_only_fields = ['created_at']