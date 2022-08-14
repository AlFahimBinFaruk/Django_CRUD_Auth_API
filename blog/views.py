from rest_framework.response import Response
from .serializers import BlogSerializer, BlogGetSerializer
from rest_framework.views import APIView
from .models import Blog
from account.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# my blog list

class MyBlogList(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated]
    # this will output only 3 objects per page
    page_size = 5

    def get(self, request):
        user = User.objects.get(id=self.request.user.id)
        # get blog list of specific user
        myBlogList = user.blog_set.all()
        # paginate them
        results = self.paginate_queryset(myBlogList, request, view=self)
        serializer = BlogGetSerializer(results, many=True)
        # send paginated data
        return self.get_paginated_response(serializer.data)


# my blog details


class MyBlogDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        blog = Blog.objects.get(blogger=request.user, id=pk)
        # serialize
        serializedBlogDetail = BlogGetSerializer(blog, many=False)
        return Response(serializedBlogDetail.data)


# create new blog


class CreateNewBlog(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        newBlogSerializer = BlogSerializer(data=request.data)
        if newBlogSerializer.is_valid():
            # dynamicly push data inside serializers
            newBlogSerializer.save(blogger=self.request.user)
            return Response(newBlogSerializer.data)
        else:
            return Response(newBlogSerializer.errors)

# update the blog


class UpdateBlog(APIView):
    def patch(self, request, pk):
        blog = Blog.objects.get(id=pk)
        if blog.blogger == request.user:
            updateBlogSerializer = BlogSerializer(blog, data=request.data)
            if updateBlogSerializer.is_valid():
                updateBlogSerializer.save()
                return Response(updateBlogSerializer.data)
            else:
                return Response(updateBlogSerializer.errors)
        else:
            return Response({"msg": "You cant update this!"})

# delete blog


class DeleteBlog(APIView):
    def delete(self, request, pk):
        blog = Blog.objects.get(id=pk)
        if blog.blogger == request.user:
            blog.delete()
            return Response({"deleted": pk})
        else:
            return Response({"msg": "You cant delete this!"})
