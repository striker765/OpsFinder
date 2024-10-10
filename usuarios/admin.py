from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.sites import AlreadyRegistered
import logging

logger = logging.getLogger(__name__)

User = get_user_model()

def register_user_model():
    try:
        admin.site.register(User, UserAdmin)
    except AlreadyRegistered:
        logger.info(f"{User.__name__} already registered in admin site.")

register_user_model()
