from rest_framework import status
from rest_framework.views import APIView,Response
from .models import Department

# Create your views here.

class DepartmentView(APIView):

    #get all the Departmemts
    def get(self,request):
        dept=list(Department.objects.all().values())
        
        response_data={
            "success": True,
            "message": "Fetched succesfully",
            "data": dept
        }
        return Response(response_data,status.HTTP_200_OK)
    
    def post(self,request):
        response_data={
            "success": True,
            "message": "Department Created succesfully!"
        }
        if 'name' not in request.data:
            response_data['success']=False
            response_data['message']='name required!'

            return Response(response_data,status.HTTP_400_BAD_REQUEST)
        name = request.data['name']
        description = request.data['description']

        try:
            Department.objects.create(name=name, description=description)
        except Exception as e:
            response_data['success']=False
            response_data['message']=str(e)
            return (response_data,status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(response_data,status.HTTP_201_CREATED)