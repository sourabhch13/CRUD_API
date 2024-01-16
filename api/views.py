from rest_framework import status
from rest_framework.views import APIView,Response
from .models import Department,Employee
from . serializers import DepartmentSerializer,EmployeeSerializer
# Create your views here.

class DepartmentView(APIView):

    #get all the Departmemts
    def get(self,request):
        depts=DepartmentSerializer(Department.objects.all(),many=True).data
        
        response_data={
            "success": True,
            "message": "Fetched succesfully",
            "data": depts
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
    

# Employee View
    
class EmployeeView(APIView):

    #get all the Employees
    def get(self,request):
        dept=EmployeeSerializer(Employee.objects.all(),many=True).data
        
        response_data={
            "success": True,
            "message": "Fetched succesfully",
            "data": dept
        }
        return Response(response_data,status.HTTP_200_OK)
    
    def post(self,request):
        response_data={
            "success": True,
            "message": "Employee Created succesfully!"
        }
        if 'email' not in request.data:
            response_data['success']=False
            response_data['message']='email required!'

            return Response(response_data,status.HTTP_400_BAD_REQUEST)
        
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        role = request.data['role']
        department_id = request.data['department_id']
        manager_id = request.data['manager_id']

        try:
            Employee.objects.create(
                first_name=first_name, 
                last_name=last_name, 
                email=email, 
                role=role, 
                department_id=department_id,
                manager_id=manager_id
            )
        except Exception as e:
            response_data['success']=False
            response_data['message']=str(e)
            return (response_data,status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(response_data,status.HTTP_201_CREATED)

    def put(self,request,id):
        
        empl = Employee.objects.filter(id=id).first()
        response_data={
            "success": True,
            "message": "Employee Updated succesfully!"
        }
        if empl is None:
            response_data['success']=False,
            response_data['message']='Employee not found!'
            return Response(response_data,status.HTTP_404_NOT_FOUND)

        for key,value in request.data.items():
            setattr(empl,key,value)

        empl.save()

        return Response(response_data,status.HTTP_204_NO_CONTENT)
    
    def patch(self,request,id):
        return self.put(request,id)
    

    def delete(self,request,id):
        print(id)
        empl = Employee.objects.get(id=id)
        response_data={
            "success": True,
            "message": "Employee Deleted succesfully!"
        }
        if empl is None:
            response_data['success']=False,
            response_data['message']='Employee not found!'
            return Response(response_data,status.HTTP_404_NOT_FOUND)
        
        empl.delete()
        return Response(response_data,status.HTTP_204_NO_CONTENT)