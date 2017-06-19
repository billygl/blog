from posts.models import Usuario, Post
from rest_framework import serializers, viewsets

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('usuario', 'nombre')
		
# Serializers define the API representation.
class PostSerializer(serializers.HyperlinkedModelSerializer):
    usuario_pub = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field="nombre")
    class Meta:
        model = Post
        fields = ('titulo', 'contenido', 'fecha_pub', 'fecha_mod', 'usuario_pub', 'categoria')
		
# ViewSets define the view behavior.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
	
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
