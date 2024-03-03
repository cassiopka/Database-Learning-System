from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    students_count = models.IntegerField(default=0)
    average_group_filling = models.FloatField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def get_purchase_percent(self):
        total_users = User.objects.count()
        product_accesses = ProductAccess.objects.filter(product=self)
        return round(product_accesses.count() / total_users * 100, 2)
    
    def assign_user_to_group(self, user):
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

    def assign_user_to_group(self, user):

        users_count = self.users.count()
        group_size = max(self.min_group_size, min(self.max_group_size, (users_count + self.max_group_size - 1) // self.max_group_size))
        for i in range(self.max_group_size):
            group = Group.objects.create(product=self)
            users = self.users.all().order_by('?')[i::self.max_group_size][:group_size]
            for user in users:
                ProductAccess.objects.create(user=user, product=self, group=group)
                user.groups.add(group)


    def __str__(self):
        return self.name

class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=255)
    video_link = models.URLField()

    def __str__(self):
        return self.name

class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, through=ProductAccess, related_name='my_groups')
    
    def __str__(self):
        return self.name
