from django.shortcuts import render
from .forms import StockSelectionForm
from .models import Stock  # Import the Stock model
from django.http import JsonResponse


def stock_selection(request):
    
    form = StockSelectionForm()

    if request.method == 'POST':
        form = StockSelectionForm(request.POST)
        if form.is_valid():
            selected_stock = form.cleaned_data['selected_stock']
            # Process the selected_stock, e.g., save it to the database or perform other actions
            return JsonResponse({'message': f'{selected_stock} Stock selected successfully'})

    return render(request, 'select_stock.html', {'form': form})
