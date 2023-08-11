from django.shortcuts import render, redirect

from app.models import Project, CategoryUz, Contact, CategoryRu, CategoryEN


def index(request):
    product = Project.objects.all()
    category = CategoryUz.objects.all()
    context = {
        'product': product,
        'category': category
    }
    return render(request, 'index/index_uz.html', context)


def index_ru(request):
    product = Project.objects.all()
    category = CategoryRu.objects.all()
    context = {
        'product': product,
        'category': category
    }
    return render(request, 'index/index_ru.html', context)


def index_en(request):
    product = Project.objects.all()
    category = CategoryEN.objects.all()
    context = {
        'product': product,
        'category': category
    }
    return render(request, 'index/index_en.html', context)


# def category(request):
#     product = Project.objects.all()
#     context = {
#         'project': product
#     }
#     return render(request, 'category.html', context)


# ----------------------------------------------------------------------------------


def project_uz(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'loyihalar/project_uz.html', context)


def project_ru(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'loyihalar/project_ru.html', context)


def project_en(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'loyihalar/project_en.html', context)


# ---------------------------------------------------------------------------------------------


def sanoat_project_uz(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project/uz/sanoat_project.html', context)


def qishloq_project_uz(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project/uz/qishloq_project.html', context)


def xizmat_project_uz(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project/uz/xizmat_project.html', context)


# -------------------------------------------------------------------------------------------------------


def sanoat_project_ru(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project/ru/sanoat_project.html', context)


def qishloq_project_ru(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project/ru/qishloq_project.html', context)


def xizmat_project_ru(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project/ru/xizmat_project.html', context)


#-------------------------------------------------------------------------------------------------------


def sanoat_project_en(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project/en/sanoat_project.html', context)


def qishloq_project_en(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project/en/qishloq_project.html', context)


def xizmat_project_en(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project/en/xizmat_project.html', context)


# -------------------------------------------------------------------------------------------------------


def sort_1_uz(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/uz/0.5-1.html', context)


def sort_2_uz(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/uz/1-5.html', context)


def sort_3_uz(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/uz/5-10.html', context)


def sort_4_uz(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/uz/10-15.html', context)


def sort_5_uz(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/uz/15-20.html', context)


def sort_6_uz(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/uz/20-25.html', context)


def sort_7_uz(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/uz/25-30.html', context)


def sort_8_uz(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/uz/30+.html', context)


# --------------------------------------------------------------------------------

def sort_1_ru(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/ru/0.5-1.html', context)


def sort_2_ru(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/ru/1-5.html', context)


def sort_3_ru(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/ru/5-10.html', context)


def sort_4_ru(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/ru/10-15.html', context)


def sort_5_ru(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/ru/15-20.html', context)


def sort_6_ru(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/ru/20-25.html', context)


def sort_7_ru(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/ru/25-30.html', context)


def sort_8_ru(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/ru/30+.html', context)


# --------------------------------------------------------------------------------


def sort_1_en(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/en/0.5-1.html', context)


def sort_2_en(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/en/1-5.html', context)


def sort_3_en(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/en/5-10.html', context)


def sort_4_en(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/en/10-15.html', context)


def sort_5_en(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/en/15-20.html', context)


def sort_6_en(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/en/20-25.html', context)


def sort_7_en(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/en/25-30.html', context)


def sort_8_en(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'price_sort/en/30+.html', context)


# --------------------------------------------------------------------------------


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