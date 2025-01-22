from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
    chaim = ChaiVariety.objects.all()
    return render(request, 'all_chai.html', {'chaim': chaim})

def chai_detail(request, id):
    # chai = get_object_or_404(ChaiVariety, pk=id)
    chai = ChaiVariety.objects.get(id=id)
    return render(request, 'chai_detail.html', {'chai': chai})

def home(request):
    return render(request, 'website/index.html')