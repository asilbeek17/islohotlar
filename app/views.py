from django.shortcuts import render, redirect

from app.models import Project, Category, Contact


def index(request):
    product = Project.objects.all()
    category = Category.objects.all()
    context = {
        'product': product,
        'category': category
    }
    return render(request, 'index.html', context)


# def category(request):
#     product = Project.objects.all()
#     context = {
#         'project': product
#     }
#     return render(request, 'category.html', context)


def project(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project.html', context)


def sanoat_project(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project/sanoat_project.html', context)


def qishloq_project(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project/qishloq_project.html', context)


def xizmat_project(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project/xizmat_project.html', context)


def sort_1(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/0.5-1.html', context)


def sort_2(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/1-5.html', context)


def sort_3(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/5-10.html', context)


def sort_4(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/10-15.html', context)


def sort_5(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/15-20.html', context)


def sort_6(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/20-25.html', context)


def sort_7(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/25-30.html', context)


def sort_8(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/30+.html', context)


def contact_view(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        text = request.POST.get("text")

        c = Contact()
        c.first_name = first_name
        c.last_name = last_name
        c.email = email
        c.phone_number = phone_number
        c.text = text

        c.save()
        return redirect('contact')

    return render(request, 'contact.html')