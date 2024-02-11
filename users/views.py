from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json

@csrf_exempt
def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        data = [{'id': user.id, 'name': user.name, 'email': user.email, 'role': user.role, 'is_admin': user.is_admin} for user in users]
        return JsonResponse({'users': data})

@csrf_exempt
def get_user_by_id(request, user_id):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=user_id)
            data = {'id': user.id, 'name': user.name, 'email': user.email, 'role': user.role, 'is_admin': user.is_admin}
            return JsonResponse(data)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = User.objects.create(
                name=data['name'],
                email=data['email'],
                role=data['role'],
                is_admin=data['is_admin']
            )
            return JsonResponse({'message': 'User created successfully'}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
    else:
       
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

@csrf_exempt
def update_user(request, user_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            user = User.objects.get(id=user_id)
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            user.role = data.get('role', user.role)
            user.is_admin = data.get('is_admin', user.is_admin)
            user.save()
            return JsonResponse({'message': 'User updated successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def patch_user(request, user_id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        try:
            user = User.objects.get(id=user_id)
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            user.role = data.get('role', user.role)
            user.is_admin = data.get('is_admin', user.is_admin)
            user.save()
            return JsonResponse({'message': 'User patched successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def delete_user(request, user_id):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)