from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

def blog_list(request):
    blog_posts = Blog.objects.all().order_by('-created_at')  # or any ordering
    paginator = Paginator(blog_posts, 6)  # Show 6 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog.html', {'page_obj': page_obj})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blogDetails.html', {'blog': blog})

