from django.shortcuts import render
from .models import Server, Job
from django.contrib.auth.decorators import login_required
@login_required
def search_jobs(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')

        servers = Server.objects.filter(server_name__icontains=search_query) if search_query else []

        jobs = Job.objects.filter(job_name__icontains=search_query) if search_query else []
    else:
        jobs = []
        servers = []

    return render(request, 'jobs/index.html', {'servers': servers, 'jobs': jobs})



def show_all_servers(request):
    servers = Server.objects.all()
    return render(request, 'jobs/index.html', {'servers': servers})

def show_all_jobs(request):
    jobs = Job.objects.all()
    return render( request,'jobs/index.html', {'jobs': jobs})

