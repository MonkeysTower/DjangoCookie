from django.shortcuts import render, redirect
from django.http import HttpResponse

def cookie_session(request):
   request.session.set_test_cookie()
   return HttpResponse("<h1>dataflair</h1>")

def cookie_delete(request):
   if request.session.test_cookie_worked():
       request.session.delete_test_cookie()
       response = HttpResponse("dataflair<br> cookie createed")
   else:
       response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
   return response

def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")

def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('name'):
        response += f"Name: {request.session.get('name')} <br>"
    if request.session.get('password'):
        response += f"Password: {request.session.get('password')} <br>"
    else:
        return redirect('create/')
    return HttpResponse(response)

def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")

def flush_session(request):
    request.session.flush()
    return HttpResponse("<h1>dataflair<br>Session and Cookie flushed</h1>")