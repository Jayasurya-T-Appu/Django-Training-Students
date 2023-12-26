from django.shortcuts import render, HttpResponse
from .forms import UserForm
# Create your views here.
from .models import ImageTest, Author, Books
def createImage(request):

    if request.method == "GET":
        data = ImageTest.objects.all()
        if data.exists():
            context = {
                "images": data
            }
            return render(request, 'home.html', context)
        else:
            return render(request, 'home.html')
    elif request.method == "POST":
        image = request.FILES['image']
        ImageTest.objects.create(image=image)
        return render(request, 'home.html')


def formView(request):

    context = {}

    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

        form = UserForm()
    context['form'] = form

    return render(request, 'form.html',  context)

def relation(request):
    if request.method == "GET":
        return render(request, 'relation.html')
    elif request.method== "POST":
        author_name = request.POST.get("author")
        book_name = request.POST.get("book")
        author =Author(name= author_name)
        author.save()
        book = Books(name=book_name, author= author)
        book.save()

        return render(request, 'relation.html')