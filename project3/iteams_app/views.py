from django.shortcuts import render
from .models import iteams
# Create your views here.
def iteam_page(request):
    shop_iteams = iteams.objects.all
    return render(request, "iteams_app/iteam_page.html",context={'iteams':shop_iteams})