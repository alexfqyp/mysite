from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator
from .models import Blog,BlogType

def blog_list(request):
    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list,10)  # 每页10条博客
    page_num = request.GET.get('page', 1)  # 获取页码参数 (GET请求)
    page_of_blogs = paginator.get_page(page_num)

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blog_list.html', context)

def blog_detail(request,blog_pk):
    context = {}
    blog = get_object_or_404(Blog,pk=blog_pk)
    context['previous_blog'] = Blog.objects.filter(create_time__gt = blog.create_time).last()
    context['next_blog'] = Blog.objects.filter(create_time__lt = blog.create_time).first()
    context['blog'] = blog
    return render_to_response('blog/blog_detail.html', context)

def blogs_with_type(request,blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blogs_with_type.html', context)