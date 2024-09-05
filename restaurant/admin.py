from django.contrib import admin
from .models import Booking, Menu

admin.site.register(Booking)
admin.site.register(Menu)

# superuser: lemon, password
# Michel, password, d20c3bbb7a9f77f9b2dc5faa2308209fc59d77ba
    # you can get the token through browsable api at http://127.0.0.1:8000/auth/token/login/
    # or insomnia through http://localhost:8000/restaurant/api-token-auth/