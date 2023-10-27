from django import forms
from .models import Stock  # Import the Stock model

class StockSelectionForm(forms.Form):
    # Retrieve unique stock names from the database
    stocks = Stock.objects.values_list('name', flat=True).distinct()
    
    # Create a list of choices from the unique names
    choices = [(stock, stock) for stock in stocks]
    
    selected_stock = forms.ChoiceField(choices=choices)
