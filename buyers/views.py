from django.shortcuts import render, get_object_or_404, redirect

from .models import Buyer
from .forms import BuyerForm


def buyer_list(request):
    buyers = Buyer.objects.all()
    return render(request, 'buyers/buyer_list.html', {'buyers': buyers})


def buyer_detail(request, pk):
    buyer = get_object_or_404(Buyer, pk=pk)
    return render(request, 'buyers/buyer_detail.html', {'buyer': buyer})


def buyer_create(request):
    if request.method == "POST":
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buyer_list')
    else:
        form = BuyerForm()
    return render(request, 'buyers/buyer_form.html', {'form': form})


def buyer_update(request, pk):
    buyer = get_object_or_404(Buyer, pk=pk)
    if request.method == "POST":
        form = BuyerForm(request.POST, instance=buyer)
        if form.is_valid():
            form.save()
            return redirect('buyer_detail', pk=buyer.pk)
    else:
        form = BuyerForm(instance=buyer)
    return render(request, 'buyers/buyer_form.html',
                  {'form': form, 'buyer': buyer})


def buyer_delete(request, pk):
    buyer = get_object_or_404(Buyer, pk=pk)
    if request.method == "POST":
        buyer.delete()
        return redirect('buyer_list')
    return render(request, 'buyers/buyer_confirm_delete.html',
                  {'buyer': buyer})
