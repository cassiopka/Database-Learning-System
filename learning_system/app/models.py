from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    """
    Модель продукта.

    Атрибуты:
    - creator (models.ForeignKey): пользователь, создавший продукт;
    - name (models.CharField): название продукта;
    - start_date (models.DateTimeField): дата начала продукта;
    - students_count (models.IntegerField): количество учеников, занимающихся на продукте;
    - average_group_filling (models.FloatField): среднее значение заполненности групп в процентах;
    - price (models.DecimalField): цена продукта.
    """
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    students_count = models.IntegerField(default=0)
    average_group_filling = models.FloatField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def get_purchase_percent(self):
        """
        Возвращает процент приобретения продукта.

        Returns:
            float: процент приобретения продукта.
        """
        total_users = User.objects.count()
        product_accesses = ProductAccess.objects.filter(product=self)
        return round(product_accesses.count() / total_users * 100, 2)
    
    def assign_user_to_group(self, user):
        """
        Распределяет пользователя в группу при получении доступа к продукту.

        Args:
            user (User): пользователь, которого нужно распределить в группу.

        Returns:
            None
        """
        groups = self.group_set.all()

        if not groups:
            group = Group.objects.create(product=self)
            ProductAccess.objects.create(user=user, product=self, group=group)
            return

        min_count = groups.annotate(count=Count('users')).order_by('count').first().count
        max_count = groups.annotate(count=Count('users')).order_by('-count').first().count

        if max_count <= self.max_group_size:
            group = groups.annotate(count=Count('users')).order_by('count').first()
            ProductAccess.objects.create(user=user, product=self, group=group)
            return

        if self.start_date > timezone.now():
            groups.update(users=None)
            for user in self.users.all():
                self.assign_user_to_group(user)
            self.assign_user_to_group(user)
            return

        users_count = self.users.count()
        group_size = (users_count // self.max_group_size) + (1 if users_count % self.max_group_size else 0)
        for i in range(self.max_group_size):
            group = Group.objects.create(product=self)
            users = self.users.all().order_by('?')[i::self.max_group_size][:group_size]
            for user in users:
                ProductAccess.objects.create(user=user, product=self, group=group)
                user.groups.add(group)
                
    max_group_size = 5
    min_group_size = 2

    def __str__(self):
        """
        Возвращает строковое представление продукта.

        Returns:
            str: название продукта.
        """
        return self.name

class ProductAccess(models.Model):
    """
    Модель для предоставления доступа пользователям к продукту и группе.

    Атрибуты:
    - user (models.ForeignKey): связь с моделью User, указывает на пользователя, которому предоставлен доступ к продукту и группе.
    - product (models.ForeignKey): связь с моделью Product, указывает на продукт, к которому предоставлен доступ.
    - group (models.ForeignKey): связь с моделью Group, указывает на группу, к которой предоставлен доступ.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        """
        Возвращает строковое представление объекта ProductAccess в формате "имя пользователя - название продукта".
        """
        return f'{self.user.username} - {self.product.name}'

class Lesson(models.Model):
    """
    Модель для представления уроков продукта.

    Атрибуты:
    - product (models.ForeignKey): связь с моделью Product, указывает на продукт, к которому относится урок.
    - name (models.CharField): название урока.
    - video_link (models.URLField): ссылка на видео урока.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=255)
    video_link = models.URLField()

    def __str__(self):
        """
        Возвращает строковое представление объекта Lesson в формате "название урока".
        """
        return self.name

class Group(models.Model):
    """
    Модель для представления групп продукта.

    Атрибуты:
    - product (models.ForeignKey): связь с моделью Product, указывает на продукт, к которому относится группа.
    - name (models.CharField): название группы.
    - users (models.ManyToManyField): связь многие-ко-многими с моделью User через модель ProductAccess, указывает на пользователей, которые имеют доступ к группе.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, through=ProductAccess, related_name='my_groups')
    
    def __str__(self):
        """
        Возвращает строковое представление объекта Group в формате "название группы".
        """
        return self.name
