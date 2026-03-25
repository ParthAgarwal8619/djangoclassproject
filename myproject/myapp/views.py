from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemberForm()
    all_members = Member.objects.all
    return render(request,'home.html', {'form':form ,'all':all_members})


def about(request):
    return HttpResponse("This is about page")

def update_member(request, id):
    member = get_object_or_404(Member, id=id)
    
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = MemberForm(instance=member)
    
    return render(request,'update.html',{'form':form})

def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect('home')
    
    