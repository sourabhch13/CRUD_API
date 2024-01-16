from rest_framework import status
from rest_framework.views import APIView,Response
from .models import Department
from . serializers import DepartmentSerializer
# Create your views here.

class DepartmentView(APIView):

    #get all the Departmemts
    def get(self,request):
        dept=DepartmentSerializer(Department.objects.all(),many=True).data
        
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
    
    def put(self,request,id):
        
        dept = Department.objects.filter(id=id).first()
        response_data={
            "success": True,
            "message": "Department Updated succesfully!"
        }
        if dept is None:
            response_data['success']=False,
            response_data['message']='Department not found!'
            return Response(response_data,status.HTTP_404_NOT_FOUND)

        for key,value in request.data.items():
            setattr(dept,key,value)

        dept.save()

        return Response(response_data,status.HTTP_204_NO_CONTENT)
    
    def patch(self,request,id):
        return self.put(request,id)
    

    def delete(self,request,id):
        dept = Department.objects.get(id=id)
        response_data={
            "success": True,
            "message": "Department Deleted succesfully!"
        }
        if dept is None:
            response_data['success']=False,
            response_data['message']='Department not found!'
            return Response(response_data,status.HTTP_404_NOT_FOUND)
        
        dept.delete()
        return Response(response_data,status.HTTP_204_NO_CONTENT)