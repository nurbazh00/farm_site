from django.db import models


class Companies(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Компании'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class Company (models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание',)
    picture = models.ImageField(upload_to='company',
                                null=True,
                                blank=True,
                                verbose_name='Изображение',)
    companies = models.ForeignKey(Companies,
                                  on_delete=models.SET_NULL,
                                  related_name='company',
                                  null=True)
    typeProduct = models.CharField(verbose_name='Тип продуктов',
                                   max_length=255)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name

    @property
    def get_first_picture(self):
        return self.picture


class Product (models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    company = models.ForeignKey(Company,
                                on_delete=models.SET_NULL,
                                related_name='product',
                                null=True)
    picture = models.ImageField(upload_to='product',
                                null=True,
                                blank=True,
                                verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Success_story (models.Model):
    feedback = models.TextField(verbose_name='Фидбэк')
    picture = models.ImageField(upload_to='success_stories',
                                null=True,
                                blank=True,
                                verbose_name='Изображение')

    class Meta:
        verbose_name = 'Успешная история'
        verbose_name_plural = 'Успешные истории'

    def __str__(self):
        return self.feedback


class About_us (models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=False)
    picture = models.ImageField(upload_to='about_us',
                                null=True,
                                blank=True,
                                verbose_name='Изображение',)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.name


class Application (models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField(null=False)
    country = models.CharField(max_length=50)
    mail = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=20)
    telegram = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.telegram


class Contact(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    phone_one = models.CharField(max_length=20)
    whatsapp_number = models.URLField(max_length=200)
    phone_two = models.CharField(max_length=20)
    instagram = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    youtube = models.URLField(max_length=200)
    gmail = models.URLField(max_length=200)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.phone_one