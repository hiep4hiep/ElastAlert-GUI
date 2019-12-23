from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rule.models import Rule
from .forms import CreateRuleForm, ViewRuleForm
import os

def create_yaml(filename,rname,rtype,rindex,rnumevents,rfilter,ralert,rcommand):
    rulefile = """\
es_host: elasticsearch.example.com
es_port: 9200
name: {0}
type: {1}
index: {2}
num_events: {3}
timeframe:
  hours: 1
filter:
{4}
alert:
- {5}
pipe_match_json: true
command: "{6}"
"""
    rulefile = rulefile.format(rname,rtype,rindex,rnumevents,rfilter,ralert,rcommand)
    print(rtype)
    print(rindex)
    path = '/etc/elastalert/example_rules/'
    filename = path + filename + '.yaml'
    with open(filename,"w") as f:
        f.write(rulefile)

# Create your views here.
def home(request):
    rules = Rule.objects.all()
    return render(request, 'home.html', {'rules': rules})

def create_rule(request):
    if request.method == 'POST':
        form = CreateRuleForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.save()
            rulename = form.cleaned_data.get('name')
            ruletype = form.cleaned_data.get('type')
            index = form.cleaned_data.get('index')
            num_events = form.cleaned_data.get('num_events')
            rulefilter = form.cleaned_data.get('filter')
            alert = form.cleaned_data.get('alert')
            command = form.cleaned_data.get('command')
            create_yaml(rulename, rulename, ruletype, index, num_events, rulefilter, alert, command)
            return redirect('home')
    else:
        form = CreateRuleForm()

    return render(request, 'create_rule.html', {'form': form})



def view_rule(request,pk):
    rule = get_object_or_404(Rule, pk=pk)
    if request.method == 'POST':
        rupdate = Rule.objects.get(pk=pk)
        updateform = CreateRuleForm(request.POST,instance=rupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect('home')
    else:
        form = ViewRuleForm(iid=rule.id,iname=rule.name, itype=rule.type, idescription=rule.description, ialert=rule.alert,
                            iindex=rule.index, icommand=rule.command, ifilter=rule.filter,inum=rule.num_events)

    return render(request, 'view_rule.html', {'form': form, 'rule': rule})

def delete_rule(request,pk):
    rdelete = get_object_or_404(Rule, pk=pk)
    rdelete.delete()
    rulefile =  rdelete.name + '.yaml'
    os.remove(rulefile)
    return redirect('home')

def run_rule(request,pk):
    rrun = get_object_or_404(Rule, pk=pk)
    rulename = rrun.name + '.yaml'
    os.system("python -m elastalert.elastalert --rule "+rulename)


