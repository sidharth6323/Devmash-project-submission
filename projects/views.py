from django.shortcuts import render,render_to_response,RequestContext
from projects.models import users,project,s_project
# Create your views here.

def submit_project(request,track,p_name):
	project_l = project.objects.get(p_name=p_name)
	if request.method=="POST":
		g_uname= request.POST.get("g_uname")
		repo_link= request.POST.get("repo_link")
		hosted_url = request.POST.get("hosted_url")
		try:
			user_l= users.objects.get(g_uname=g_uname)
		except:
			error = "Please Enter correct github username!"
			return render_to_response("submit.html",{"error":error},RequestContext(request))
		project_l = project.objects.get(p_name=p_name)
		user_l.p_submitted.add(project_l)
		s_project.objects.create(project=project_l,user=user_l,repo_link=repo_link,hosted_url=hosted_url)
		user_l.save()
	return render_to_response("submit.html",{"project":project_l},RequestContext(request))
