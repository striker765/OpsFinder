from django.shortcuts import render
from .models import Job

def search_jobs(request):
    if request.method == 'POST':
        job_name = request.POST.get('job_name')
        jobs = Job.objects.filter(job_name__icontains=job_name)
    else:
        jobs = []

    return render(request, 'jobs/index.html', {'jobs': jobs})
