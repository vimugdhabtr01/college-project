import random
import string
import json
import logging
import urllib2,urllib
import httplib2
import pdfkit
from oauth2client import client
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.django_orm import Storage
from apiclient.discovery import build

from django.views.generic.base import View
from django.template import Template,Context
from django.shortcuts import render,render_to_response,redirect
from django.template import RequestContext,loader
from django.contrib.auth.models import User
from django.http import Http404,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from .models import ComposersProfile,ForgotPasswordUsers,FlowModel,CredentialsModel
from .forms import LoginForm,ComposerForm,ForgotPasswordForm,ResetPasswordForm


def loginwithgoogle(request):
    flow = OAuth2WebServerFlow(client_id='660478359243-nmv03t1i5pr2p1l1its676503gghvje0.apps.googleusercontent.com',client_secret='MqMbvkQ964_E_4b8eb0U6pAN',scope='https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile https://www.google.com/m8/feeds/', redirect_uri='http://localhost:8000/loginwithgoogle/google')
    auth_uri = flow.step1_get_authorize_url()
    return redirect(auth_uri)


def credentials(request):
    flow = OAuth2WebServerFlow(client_id='660478359243-nmv03t1i5pr2p1l1its676503gghvje0.apps.googleusercontent.com',client_secret='MqMbvkQ964_E_4b8eb0U6pAN',scope='https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile https://www.google.com/m8/feeds/', redirect_uri='http://localhost:8000/loginwithgoogle/google')
    code = request.GET.get('code')
    if code:
        credentials = flow.step2_exchange(code)
        access_token = credentials.access_token
        userinfo_url = 'https://www.googleapis.com/oauth2/v1/userinfo'
        query_string = urllib.urlencode({'access_token': access_token})
        resp = urllib2.urlopen("%s?%s" % (userinfo_url, query_string))
        data = json.loads(resp.read())
        print data
        return HttpResponse(json.dumps(data))
    elif error:
        return HttpResponse("error")


def home_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password= password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/composers_profile/')
                password_error = "Password is in valid."
                return render_to_response('composers_profile/home_page.html', {'form':form,'password_error':password_error}, context_instance= RequestContext(request))
    else:
        if request.user.is_authenticated():
            return redirect('/composers_profile/')
        form = LoginForm()

    return render_to_response('composers_profile/home_page.html', {'form': form}, context_instance=RequestContext(request))


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def forgotpassword(request):
    if request.user.is_authenticated():
        return redirect("/composers_profile/")
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username = form.cleaned_data["username"])
            token = token_generator()
            ForgotPasswordUsers.objects.create(
                forgotpassworduser = user,
                token = token,
            )
            email_body = "Hey,%s please click on the given link to reset your password. You can change your password only once by clicking on given link. http://127.0.0.1:8000/resetpassword/%s" % (user.first_name, token)
            send_mail('Regarding Password Change',email_body,'vimugdhabtr01@gmail.com',[ user.username ])
            msg = "Please check your email for Reset Password."
            return render_to_response('composers_profile/forgotpassword.html', {'form': form, 'msg': msg}, context_instance=RequestContext(request))
    else:
        form = ForgotPasswordForm()
    return render_to_response('composers_profile/forgotpassword.html', {'form': form}, context_instance=RequestContext(request))


def token_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def resetpassword(request,token):
    if request.user.is_authenticated():
        return redirect("/composers_profile/")
    try:
        forgotpassworduser = ForgotPasswordUsers.objects.get(token=token)
        if request.method == 'POST':
            form = ResetPasswordForm(request.POST)
            if forgotpassworduser.flag == False:
                if form.is_valid():
                    forgotpassworduser.forgotpassworduser.set_password(form.cleaned_data['password'])
                    forgotpassworduser.flag = True
                    forgotpassworduser.save()
                    forgotpassworduser.forgotpassworduser.save()
                    password_reset_success = "Congras,You have updated your password successfully."
                    return render_to_response('composers_profile/resetpassword.html', {'form':form, 'password_reset_success':password_reset_success}, context_instance=RequestContext(request))
            else:
                reset_try = "You have updated your password once.Please go to login page for reset password again."
                return render_to_response('composers_profile/resetpassword.html', {'form':form, 'reset_try':reset_try}, context_instance=RequestContext(request))
        else:
            form = ResetPasswordForm()
        return render_to_response('composers_profile/resetpassword.html', {'form':form}, context_instance=RequestContext(request))
    except ForgotPasswordUsers.DoesNotExist:
        raise Http404("This page does not exist.")


@login_required
def show_list(request):
    composers = ComposersProfile.objects.all()
    for composer in composers:
        latitude = composer.latitude
        print latitude
    return render_to_response('composers_profile/show_list.html', {'composers': composers}, context_instance=RequestContext(request))

@login_required
def create(request):
    if request.method == 'POST':
        form = ComposerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/composers_profile/')
    else:
        form = ComposerForm()
    return render_to_response('composers_profile/create.html', {'form': form}, context_instance=RequestContext(request))


@login_required
def edit(request,composer_id):
    try:
        composer = ComposersProfile.objects.get(id=composer_id)
        if request.method == 'POST':
            form = ComposerForm(request.POST,instance=composer)
            if form.is_valid():
                form.save()
                return redirect('/composers_profile/')
        else:
            form = ComposerForm(instance=composer)
        return render_to_response('composers_profile/create.html', {'form': form}, context_instance=RequestContext(request))
    except ComposersProfile.DoesNotExist:
        raise Http404("This page does not exist.")


@login_required
def delete(request,composer_id):
    try:
        composer = ComposersProfile.objects.get(id=composer_id)
        composer.delete()
        return render_to_response('composers_profile/show_list.html', context_instance=RequestContext(request))
    except ComposersProfile.DoesNotExist:
        raise Http404("This page does not exist.")


@login_required
def show(request,composer_id):
    try:
        composer = ComposersProfile.objects.get(id=composer_id)
        return render_to_response('composers_profile/show.html', {'composer': composer}, context_instance=RequestContext(request))
    except ComposersProfile.DoesNotExist:
        raise Http404("This page does not exist.")


def Mypdf(request):
    # filename = 'create.pdf'
    # pdf = wkhtmltopdf(template)
    # return HttpResponse(pdf)





    # config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/html2pdf')
    # pdfkit.from_string('template', 'salary1.pdf', configuration=config)
    logger = logging.getLogger('pdf')
    logger.info('pdf file')
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/html2pdf')
    composers = ComposersProfile.objects.all()
    for composer in composers:
        context = Context({'my_name': composer.first_name,'last_name':composer.last_name })
        print context
        body = "<html>ggggggg</html>"
        template = Template("<table>My name is</table>{{ my_name }}{{ last_name }}")
        print template
        m = template.render(context)
        print m
        pdfkit.from_string(m, 'salary7.pdf', configuration=config)
        mail = EmailMultiAlternatives('Regarding Password Change','email_body','vimugdhabtr01@gmail.com',['vimugdhabtr01@gmail.com'])
        mail.attach_file('salary7.pdf')
        mail.send()
    logger.info('end')
    return HttpResponse('0')
