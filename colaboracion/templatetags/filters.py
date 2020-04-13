from django.template import Library
from django.contrib.auth.models import Group

register = Library()

def has_group(user, group_name):
	group = Group.objects.get(name=group_name)
	return True if group in user.groups.all() else False

register.filter('has_group', has_group)