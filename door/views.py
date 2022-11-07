from django.urls import reverse_lazy
from django.contrib.auth import logout, login

import aiohttp
from django.core.paginator import Paginator
from time import time
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .utils import *
from .forms import *
from django.http import JsonResponse
from door_manager.settings import *

CONTROLLERS = list(Door.objects.all())


class DoorHome(DataMixin, ListView):
    model = Door
    template_name = 'door/index.html'
    context_object_name = 'door'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        c_def = self.get_user_context(title='Main page')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return User.objects.filter(is_active=True).select_related('door')


class UsersHome(DataMixin, ListView):
    model = User
    template_name = 'door/users.html'
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        c_def = self.get_user_context(title='All user')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return User.objects.filter(is_active=True).select_related('door')


class UsersDoors(DataMixin, ListView):
    model = User
    template_name = 'door/users.html'
    context_object_name = 'door'
    allow_empty = False

    # this get_queryset don't work !?
    def get_queryset(self):
        return User.objects.filter(door__slug=self.kwargs['door_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.filter(door__slug=self.kwargs['door_slug'])
        c_def = self.get_user_context(title='All door')
        return dict(list(context.items()) + list(c_def.items()))


class ShowUserInfo(DataMixin, DetailView):
    model = User
    template_name = 'door/info.html'
    slug_url_kwarg = 'info_slug'
    context_object_name = 'info'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['info'])
        return dict(list(context.items()) + list(c_def.items()))


class AddUser(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddUserForm
    template_name = 'door/adduser.html'
    success_url = reverse_lazy('users')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add user'
        context['menu'] = menu
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'door/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="System registration")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ErrorPage(DataMixin, ListView):
    model = ErrorLog
    template_name = 'door/error.html'
    context_object_name = 'error'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['error'] = ErrorLog.objects.all()
        c_def = self.get_user_context(title='Error Log')
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'door/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authorisation")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class FilterHistory(DataMixin, FormView):
    form_class = HistoryForm
    template_name = 'door/history.html'
    success_url = reverse_lazy('home')


class SupportFormView(DataMixin, FormView):
    form_class = SupportForm
    template_name = 'door/support.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Describe your problem")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def about(request):
    # print (request.user.id)
    contact_list = User.objects.all()
    # paginator = Paginator(contact_list, 3)
    #
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': contact_list,
        'menu': menu,
        'title': 'Test paginator (3 users per page)',
    }

    return render(request, 'door/about.html', context=context)


# def history(request):
#     history_list = History.objects.all()
#     # door_list = Door.objects.all()
#     # user_list = User.objects.all()
#     # paginator = Paginator(history_list, 5)
#     # page_number = request.GET.get('page')
#     # page_obj = paginator.get_page(page_number)
#
#     context = {
#         'title': 'History',
#         'menu': menu,
#         'page_obj': history_list,
#         # 'door_list': door_list,
#         # 'user_list'  : user_list,
#
#     }
#     return render(request, 'door/history.html', context=context)

def history(request):
    if request.method == 'POST':
        users = request.POST.getlist('users-list')
        doors = request.POST.getlist('door')
        date_first = request.POST.get('date1')
        date_last = request.POST.get('date2')
        page_obj = History.objects.filter(
            user__name__in=users,
            door__name__in=doors,
            time_opening__range=[date_first, date_last]
        )
    else:
        page_obj = History.objects.all()
    context = {
        'title': 'History',
        'menu': menu,
        'page_obj': page_obj,
        'door_list': Door.objects.all(),
        'user_list': User.objects.all(), }

    # if form.is_valid():
    #     # search_res = []
    #     data_for_search = form.data['data_for_search']
    #
    #     # if data_for_search.isdigit():
    #     #     search_res = list(History.objects.filter(door_id=int(data_for_search)))
    #     search_res = list(History.objects.filter(name='Sacha'))
    #
    #     return render(request, "door/history.html", {"page_obj": search_res, "form": form})

    return render(request, "door/history.html", context=context)


from asgiref.sync import sync_to_async


@sync_to_async
def get_all_users(request):
    return request.user.username


@sync_to_async
def get_doors(request):
    return Door.objects.all()


async def controller_determinant(request, path, door_name):
    print(await get_all_users(request) + path + door_name)
    # print(await get_doors(request))
    try:

        d = await Door.objects.aget(name=door_name)
        u = await User.objects.aget(name=request.user.username)
        h = History(door=d, user=u)
    except Exception as err:
        err = ErrorLog(error_name=err)
        await sync_to_async(err.save)()

    if path == "grant-access":
        await sync_to_async(h.save)()

    url = [controller.url for controller in CONTROLLERS if controller.name == door_name][0] + "/" + path

    current_timestamp = int(time())

    claims = {
        'iss': 'org.netica',
        'type': 'grant-access',
        'iat': current_timestamp,
        'nbf': current_timestamp - ACCESS_TOKEN_TIME_TOLERANCE,
        'exp': current_timestamp + ACCESS_TOKEN_TIME_TOLERANCE,
    }
    jwt_token = jwt.encode({'alg': JWT_ALGORITHM}, claims, JWT_PRIVATE_KEY).decode('ascii')

    async with aiohttp.ClientSession() as session:
        response = await session.post(
            url=url,
            headers={
                'Authorization': f'Bearer {jwt_token}',
            },
        )
        try:
            resp = await response.json()
        except Exception as err:
            err = ErrorLog(error_name=err)
            await sync_to_async(err.save)()

        return JsonResponse(resp)


def errors(request):
    pass


def doors(request):
    return HttpResponse("Doors")


def edit_door(request, door):
    return HttpResponseNotFound(f' Door edit {door} ')


#   path('users/', about, name = 'users'),
#     path('history/', about, name = 'history'),
#     path('errors/', about, name = 'errors'),
#     path('admin/', about, name = 'adduser'),


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h3> Door manager. Page not found ! </h3>')


def test_error(request, year):
    if year == '5678':
        return redirect('home', permanent=True)
    if int(year) > 2022:
        raise Http404()

    return HttpResponseNotFound(f'Test_error_OK - {year}')

# handler500 -server error
# handled403 - access denied
# handler400 - unable to process request


# redirect 301  another permanent address
# redirect 401 temporarily different address
