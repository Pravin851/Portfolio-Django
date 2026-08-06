from django.shortcuts import redirect, render

from .models import User, experience, project, resume


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate the user (you can implement your own authentication logic)
        try:
            User.objects.get(username=username, password=password)
            # User authenticated successfully, redirect to a Admin page or any other page
            return render(request, "admin.html")
        except User.DoesNotExist:
            # User not found or invalid credentials, show an error message
            return render(
                request, "login.html", {"error": "Invalid username or password"}
            )
    return render(request, "login.html")


def logout_view(request):
    from django.contrib.auth import logout

    logout(request)
    return redirect("homepage")  # Redirect to the homepage after logout


def signup(request):
    if request.method == "POST":
        # Handle form submission and user creation logic here
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Create a new user instance
        user = User(username=username, email=email, password=password)
        user.save()

    return render(request, "signup.html")


def adminpage(request):
    return render(request, "Admin.html")


def experiences(request):
    if request.method == "POST":
        username = request.POST["username"]
        company_name = request.POST["company"]
        position = request.POST["position"]
        start_date = request.POST["start_date"]
        end_date = request.POST.get("end_date")  # Optional field
        description = request.POST["description"]
        certificate = request.FILES.get("certificate")  # Optional file upload
        image = request.FILES.get("image")  # Optional image upload

        # Create a new experience instance
        user = User.objects.get(username=username)
        experience_instance = experience(
            user=user,
            company_name=company_name,
            position=position,
            start_date=start_date,
            end_date=end_date,
            description=description,
            certificate=certificate,
            image=image,
        )
        experience_instance.save()

    return render(request, "experience.html")


def resumes(request):
    if request.method == "POST":
        username = request.POST.get("username")
        file = request.FILES.get("file")
        image = request.FILES.get("image")

        # find or create user
        user = User.objects.get(username=username)

        if file:
            file = resume.objects.create(user=user, file=file, image=image)
            file.save()

        return redirect("resumes")  # reload page after upload

    resumes = resume.objects.get_queryset().order_by("-id")
    return render(request, "resume.html", {"resumes": resumes})


def Internship_Experience(request):
    data = experience.objects.all().order_by("-id")
    return render(request, "Internship.html", {"experiences": data})


def homepage(request):
    data = experience.objects.all()
    return render(request, "homepage.html", {"experiences": data})


def projects(request):
    if request.method == "POST":
        username = request.POST.get("username")
        title = request.POST.get("title")
        description = request.POST.get("description")
        link = request.POST.get("link")

        # find or create user
        user = User.objects.get(username=username)

        if title and description:
            project_instance = project.objects.create(
                user=user, title=title, description=description, link=link
            )
            project_instance.save()
    return render(request, "add-project.html")


def favicon(request):
    return redirect("/static/images/favicon.ico")


def project_info(request):
    try:
        project_instance = project.objects.all().order_by("-id")
        return render(request, "projects.html", {"projects": project_instance})
    except project.DoesNotExist:
        return render(request, "404.html", status=404)


def resume_info(request):
    try:
        resume_instance = resume.objects.get_queryset().order_by("-id")
        return render(request, "resume_view.html", {"resumes": resume_instance})
    except resume.DoesNotExist:
        return render(request, "404.html", status=404)
