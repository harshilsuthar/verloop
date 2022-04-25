from rest_framework.exceptions import APIException
from rest_framework.viewsets import ViewSet
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

gmaps = settings.GMAPS

class getAddressDetails(ViewSet):

    # renderer_classes = [JSONRenderer, XMLRenderer]

    def get_renderers(self):
        output_format = self.request.POST.get("output_format")
        if output_format == 'json':
            return [JSONRenderer()]
        elif output_format == 'xml':
            return [XMLRenderer()]
        return super().get_renderers()
    
    def create(self, request):
        address = request.POST.get("address")
        output_format= str(request.POST.get("output_format")).lower()
        if not address:
            raise APIException("Provide valid address!", code=400)
    
        if output_format not in ["json", "xml"]:
            raise APIException("Provide valid output format!", code=400)
        
        geocode_result = gmaps.geocode(address)
        if not geocode_result:
            raise APIException("No Result Found!", code=400)
        coordinates = geocode_result[0].get("geometry", {}).get("location")
        response = {
            "address": address,
            "coordinates": coordinates
        }
        return Response(response, status=status.HTTP_200_OK)