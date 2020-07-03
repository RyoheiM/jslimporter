from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Bunch, Details
from .forms import BunchForm
from django.utils import timezone


def bunchlist(request):
    ctx = {
        'bunches': Bunch.objects.all(),
    }
    return render(request, 'factors/bunchlist.html', ctx)


def bunchadd(request):
    if request.method == "POST":
        form = BunchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('bunchlist')
    else:
        form = BunchForm()
    return render(request, 'factors/bunchadd.html')

    # Create your views here.


def bunchdetail(request, pk):
    bunch = get_object_or_404(Bunch, pk=pk)
    return render(request, 'factors/bunchdetail.html', {'bunch': bunch})


def bunchedit(request, pk):
    bunch = get_object_or_404(Bunch, pk=pk)
    if request.method == "POST":
        form = BunchForm(request.POST, instance=bunch)
        if form.is_valid():
            bunch = form.save(commit=False)
            bunch.save()
            return redirect('bunchdetail', pk=bunch.pk)
    else:
        form = BunchForm(instance=bunch)
    return render(request, 'factors/bunchedit.html', {'form': form})
