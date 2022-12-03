from django.shortcuts import redirect, render


def showAboutMe(request):
    return render(request, 'about-me.html')

def showAboutProject(request):
    return render(request, 'about-project.html')
