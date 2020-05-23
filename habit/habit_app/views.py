from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from .models import Habit, Progress
from .forms import HabitForm, ProgressForm
from django.views import generic
from django.views.generic import ListView


# Create your views here.


def habit_create_view(request):
    if request.method == 'POST':
        model = Habit
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Your data is saved!")
        else:
            return HttpResponse("Invalid data")
    else:
        form = HabitForm()
    context = {
        'form': form
    }
    return render(request, 'create_habit.html', context)


def habit(request):
    queryset = Habit.objects.all()
    return render(request, "home.html", {'habit_list': queryset})


# def detail(request, habit_id):
#     curr_habit = get_object_or_404(Habit, pk=habit_id)
#     return render(request, "detail.html", {"habit": curr_habit})


def detail(request, habit_id):
    curr_habit = get_object_or_404(Habit, pk=habit_id)
    progresses = Progress.objects.filter(habit=habit_id)
    if request.method == 'POST':
        model = Progress
        form = ProgressForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.habit = curr_habit
            instance.save()
            return HttpResponseRedirect(request.path_info)
        else:
            return HttpResponse("Invalid data")
    else:
        form = ProgressForm()
    context = {
        'form': form,
        'habit': curr_habit,
        'progress_list': progresses
    }
    return render(request, 'detail.html', context)
