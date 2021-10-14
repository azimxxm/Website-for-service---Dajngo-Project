from django.db import models


class Advantages(models.Model):
    title = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Xizmatlar texnologiyalari'
        verbose_name_plural = 'Xizmatlar texnologiyalari'

    def __str__(self):
        return self.title


class Service(models.Model):
    service_name = models.CharField(max_length=50)
    service_info = models.TextField(max_length=150)
    advantages = models.ManyToManyField(Advantages)
    icon = models.CharField(max_length=50)
    color_icon = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Xizmatlar'
        verbose_name_plural = 'Xizmatlar'

    def __str__(self):
        return self.service_name


class Home(models.Model):
    title = models.CharField(max_length=50)
    info_title = models.TextField(max_length=100)
    image = models.ImageField(upload_to="Home/%Y/%M/")
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Asosiy'
        verbose_name_plural = 'Asosiy'

    def __str__(self):
        return self.title


class Service_about(models.Model):
    title = models.CharField(max_length=50)
    info_title = models.TextField(max_length=200)
    image = models.ImageField(upload_to="Service/%Y/%M/")
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Xizmat haqida'
        verbose_name_plural = 'Xizmat haqida'

    def __str__(self):
        return self.title


class Modal_texnology(models.Model):
    title = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Xizmat turi texnologiyalari'
        verbose_name_plural = 'Xizmat turi texnologiyalari'

    def __str__(self):
        return self.title


class Service_modal(models.Model):
    title1 = models.CharField(max_length=50)
    info_title1 = models.TextField(max_length=200)
    title2 = models.CharField(max_length=50)
    info_title2 = models.TextField(max_length=200)
    texnology = models.ManyToManyField(Modal_texnology)
    image = models.ImageField(upload_to="Service_modal/%Y/%M/")
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Xizmat turi modeli'
        verbose_name_plural = 'Xizmat turi modeli'

    def __str__(self):
        return f'{self.title1} - {self.title2}'


class Service_about2(models.Model):
    title = models.CharField(max_length=100)
    info_title = models.TextField(max_length=220)
    happy_customers = models.IntegerField(default=0)
    issues_solved = models.IntegerField(default=0)
    image = models.ImageField(upload_to="Service_about2/%Y/%M/")
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Xizmat haqida 2'
        verbose_name_plural = 'Xizmat haqida 2'

    def __str__(self):
        return self.title


class Projects_type(models.Model):
    title = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Project turlari'
        verbose_name_plural = 'Project turlari'

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=50)
    info_title = models.TextField(max_length=100)
    project_types = models.ManyToManyField(Projects_type)
    image = models.ImageField(upload_to="Projects/%Y/%M/")
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Projectlar'
        verbose_name_plural = 'Projectlar'

    def __str__(self):
        return self.title


class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    work_types = models.CharField(max_length=50)
    comments = models.TextField(max_length=100)
    image = models.ImageField(upload_to="Testimonials/%Y/%M/")
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Izoxlar'
        verbose_name_plural = 'Izoxlar'

    def __str__(self):
        return self.name


class Plan_type(models.Model):
    plan_types = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tariflar'
        verbose_name_plural = 'Tariflar'

    def __str__(self):
        return self.plan_types


class Pricing(models.Model):
    plan_name = models.CharField(max_length=20)
    plan_types = models.ManyToManyField(Plan_type)
    plan_price = models.BigIntegerField(default=0)
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Narxlar'
        verbose_name_plural = 'Narxlar'

    def __str__(self):
        return self.plan_name


class Work_tpye(models.Model):
    work_type_name = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Xizmat turi'
        verbose_name_plural = 'Xizmat turi'

    def __str__(self):
        return self.work_type_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField(blank=True)
    work_tpye = models.ForeignKey(Work_tpye, on_delete=models.CASCADE)
    message = models.TextField(max_length=300)
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Xabarlar'
        verbose_name_plural = 'Xabarlar'

    def __str__(self):
        return self.name
