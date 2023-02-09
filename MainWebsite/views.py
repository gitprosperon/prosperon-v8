from django.shortcuts import render
from Student.models import Location
from .forms import AddLocationForm, AddApartmentForm
from .models import BlogArticle


# Create your views here.
def home_page(request):
    return render(request, 'MainWebsite/index.html')


# Our Story Page
def our_stpry(request):
    return render(request, 'MainWebsite/our-story.html')

# Page to show product
def product_page(request):
    return render(request, 'MainWebsite/product.html')

# Page for pilot program
def pilot_program_page(request):
    return render(request, 'MainWebsite/pilot-program.html')

# Views for all blogs
def all_blogs(request):
    all_blogs = BlogArticle.objects.all()

    context = {
        'all_blogs': all_blogs[:3]
    }
    return render(request, 'MainWebsite/blog/all_blogs.html', context=context)


# Views for individual blog
def blog(request, id):
    cleaned_id = str(id)
    all_blogs = BlogArticle.objects.get(blog_id=cleaned_id)
    page_type = all_blogs.page_type
    print(page_type)

    context = {
        'all_blogs': all_blogs
    }
    return render(request, f'MainWebsite/blog/{page_type}.html', context=context)