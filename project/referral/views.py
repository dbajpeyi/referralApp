from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, HttpResponse

# Create your views here.

class JsonBaseView():
    
    def send_err(error_msg):
        return JsonResponse({
            'msg' : error_msg,
            'status' : 'error' 
        })

    def send_json(msg):
        return JsonResponse({
            'msg' : msg,
            'status' : 'ok'
        })


class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello")

class LoginView(View):
    def get(self, request):
        return render(request, 'referral/login.html', {})


    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return self.send_err("Your Django Hackathon account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return self.send_error("Invalid login details supplied.")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')
