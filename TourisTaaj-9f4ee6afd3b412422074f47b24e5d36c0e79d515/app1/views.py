from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib import messages
from django.db import IntegrityError
from .models import Registration

# project_name/app_name/views.py
from django.http import HttpResponseForbidden


session = {'username':None}

def restricted_view(request, url):
    referring_url = request.META.get('HTTP_REFERER')

    # Check if the referring URL matches the expected URL
    if referring_url == url:
        # Allow access to the restricted content
        return True
    else:
        # Deny access or redirect to another URL
        return False


token_generator = PasswordResetTokenGenerator()

# Create your views here.

def HomePage(request):
    return render(request, 'index.html')


def verifyEmail(request):
    global token_generator
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        try:
            user = User.objects.create_user(username=uname, email=email, password=pass1)
            user.is_active = False
            user.save()
            token = token_generator.make_token(user)
            activation_link = generateVerificationURL(token, user)
            status = sendEmail(activation_link, email)
            messages.add_message(request, messages.INFO, 'Registration successful! Please check your email to verify your account.')
            return redirect('login')
        except IntegrityError:
            # Redirect with error message if the username is taken
            messages.add_message(request, messages.ERROR, 'Username already exists. Please try a different one.')
            return redirect('login')
        except Exception as e:
            # Handle other exceptions and provide a generic error message
            messages.add_message(request, messages.ERROR, 'An unexpected error occurred. Please try again.')
            return redirect('login')

def generateVerificationURL(token, user:User):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    link = reverse('activate', kwargs={'uidb64': uid, 'token': token})
    activation_link = 'http://localhost:8000'+link
    return activation_link

def sendEmail(activation_link, email):
    email_subject = 'Activate your account'
    email_body = 'Click on the link below to activate your account\n'+activation_link
    email = EmailMessage(
        email_subject,
        email_body,
        'jaysadhu21@gnu.ac.in',
        [email],
    )
    email.send(fail_silently=False)
    return True

def activate(request, uidb64, token):
    global token_generator
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
        if token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            return HttpResponse('Activation link is invalid!')
    except Exception as ex:
        pass


def LoginPage(request):
    # print(request.method)
    if request.method == 'POST':
        print(request.POST)
        uname = request.POST['username']
        pass1 = request.POST['password']
        print(uname, pass1)

        # Authenticate the user
        u = User.objects.get(username=uname)
        if u is not None:
            if u.check_password(pass1):
                print('Password is correct')
            else:
                print(pass1)
        else:
            print('username not found')
        user = authenticate(username=uname, password=pass1)
        print('user found', user)

        if user is not None:
            print('user found')
            if user.is_active:  # Check if the user is active (verified)
                login(request, user)
                session['username'] = uname
                return redirect('/registration/')  # Redirect to registration page
            else:
                messages.add_message(request, messages.ERROR, 'Your account is not verified. Please check your email for the verification link.')
        else:
            # Check if the username exists in the database
            try:
                User.objects.get(username=uname)
                messages.add_message(request, messages.ERROR, 'Invalid password.')
            except User.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'Invalid username.')

    return render(request, 'login.html')

def registerPage(request):
    status = restricted_view(request, 'http://localhost:8000/login/')
    if not status:
        return redirect('/login/')

    return render(request, 'registration.html', {'username': session['username']})



def save_data(request):
    if request.method == 'POST':
        # Get the form data
        user_id = request.POST['user_id']
        yearly_avg_view = request.POST['yearly_avg_view']
        frequentflyer = request.POST['frequentflyer'] == 'Yes'
        preferred_device = request.POST['preferred_device']
        yearly_avg_outstation_checkins = request.POST['yearly_avg_outstation_checkins']
        annual_income_class = request.POST['annual_income_class']
        member_in_family = request.POST['member_in_family']
        booking_hotel = request.POST['booking_hotel'] == 'Yes'
        preferred_location_type = ','.join(request.POST.getlist('preferred_location_type'))
        working_flag = request.POST['working_flag'] == 'Yes'
        travelling_rating = request.POST['travelling_rating']

        # Create a new Registration object and save it
        registration = Registration(
            username=user_id,
            yearly_avg_view=yearly_avg_view,
            frequentflyer=frequentflyer,
            preferred_device=preferred_device,
            yearly_avg_outstation_checkins=yearly_avg_outstation_checkins,
            annual_income_class=annual_income_class,
            member_in_family=member_in_family,
            booking_hotel=booking_hotel,
            preferred_location_type=preferred_location_type,
            working_flag=working_flag,
            travelling_rating=travelling_rating
        )
        registration.save()

        # Redirect to a success page or any other desired page
        return redirect('/')

    # If the request is not POST, render the registration form
    return render(request, 'registration.html')