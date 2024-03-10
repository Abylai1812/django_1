from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from post.models import Post

def posts(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "index.html", context)

def post_detail(request,post_id):
    return HttpResponse(f"detail: {post_id}")

def post_archive(request,year):
    if int(year)>2024 or int(year)<1995:
        return Http404
    return HttpResponse(f"archive for: {year}")

def get_post_handler(request):
    if request.POST:
        return HttpResponse("POST request")
    return HttpResponse("GET request")

def page404(request,exception):
    return HttpResponseNotFound("<h3> Page not Found!</h3>")