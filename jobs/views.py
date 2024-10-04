from django.shortcuts import render
from .models import Cc_server, Job, Cc_fast
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def search_jobs(request):
    search_query = request.POST.get('search_query', '') if request.method == 'POST' else ''
    
    cc_servers = Cc_server.objects.filter(server_name__icontains=search_query) if search_query else Cc_server.objects.none()
    cc_fast = Cc_fast.objects.filter(server_name__icontains=search_query) if search_query else Cc_fast.objects.none()
    jobs = Job.objects.filter(job_name__icontains=search_query) if search_query else Job.objects.none()
    
    message = ""
    if not (cc_servers or cc_fast or jobs):
        message = "No results found for your search."
    
    return render(request, 'jobs/index.html', {
        'cc_servers': cc_servers,
        'cc_fast': cc_fast,
        'jobs': jobs,
        'message': message,
    })

@login_required
def show_all_jobs(request):
    jobs = Job.objects.all()
    
    num_display = request.GET.get('num_display', '10')
    paginator = Paginator(jobs, jobs.count() if num_display == 'all' else int(num_display))
    
    page_number = request.GET.get('page')
    jobs_page = paginator.get_page(page_number)

    return render(request, 'jobs/index.html', {
        'jobs': jobs_page,
        'num_display': num_display,
    })

@login_required
def show_all_servers(request):
    cc_servers = Cc_server.objects.all()
    
    num_display = request.GET.get('num_display', '10')
    paginator = Paginator(cc_servers, cc_servers.count() if num_display == 'all' else int(num_display))
    
    page_number = request.GET.get('page')
    servers_page = paginator.get_page(page_number)

    return render(request, 'jobs/index.html', {
        'cc_servers': servers_page,
        'num_display': num_display,
    })

@login_required
def ajuda(request):
    return render(request, 'jobs/ajuda.html')
