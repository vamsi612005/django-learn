import csv
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


def send_emails(request):
    csv_file_path = r'C:\Users\user\PycharmProjects\DjangoProject\TravelManagement\static\Book1.csv'
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Hello KLUian'  # Set your subject here
            message_body = 'Hey, Welcome to PFSD Class, Hope u have a great time with python'  # Set your email content here
            send_mail(
                subject,
                message_body,
                '2200030405cseh@gmail.com',
                [recipient_email],
                fail_silently=False,
            )
            print(f'Sent email to {recipient_email}')
    return render(request, 'Emails_sent_successfully.html')
def contact123(request):
    return render(request, 'contact.html')


from .models import *
from django.shortcuts import render, redirect


def contactmail(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        data = contactus(firstname=firstname, lastname=lastname, email=email, comments=comments)
        tosend = comments + '------------------This is just a copy of your comments'
        data.save()
    #   return redirect('newhomepage')
    # return render(request, 'contact.html')
    send_mail(
        'Thank you for Contacting Varshitha Travel and Tourism',
        tosend,
        '2200030405cseh@gmail.com',
        [email],
        fail_silently='False'

    )

