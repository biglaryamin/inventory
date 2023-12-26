from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemDetailSerializer


@api_view()
def itemDetail(request):
    return Response("OK")