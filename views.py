
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here.

# class UserListView(ListView):
#     model = User
#     template_name = 'page/user_list.html'  # Default: <app_label>/<model_name>_list.html
#     context_object_name = 'users'  # Default: object_list
#     paginate_by = 10
#     queryset = User.objects.all()  # Default: Model.objects.all()

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'page/user_list.html', { 'users': users })




