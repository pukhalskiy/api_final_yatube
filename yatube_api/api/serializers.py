from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts import models


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = models.Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = models.Comment
        read_only_fields = ('post', )


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=models.User.objects.all(),
        default=serializers.CurrentUserDefault(),
        slug_field='username',
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=models.User.objects.all(),
    )

    class Meta:
        fields = '__all__'
        model = models.Follow

    validators = [UniqueTogetherValidator(
        queryset=models.Follow.objects.all(),
        fields=('user', 'following'))]

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя'
            )
        return data
