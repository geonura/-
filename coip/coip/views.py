from django.shortcuts import render

def main(request):
    return render(request, 'coip/main.html')

def team(request):
    return render(request, 'coip/team.html')