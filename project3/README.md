making a non dynamic profile

    django-admin startproject <project name>
    python manage.py startapp
    installing app into settings.py
    makeing a view useing httpresponse
    makeing a urls path in app folder 
        from django.urls imoprt path
        from . import views
        urlpatterns = [
            path('',views.<founction name>)
        ]
    adding url paths to main url paths in the main folder
        from django.urls import include
        urlpatterns = [
            ****
            path('',include('<app name>.urls'))
        ]

makeeing a dynamic profile
for making a dynamic profile 
    in the path of the app url'<name of the varible>'
    add the varible to founction argument and use it 

rendering a template
    in the app folder make a file named temlates
    make another file with the same name of the app
    return render(requests, "appname/filename") in the view founction with this format

sending a varible to a html file:
    def profile(request,username):
        if username in users:
            return render(request, "person/parsa.html",{'name': username})
reading it in a html file
    <h1>
    hello to {{name}}
    </h2>
u can also send a list like this 
    def profile(request,username):
    if username in users:
        return render(request, "person/parsa.html",{'username': ["parsa", "nazer"]})
and read it like this in html
    <h1>
    hello to {{name.1}}
    </h2>


for loop in django template tag:
    <main>
        <ul>
            {% for user in database %}
                <li>{{user.name}}</li>
            {% endfor %}
        </ul>
    </main>

adding a class into admin pannel
    1 making the modle
    in modles 
        class userinfo(models.Model):
            name = models.CharField(max_length=50)
            life = models.TextField()
            offon = models.BoolenField()
            view = modles.IntegrField()
            (if use str founction u can return a the name u want as the calss name in the admin pannel)
    2 migrateing it 
        py manage.py makemigrations
        py manage.py migrate
    3 adding into admin.py 
    from .models import userinfo
    admin.site.register(userinfo)
    4 creating a superuser to accsessing those data : python manage.py createsuperuser


