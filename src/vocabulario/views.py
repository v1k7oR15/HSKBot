from django.shortcuts import render

# Create your views here.
def base_view(request):
    context = {}
    return render(request, 'base.html', context)