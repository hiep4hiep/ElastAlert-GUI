from django import forms
from .models import Rule
from datetime import datetime
from django.core.validators import RegexValidator

type_choice = [
    ('any','Match Any hit'),
    ('change','Change'),
    ('blacklist','Black List'),
    ('whitelist','White List'),
    ('frequency','Frequency'),
    ('spike','Spike'),
    ('flatline','Flat Line'),
    ('new_term','New Term'),
    ('cardinality','Cardinality'),
    ('metric_aggregation','Metric Aggregation'),
    ('spike_aggregation','Spike Aggregaion'),
    ('percentage_match','Percentage Match'),
]

index_choice = [
    ('fidelis*','Fidelis'),
    ('panos*','Palo Alto Networks'),
    ('checkpoint*','CheckPoint'),
    ('cisco*','Cisco'),
    ('forescout*','Fore Scout'),
]

alert_choice = [
    ('command','Run Shell Command'),
    ('email','Email'),
    ('slack','Slack'),
    ('servicenow','ServiceNow'),
    ('post','HTTP POST'),
    ('line','Line message'),
]


class CreateRuleForm(forms.ModelForm):
    type = forms.CharField(label='Type',
        widget=forms.Select(choices=type_choice)
    )
    index = forms.CharField(label='Index',
                           widget=forms.Select(choices=index_choice)
    )
    alert = forms.CharField(label='Alert',
                            widget=forms.Select(choices=alert_choice)
                            )
    name = forms.CharField(help_text='Name of the rule, no space',
                           validators=[RegexValidator(
                                regex=r'^[-,_\w]*$',
                                message=("Only AlphaNumerics and , - _ are allowed"),
                                )]
                           )

    class Meta:
        model = Rule
        fields = ['name','description','type',
                  'index','num_events','filter','alert','command',
                  ]

class ViewRuleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.iname = kwargs.pop('iname')
        self.itype = kwargs.pop('itype')
        self.idescription = kwargs.pop('idescription')
        self.iindex  = kwargs.pop('iindex')
        self.ifilter = kwargs.pop('ifilter')
        self.ialert = kwargs.pop('ialert')
        self.icommand = kwargs.pop('icommand')
        self.inum = kwargs.pop('inum')
        self.iid = kwargs.pop('iid')
        super(ViewRuleForm, self).__init__(*args, **kwargs)

        self.fields['id'] = forms.IntegerField(initial=str(self.iid))
        self.fields['name'] = forms.CharField(initial=str(self.iname))
        self.fields['description'] = forms.CharField(initial=str(self.idescription))
        self.fields['type'] = forms.CharField(initial=str(self.itype))
        self.fields['index'] = forms.CharField(initial=str(self.iindex))
        self.fields['filter'] = forms.CharField(initial=str(self.ifilter))
        self.fields['alert'] = forms.CharField(initial=str(self.ialert))
        self.fields['command'] = forms.CharField(initial=str(self.icommand))
        self.fields['num_events']=forms.IntegerField(initial=str(self.inum))



    class Meta:
        model = Rule
        fields = ['id','name', 'description', 'type',
                  'index', 'num_events', 'filter', 'alert', 'command',
                  ]