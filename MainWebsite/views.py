from django.shortcuts import render
from Student.models import Location
from .forms import AddLocationForm, AddApartmentForm
from .models import BlogArticle
from .forms import ContactForm


# Index Page
def home_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            post = request.POST
            name = post['name']
            email = post['email']
            message = post['message']
            form.name = name
            form.email = email
            form.message = message
            form.save()
    else:
        form = ContactForm(request.POST)

    context = {
        'form': form
    }

    return render(request, 'MainWebsite/index.html', context=context)


#
def testamonials(request):

    return render(request, 'MainWebsite/testamonials.html')


# Our Story Page
def our_stpry(request):
    return render(request, 'MainWebsite/our-story.html')


# Page to show product
def product_page(request):
    return render(request, 'MainWebsite/product.html')


# Page for pilot program
def pilot_program_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            post = request.POST
            name = post['name']
            email = post['email']
            message = post['message']
            form.name = name
            form.email = email
            form.message = message
            form.save()

    else:
        form = ContactForm(request.POST)

    context = {
        'form': form
    }
    return render(request, 'MainWebsite/pilot-program.html', context=context)


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
        'the_Blog': all_blogs
    }
    return render(request, f'MainWebsite/blog/{page_type}.html', context=context)


# Terms and conditions page
def terms_and_conditions(request):
    return render(request, 'MainWebsite/terms-and-conditions.html')


