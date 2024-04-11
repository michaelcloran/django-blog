from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
   queryset = Post.objects.filter(status=1)  #all()
   template_name = "blog/index.html"
   paginate_by = 6


def post_detail(request, slug):
   """ Display an individual: model:`blog.Post`

   **Context**

   ``post``
      an instance of :model:`blog.Post`.

   **Template:**
   :template: `blog/post_detail.html`
   """

   queryset = Post.objects.filter(status=1)  # all()
   post = get_object_or_404(queryset, slug=slug)

   return render(
      request,
      "blog/post_detail.html",
      {"post": post},
   )


def about_detail(request):
   queryset = About.objects.all().order_by('-updated_on').first()
   about = get_object_or_404(queryset, title=title)

   return render(
      request,
      "about/about_detail.html",
      {"about": about},
   )