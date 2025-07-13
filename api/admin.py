from django.contrib import admin
from .models import User, KYCForm  # import your models

# Register the User model
admin.site.register(User)

# Optional: also register KYCForm for verification
admin.site.register(KYCForm)
