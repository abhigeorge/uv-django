from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def upload_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("gallery")
    else:
        form = ImageForm()
    return render(request, "gallery/upload.html", {"form": form})

def gallery_view(request):
    images = Image.objects.all().order_by("-uploaded_at")
    return render(request, "gallery/gallery.html", {"images": images})