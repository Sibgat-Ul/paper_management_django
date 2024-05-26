from django.shortcuts import render, redirect, get_object_or_404
from .models import Thesis as Fetch_topic
from .models import ThesisDescription as Fetch_desc
from .forms import ThesisForm
from thesis_site.thesis_modules.topic_class import ThesisTopic, ThesisDescription
import json


def home(request):
    return render(request, 'thesis_site/home.html')


def about(request):
    makers = [
        {'name': 'Mohammad Reza', 'id': 's366400'},
        {'name': 'Nusrat Jahan', 'id': 's366401'},
        {'name': 'Fauzia Khanom Luna', 'id': 's366819'},
        {'name': 'Umme Salma Rumana', 'id': 's367994'}
    ]

    context = {
        'makers': makers
    }

    return render(request, 'thesis_site/about.html', context)


def thesis_topics(request):
    thesis_list = Fetch_topic.objects.all()

    thesis_list = [
        ThesisTopic(
            t_id=tp.id,
            title=tp.title,
            supervisor=tp.supervisor,
            category=tp.category
        )
        for tp in thesis_list
    ]

    context = {
        'thesis_list': thesis_list
    }

    return render(request, context=context, template_name='thesis_site/thesis_topic.html')


def thesis_details(request, id):
    topic = Fetch_topic.objects.get(id=id)
    desc = Fetch_desc.objects.get(id=id)

    topic_t = ThesisTopic(t_id=topic.id, title=topic.title, supervisor=topic.supervisor, category=topic.category)
    topic_desc = ThesisDescription(t_id=desc.id, description=desc.description)

    context = {
        'topic_desc': topic_desc,
        'topic': topic_t
    }

    return render(request, context=context, template_name='thesis_site/thesis_details.html')


# Create thesis
def add_thesis(request):
    if request.method == 'POST':
        form = ThesisForm(request.POST)
        try:
            if form.is_valid():
                title = form.cleaned_data['title']
                supervisor = form.cleaned_data['supervisor']
                category = form.cleaned_data['category']

                thesis = Fetch_topic(title=title, supervisor=supervisor, category=category)
                thesis.save()

                description = form.cleaned_data['description']
                thesis_description = Fetch_desc(id=thesis, description=description)

                thesis_description.save()
                return redirect('thesis_details', id=thesis.id)
            else:
                return redirect('errors', form.errors.as_data())
        except Exception as e:
            return redirect('errors', e)
    else:
        form = ThesisForm(request.POST)
    return render(request, 'thesis_site/add_thesis.html', {'form': form})


def edit_thesis(request, id):
    thesis = Fetch_topic.objects.get(id=id)
    thesis_desc = Fetch_desc.objects.get(id=thesis)

    form = ThesisForm(request.POST)

    context = {
        'form': form,
        'thesis': thesis,
        'thesis_desc': thesis_desc
    }

    if request.method == 'POST':
        form = ThesisForm(request.POST)

        try:
            if form.is_valid():
                thesis.title = form.cleaned_data['title']
                thesis.supervisor = form.cleaned_data['supervisor']
                thesis.category = form.cleaned_data['category']
                thesis_desc.description = form.cleaned_data['description']

                thesis.save()
                thesis_desc.save()
                return redirect('thesis_topics')
            else:
                return redirect('errors', form.errors.as_data())

        except Exception as e:
            return redirect('errors', e)
    return render(request, 'thesis_site/edit_thesis.html', context)


def delete_thesis(request, id):
    thesis = Fetch_topic.objects.get(id=id)
    thesis.delete()
    return redirect('thesis_topics')

# Error handling
def error(request, exception):
    return render(request, 'thesis_site/errors.html', context=exception)
