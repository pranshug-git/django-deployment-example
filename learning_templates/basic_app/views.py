from django.shortcuts import render


def index(request):
    context_dict = {'text': "Hello World", 'number': 10}
    return render(request, 'basic_app/index.html', context= context_dict)


def other(request):
    return render(request, 'basic_app/other.html')


def relative(request):
    return render(request, 'basic_app/relative_url_template.html')
