from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Post, Comment
from .permissions import IsOwnerOrIsStaffOrReadOnly
from .serializers import PostSerializer, PostUpdateSerializer, PostCreateSerializer, CommentSerializer, \
    RateCreateSerializer, CommentCreateSerializer


class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrIsStaffOrReadOnly]

    def get_serializer_class(self):
        if self.action == "update":
            return PostUpdateSerializer
        elif self.action == "post_add":
            return PostCreateSerializer
        elif self.action == "add_comment":
            return CommentCreateSerializer
        elif self.action == "mark_add":
            return RateCreateSerializer
        else:
            return PostSerializer

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def post_add(self, request):
        serializer = PostCreateSerializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        return Response(PostSerializer(post).data)

    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        post = self.get_object()
        serializer = CommentCreateSerializer(data=request.data, context=self.get_serializer_context())
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.post_comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def mark_add(self, request, pk=None):
        post = self.get_object()
        data = request.data.copy()
        data["post"] = post.id
        serializer = RateCreateSerializer(data=data, context=self.get_serializer_context())
        serializer.is_valid()
        serializer.save()
        return Response(PostSerializer(post).data)



