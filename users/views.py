from django.shortcuts import render

from projects.models import Tag
from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    tags = Tag.objects.all()

    context = {'profiles': profiles, 'tags': tags}
    return render(request, 'users/profiles.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)

    top_skills = profile.skill_set.exclude(
        description="")  # exclude empty descriprion
    other_skills = profile.skill_set.exclude(
        description="")  # filter only by empty descriptions

    context = {'profile': profile, 'top_skills': top_skills,
               'other_skills': other_skills}
    return render(request, 'users/user-profile.html', context)
