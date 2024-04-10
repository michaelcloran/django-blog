from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

def post_detail(request, slug):
   """ Display an individual: model:`blog.Post`

   **Context**

   ``post``
      an instance of :model:`blog.Post`.

   **Template:**
   :template: `blog/post_detail.html`
   """

   queryset = Post.objects.all()  # filter(status=1)
   post = get_object_or_404(queryset, slug=slug)

   return render(
      request,
      "blog/post_detail.html",
      {"post": post},
   )

# Create your views here.
class PostList(generic.ListView):
   queryset = Post.objects.all()
   template_name = "blog/index.html"
   paginate_by = 6
