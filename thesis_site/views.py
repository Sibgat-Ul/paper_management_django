from django.shortcuts import render, redirect, get_object_or_404
from .models import Thesis as Fetch_topic
from .models import ThesisDescription as Fetch_desc
from .forms import ThesisForm
from thesis_site.thesis_modules.topic_class import ThesisTopic, ThesisDescription
import json

# Create your views here.
# with open('thesis_site/data/topic_obj_1.json') as f:
#     topics = json.load(f)
#
# with open('thesis_site/data/desc_obj_1.json') as f:
#     desc = json.load(f)

# thesis_list = [
#     ThesisTopic(t_id=tp['TopicNo'], title=tp['Title'], supervisor=tp['ThesisSupervisor'], category=tp['Category'])
#     for tp in topics
# ]
#
# thesis_desc = [
#     ThesisDescription(t_id=des['TopicNo'], description=des['Description'])
#     for des in desc
# ]


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
    context = {
        'thesis_list': [
            ThesisTopic(
                t_id=tp.id,
                title=tp.title,
                supervisor=tp.supervisor,
                category=tp.category
            )
            for tp in thesis_list
        ]
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
        if form.is_valid():
            title = form.cleaned_data['title']
            supervisor = form.cleaned_data['supervisor']
            category = form.cleaned_data['category']

            thesis = Fetch_topic(title=title, supervisor=supervisor, category=category)
            thesis.save()

            description = form.cleaned_data['description']
            thesis_description = Fetch_desc(description=description)
            thesis_description.save()

            return redirect('thesis_details', id=id)
    else:
        form = ThesisForm()
    return render(request, 'thesis_site/add_thesis.html', {'form': form})


def edit_thesis(request, key):
    thesis = Fetch_topic.objects.get(id=key)
    thesis_desc = Fetch_desc.objects.get(id=key)
    form = ThesisForm(request.POST)



    return render(request, 'edit.html', {'form': form})

def delete_thesis(request, key):
    thesis = Fetch_topic.objects.get(id=key)
    thesis.delete()
    return redirect('thesis_topics')
