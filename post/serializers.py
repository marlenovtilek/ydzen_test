from rest_framework import serializers
from .models import Post, Comment, Rate


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'created_at', 'content']


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'post', 'content']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')
    comments = serializers.SerializerMethodField()
    mark = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'created_at', 'author', 'comments', 'mark']

    def get_comments(self, obj):
        comments = obj.post_comments.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

    def get_mark(self, obj):
        total_rate = 0
        marks = obj.marks.all()
        for mark in marks:
            total_rate += mark.value
        return total_rate / len(marks)


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['text', 'author']


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['text']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        instance = super().create(validated_data)
        return instance


class RateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['value', 'post']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        instance = super().create(validated_data)
        return instance
