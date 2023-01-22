from django.http import JsonResponse
from django.shortcuts import render
from .models import Like_Dislike_count


def home(request):
    count = Like_Dislike_count.objects.get(pk = 1)
    return render(request,'like_dislike_app/home.html',{'like_count' : count.like_count, 'dislike_count' : count.dislike_count})



def like(request):
    count = Like_Dislike_count.objects.get(pk = 1)
    
    if request.method == "POST":
        count.like_count = count.like_count + 1
        count.save()
    
    return JsonResponse({'like_count' : count.like_count})
    


def dislike(request):
    count = Like_Dislike_count.objects.get(pk = 1)

    if request.method == "POST":
        count.dislike_count = count.dislike_count + 1
        count.save()
    
    return JsonResponse({'dislike_count' : count.dislike_count})
    

    