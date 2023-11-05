from django import forms
from .models import Stock  # Import the Stock model

class StockSelectionForm(forms.Form):

    selected_stock = forms.ChoiceField(choices=())

    def __init__(self,*args,**kwargs):
        super(StockSelectionForm,self).__init__(*args, **kwargs)
    # Retrieve unique stock names from the database
        stocks = Stock.objects.values_list('name',flat=True)
    # stocks = Stock.objects.values_list('name', flat=True).distinct()
    
    # Create a list of choices from the unique names
        self.fields['selected_stock'].choices = [(stock, stock) for stock in stocks]
