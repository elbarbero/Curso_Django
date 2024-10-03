from django.shortcuts import render, HttpResponse

# html_home="""<h1>Mi Web Personal</h1>
# <ul>
#     <li><a href="/">Portada</a></li>
#     <li><a href="/about-me">Acerca de</a></li>
#     <li><a href="/porfolio">Porfolio</a></li>
#     <li><a href="/contact">Contacto</a></li>
# </ul>"""

# Create your views here.´
def home(request):
    return render(request=request, template_name="core/home.html")

def porfolio(request):
    return render(request=request, template_name="core/porfolio.html")

def contact(request):
    return render(request=request, template_name="core/contact.html")

def about(request):
    return render(request=request, template_name="core/about_me.html")

def test(request):
    html_response = "<h1>Mi web Personal</h1>"
    for i in range(10):
        html_response += "<h2>Portal</h2>"
    return HttpResponse(html_response)