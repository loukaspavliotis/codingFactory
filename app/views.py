from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, UserEditForm
from django.contrib.auth.decorators import login_required  # Import login_required
from .dto import UserCreateDTO, PlatformStatsDTO
from django.contrib.auth.models import User
from .dao import UserDAO, ProfileDAO
from .dao import UserDAO, ProfileDAO
from .dto import UserCreateDTO, PlatformStatsDTO

from django.shortcuts import render, redirect
from .dto import UserCreateDTO
from .dao import UserDAO
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully. You can now log in.')
            return redirect('login')
        else:
            # Iterate over form errors and add them to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})


from django.shortcuts import render


def custom_404(request, exception):
    return render(request, '404.html', status=404)


@login_required
def manage_users(request):
    # Use UserDAO to get all users
    users = UserDAO.get_all_users()
    return render(request, 'app/manage_users.html', {'users': users})


@login_required
def delete_user(request, user_id):
    # Use UserDAO to get the user by ID
    user = UserDAO.get_user_by_id(user_id)
    if request.method == 'POST':
        # Use UserDAO to delete the user
        UserDAO.delete_user(user)
        messages.success(request, 'User deleted successfully.')
        return redirect('manage_users')
    return render(request, 'app/confirm_delete.html', {'user': user})


@login_required
def edit_user(request, user_id):
    # Use UserDAO to get the user by ID
    user = UserDAO.get_user_by_id(user_id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            # Save the updated user via the DAO
            UserDAO.update_user(user, form.cleaned_data)
            messages.success(request, 'User updated successfully.')
            return redirect('manage_users')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'app/edit_user.html', {'form': form})


# @login_required
# def manage_users(request):
#     users = User.objects.all()
#     return render(request, 'app/manage_users.html', {'users': users})
#
# @login_required
# def delete_user(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.method == 'POST':
#         user.delete()
#         messages.success(request, 'User deleted successfully.')
#         return redirect('manage_users')
#     return render(request, 'app/confirm_delete.html', {'user': user})
#
# @login_required
# def edit_user(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.method == 'POST':
#         form = UserEditForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'User updated successfully.')
#             return redirect('manage_users')
#     else:
#         form = UserEditForm(instance=user)
#     return render(request, 'app/edit_user.html', {'form': form})
@login_required
def home(request):
    total_users = UserDAO.get_total_users()
    active_users = UserDAO.get_active_users()
    latest_users = ProfileDAO.get_latest_users()

    # Calculate active user percentage (0 if total_users is 0 to avoid division by zero)
    active_user_percentage = 0
    if total_users > 0:
        active_user_percentage = (active_users / total_users) * 100

    # Create PlatformStatsDTO with the new field
    stats_dto = PlatformStatsDTO(
        total_users=total_users,
        active_users=active_users,
        latest_users=latest_users,
        active_user_percentage=active_user_percentage
    )

    context = {
        'stats': stats_dto
    }
    return render(request, 'app/home.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')  # Redirect to your desired home page
                else:
                    messages.error(request, 'Your account is deactivated. Please contact the administrator.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})


from django.shortcuts import get_object_or_404


def user_logout(request):
    logout(request)
    return redirect('login')
