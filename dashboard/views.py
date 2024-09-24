import logging
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

def dashboard_view(request):
    log_file_path = os.path.join(settings.BASE_DIR, 'logs', 'app.log')
    log_data = []

    # Ler os logs
    try:
        with open(log_file_path, 'r') as f:
            log_data = f.readlines()
    except FileNotFoundError:
        logging.error(f"Log file not found: {log_file_path}")
        log_data = ["Log file not found."]

    return render(request, 'jobs/dashboard.html', {'log_data': log_data})

def get_log_data(request):
    log_file_path = os.path.join(settings.BASE_DIR, 'logs', 'app.log')
    log_data = []

    try:
        with open(log_file_path, 'r') as f:
            log_data = f.readlines()
    except FileNotFoundError:
        return JsonResponse({'error': 'Log file not found.'})

    log_counts = {
        'DEBUG': 0,
        'INFO': 0,
        'WARNING': 0,
        'ERROR': 0,
        'CRITICAL': 0,
    }

    for log in log_data:
        if 'DEBUG' in log:
            log_counts['DEBUG'] += 1
        elif 'INFO' in log:
            log_counts['INFO'] += 1
        elif 'WARNING' in log:
            log_counts['WARNING'] += 1
        elif 'ERROR' in log:
            log_counts['ERROR'] += 1
        elif 'CRITICAL' in log:
            log_counts['CRITICAL'] += 1

    labels = list(log_counts.keys())
    data = list(log_counts.values())

    return JsonResponse({'labels': labels, 'data': data})


