from django.urls import path
from . import views


from apisimple.blog.apiviews import*
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('categorie', CategorieArticleViewset)
router.register('tag', TagViewset)
router.register('article', ArticleViewset)
router.register('commentaire', CommentaireViewset)

urlpatterns = [
    path("fashion",views.fashion, name="fashion"),
    path("travel",views.travel, name="travel"),
    path("single",views.single, name="single"),


]