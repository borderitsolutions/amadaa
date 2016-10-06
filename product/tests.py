from django.test import TestCase
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from product.views import ProductCategoryCreate, ProductCategoryUpdate, ProductCategoryDelete
from product.models import ProductCategory

# Create your tests here.

class ProductCategoryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.user.save()
        self.content_type = ContentType.objects.get_for_model(ProductCategory)

    def test_anon_add_permission(self):
        self.client.logout()
        response = self.client.get('/product/category/add/')
        self.assertEquals(response.status_code, 403)

    def test_anon_update_permission(self):
        self.client.logout()
        response = self.client.get('/product/category/update/1/')
        self.assertEquals(response.status_code, 403)

    def test_anon_delete_permission(self):
        self.client.logout()
        response = self.client.get('/product/category/delete/1/')
        self.assertEquals(response.status_code, 403)

    def test_denied_user_add_permission(self):
        perm = Permission.objects.get(content_type=self.content_type, 
                codename='add_productcategory')
        self.user.user_permissions.remove(perm)
        self.user.save()
        self.client.login(username='u', password='p')
        response = self.client.get('/product/category/add/')
        self.assertEquals(response.status_code, 403)
        self.client.logout()

    def test_denied_user_update_permission(self):
        perm = Permission.objects.get(content_type=self.content_type,
                codename='change_productcategory')
        self.user.user_permissions.remove(perm)
        self.user.save()
        self.client.login(username='u', password='p')
        response = self.client.get('/product/category/update/1/')
        self.assertEquals(response.status_code, 403)
        self.client.logout()

    def test_denied_user_delete_permission(self):
        perm = Permission.objects.get(content_type=self.content_type,
                codename='delete_productcategory')
        self.user.user_permissions.remove(perm)
        self.user.save()
        self.client.login(username='u', password='p')
        response = self.client.get('/product/category/delete/1/')
        self.assertEquals(response.status_code, 403)
        self.client.logout()
    
    def test_allowed_user_add_permission(self):
        perm = Permission.objects.get(content_type=self.content_type,
                codename='add_productcategory')
        self.user.user_permissions.add(perm)
        self.user.save()
        self.client.login(username='u', password='p')
        response = self.client.get('/product/category/add/')
        self.assertEquals(response.status_code, 200)
        self.client.logout()

    def test_allowed_user_update_permission(self):
        category = ProductCategory(name='testing')
        category.save()
        perm = Permission.objects.get(content_type=self.content_type,
                codename='change_productcategory')
        self.user.user_permissions.add(perm)
        self.user.save()
        self.client.login(username='u', password='p')
        url = "/product/category/update/{}/".format(category.id)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_allowed_user_delete_permission(self):
        category = ProductCategory(name='to be deleted')
        category.save()
        perm = Permission.objects.get(content_type=self.content_type,
                codename='delete_productcategory')
        self.user.user_permissions.add(perm)
        self.user.save()
        self.client.login(username='u', password='p')
        url = '/product/category/update/{}'.format(category.id)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 301)
