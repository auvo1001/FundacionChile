from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic.detail import DetailView
from management.models import Trip, Organization
from management.forms import OrganizationForm
from django.core.urlresolvers import reverse

def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('management/index.html',context_dict, context)

def login_view(request):
    context= RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username , password = password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/management/dashboard/')
            else:
                return HttpResponse("Your account is disabled")
        else:
            print "Invalid login details {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('management/login.html', {}, context)

def logout_view(request):
    logout(request)
    return redirect('/management/')

def dashboard(request):
    context = RequestContext(request)
    context_dict = {}
    latest_org_list = Organization.objects.order_by('-name')[:20]
    latest_trip_list = Trip.objects.order_by('-date')[:5]
    context_dict['latest_org_list'] = latest_org_list
    context_dict['latest_trip_list']= latest_trip_list

    return render_to_response('management/dashboard.html',context_dict, context )

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            orgs = Organization.objects.filter(name__icontains=q)
            return render(request, 'management/search_results.html',
                {'orgs': orgs, 'query': q})
    return render(request, 'management/search_form.html',
        {'error': error})

def create_organization(request):
    context = RequestContext(request)
    org_list =get_organization_list()
    context_dict={}
    context_dict['org_list']=org_list

    if request.method =='POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            created = form.save(commit=True)
            return HttpResponseRedirect(reverse('org_detail', args=(created.name,)))
        else:
            print form.errors
    else:
        form = OrganizationForm
        context_dict['form']=form
    return render_to_response('management/organization_create_form.html',context_dict,context)

def create_trip(request , organization_name_url):
    context = RequestContext(request)
    org_list=get_organization_list()
    context_dict={}
    context_dict['org_list'] = org_list
    organization_name = decode_url(organization_name_url)

    if request.method =='POST':
        form = TripForm(request.POST)
        if form.is_valid():
            page = form.save(commit = False)
            try:
                org = Organization.objects.get(name=organization_name)
                trip.organization = org
            except Organization.DoesNotExist:
                return render_to_response('mangement/organization_create_form.html',{}, context)
            trip.save()
            return OrgDetailView(request,organization_name_url)
        else:
            print form.errors
    else:
        form = TripForm()

    context_dict['organization_name_url']= organization_name_url
    context_dict['organization_name']= organization_name
    context_dict['form'] = form

    return render_to_response('management/create_trip_form.html',
                              context_dict,
                              context)

def encode_url(stri):
    return stri.replace(' ', '_')

def decode_url(stri):
    return stri.replace('_', ' ')


def OrgDetailView(request,organization_name_url):
    context = RequestContext(request)
    organization_name = decode_url(organization_name_url)
    context_dict={}
    context_dict['organization_name'] = organization_name
    context_dict['organization_name_url'] = organization_name_url
    org_list = get_organization_list()
    context_dict['org_list'] = org_list


    try:
        # Can we find a category with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        organization = Organization.objects.get(name__iexact=organization_name)
        context_dict['organization'] =organization

        #pages = Page.objects.filter(category=category).order_by('-views')
       # context_dict['pages'] = pages
    except Organization.DoesNotExist:
        pass

    if request.method =='POST':
        query =request.POST.get('query')
        if query:
            query = query.strip()
            result_list = run_query(query)
            context_dict['result_list']=result_list
    return render_to_response('management/organization_detail.html',context_dict, context)

def get_organization_list(max_results=0, starts_with=''):
        org_list=[]
        if starts_with:
            org_list = Organization.objects.filter(name__istartswith=starts_with)
        else:
            org_list = Organization.objects.all()

        if max_results >0:
            if len(cat_list) >max_results:
                org_list - org_list[:max_results]

            for org in org_list:
                org.url = encode_url(org.name)
            return org_list


