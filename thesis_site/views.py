from django.shortcuts import render
from thesis_site.thesis_modules.topic_class import ThesisTopic, ThesisDescription
import json

# Create your views here.
with open('thesis_site/data/topic_obj_1.json') as f:
    topics = json.load(f)

with open('thesis_site/data/desc_obj_1.json') as f:
    desc = json.load(f)

thesis_list = [
    ThesisTopic(t_id=tp['TopicNo'], title=tp['Title'], supervisor=tp['ThesisSupervisor'], category=tp['Category'])
    for tp in topics
]

thesis_desc = [
    ThesisDescription(t_id=des['TopicNo'], description=des['Description'])
    for des in desc
]


def home(request):
    return render(request, 'thesis_site/home.html')


def about(request):
    makers = [
        {'name':'Mohammad Reza', 'id':'s366400'},
        {'name':'Nusrat Jahan', 'id':'s366401'},
        {'name':'Fauzia Khanom Luna', 'id':'s366819'},
        {'name':'Umme Salma Rumana', 'id':'s367994'}
    ]

    context = {
        'makers': makers
    }

    return render(request, 'thesis_site/about.html', context)


def thesis_topics(request):
    context = {
        'topics': thesis_list
    }
    return render(request, context=context, template_name='thesis_site/thesis_topic.html')


def thesis_details(request, id):
    topic_desc = None
    topic_t = None

    for t_d, t_t in zip(thesis_desc, thesis_list):
        if t_d.TopicNo == id and t_t.TopicNo == id:
            topic_desc = t_d
            topic_t = t_t
            break
    print(topic_desc.TopicNo, topic_t.TopicNo)

    context = {
        'topic_desc': topic_desc,
        'topic': topic_t
    }
    return render(request, context=context, template_name='thesis_site/thesis_details.html')

