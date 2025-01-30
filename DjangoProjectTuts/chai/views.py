from django.shortcuts import render
from .models import ChaiVariety, StoreModel
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

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

def ChaiStore(request):
    my_store = None 
    
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            my_varieties = form.cleaned_data['variety']
            my_store = StoreModel.objects.filter(variety=my_varieties)
    else:
        form = ChaiVarietyForm()

    return render(request, 'chai_store.html', {'mystore': my_store, 'form': form})
