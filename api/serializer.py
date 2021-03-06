from rest_framework import serializers
from .models import user, education, job, pictures, contact, project, blog_post
from django.contrib.auth.models import User

class DUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = education
        fields = ('id','url', 'title','qualification','description','start','finish')

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = job
        fields = ('id','url', 'title', 'description','start','finish')

class PicturesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pictures
        fields = ('id', 'url', 'title','alt_tag','image')

class userSerializer(serializers.HyperlinkedModelSerializer):
    user = DUserSerializer()
    picturez = PicturesSerializer(read_only=True, many=True)
    educationz = EducationSerializer(read_only=True, many=True)
    career = JobSerializer(read_only=True, many=True)
    class Meta:
        model = user
        fields = ('id','url','user', 'first_name', 'last_name', 'admin', 'about','picturez', 'educationz', 'career')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    user = userSerializer()
    class Meta:
        model = contact
        fields = ('id','url','user', 'email', 'phone')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    writer = userSerializer()
    picturez = PicturesSerializer(read_only=True, many=True)    
    class Meta:
        model = project
        fields = ('id','url','writer', 'title', 'description', 'live_link','picturez')

class Blog_PostSerializer(serializers.HyperlinkedModelSerializer):
    writer = userSerializer()
    picturez = PicturesSerializer(read_only=True, many=True)
    class Meta:
        model = blog_post
        fields = ('id','url','writer', 'title', 'content', 'picturez')
