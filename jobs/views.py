from django.shortcuts import render
from .models import Job
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from servidores.models import Servidores_FastShop, Servidores_CC 
from django.contrib.auth.models import User
@login_required
def search_jobs(request):
    search_query = request.POST.get('search_query', '') if request.method == 'POST' else ''
    
    servidores_fastshop = Servidores_FastShop.objects.filter(server_name__icontains=search_query) if search_query else Servidores_FastShop.objects.none()
    servidores_cc = Servidores_CC.objects.filter(server_name__icontains=search_query) if search_query else Servidores_CC.objects.none()
    jobs = Job.objects.filter(job_name__icontains=search_query) if search_query else Job.objects.none()
    
    message = ""
    if not (servidores_cc or servidores_fastshop or jobs):
        message = "No results found for your search."
    
    return render(request, 'jobs/index.html', {
        'Servidores_FastShop': servidores_fastshop,
        'Servidores_CC': servidores_cc,
        'jobs': jobs,
        'message': message,
    })

@login_required
def show_all_jobs(request):
    jobs = Job.objects.all()
    
    
    num_display = request.GET.get('num_display', 5)
    paginator = Paginator(jobs, int(num_display))

    page_number = request.GET.get('page')
    jobs_page = paginator.get_page(page_number)

    return render(request, 'jobs/index.html', {
        'jobs': jobs_page,
        'num_display': num_display,
    })

@login_required
def show_all_servers(request):
    servidores_cc = Servidores_CC.objects.all()  
    
    num_display = request.GET.get('num_display', 5)
    paginator = Paginator(servidores_cc, int(num_display))

    page_number = request.GET.get('page')
    servers_page = paginator.get_page(page_number)

    return render(request, 'jobs/index.html', {
        'Servidores_CC': servers_page,
        'num_display': num_display,
        'jobs': [],  
        'message': "",  
})
@login_required
def ajuda(request):
    return render(request, 'jobs/ajuda.html')


@login_required
def show_all_fastshop(request):
    servidores_fastshop = Servidores_FastShop.objects.all()  
    
    num_display = request.GET.get('num_display', 5)
    paginator = Paginator(servidores_fastshop, int(num_display))

    page_number = request.GET.get('page')
    fastshop_page = paginator.get_page(page_number)

    return render(request, 'jobs/index.html', {
        'Servidores_FastShop': fastshop_page,
        'num_display': num_display,
        'jobs': [],  
        'message': "",  
 })


@login_required
def dashboard(request):
    total_users = User.objects.count()
    total_servidores_cc = Servidores_CC.objects.count()
    total_servidores_fastshop = Servidores_FastShop.objects.count()
    total_jobs = Job.objects.count()

    context = {
        'total_users': total_users,
        'total_servidores_cc': total_servidores_cc,
        'total_servidores_fastshop': total_servidores_fastshop,
        'total_jobs': total_jobs,
    }
    
    return render(request, 'jobs/dashboard.html', context)