from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import TemplateView
from accounts.forms import LoginForm


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            print("Form is not valid")
            return redirect('index')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            print("User authentication failed")
            return redirect('index')
        print("User authentication successful")
        login(request, user)
        next_request = request.GET.get('next')
        if next_request:
            return redirect(next_request)
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')

