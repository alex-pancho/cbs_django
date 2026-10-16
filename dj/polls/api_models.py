from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer



class PostList(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):

        posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(
            posts,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = BlogPostSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)


        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
