from rest_framework import viewsets
from .serializers import*
from rest_framework import filters


class CommentaireViewset(viewsets.ModelViewSet):

    queryset = models.Commentaire.objects.all()
    serializer_class = CommentaireSerializer




class ArticleViewset(viewsets.ModelViewSet):
    
    queryset = models.Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titre', ]




class TagViewset(viewsets.ModelViewSet):
    
    queryset = models.Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', ]



class CategorieArticleViewset(viewsets.ModelViewSet):
    
    queryset = models.CategorieArticle.objects.all()
    serializer_class = CategorieArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', ]
