# from django import forms

# HOSTEL_CHOICES = [
#     ("Mfumbiro Hostels", "Mfumbiro Hostels"),
#     ("Nyayo Hostels", "Nyayo Hostels"),
#     ("Nyandarua Hostels", "Nyandarua Hostels"),
#     ("New Menengai Hostels", "New Menengai Hostels"),
#     ("New Ruwenzori Hostels", "New Ruwenzori Hostels"),
#     ("Usambara Hostels", "Usambara Hostels"),
#     ("Longonot Hostels", "Longonot Hostels"),
#     ("Kilimambogo Hostels", "Kilimambogo Hostels"),
#     ("Chania Hostels", "Chania Hostels"),
#     ("Tana Hostels", "Tana Hostels"),
#     ("New Menengai Hostels", "New Menengai Hostels"),
#     ("New Aberdares Hostels", "New Aberdares Hostels"),
#     ("Old Aberdares Hostels", "Old Aberdares Hostels"),
#     ("Ngong Hostels", "Ngong Hostels"),
#     ("Old Ruwenzori Hostels", "Old Ruwenzori Hostels"),
#     ("Usambara Hostels", "Usambara Hostels"),
#     ("Lukenya Hostels", "Lukenya Hostels"),
#     ("Athi Hostels", "Athi Hostels"),
#     ("Tana Hostels", "Tana Hostels"),
# ]



# from django import forms

# class HostelApplicationForm(forms.Form):
#     HOSTEL_TYPE_COST = {
#         'Single Room': 12000,
#         'Double Room': 10000,
#         'Triple Room': 9000,
#         'Quadruple Room': 8800,
#         'Quintuple Room': 8000,
#         'Sextuple Room': 7600,
#     }

#     YEAR_CHOICES = [
#         ('Year One', 'Year One'),
#         ('Year Two', 'Year Two'),
#         ('Year Three', 'Year Three'),
#         ('Year Four', 'Year Four'),
#         ('Year Five', 'Year Five'),
#         ('Year Six', 'Year Six'),
#     ]

#     name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     reg_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     year_of_study = forms.ChoiceField(choices=YEAR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
#     gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.Select(attrs={'class': 'form-control'}))
#     hostel_type = forms.ChoiceField(
#         choices=list(HOSTEL_TYPE_COST.items()), 
#         widget=forms.Select(attrs={'class': 'form-control', 'onchange': 'updateCost()'})
#     )
#     location = forms.ChoiceField(choices=[('On-campus', 'On-campus'), ('Off-campus', 'Off-campus')], widget=forms.Select(attrs={'class': 'form-control'}))
#     hostel_name = forms.MultipleChoiceField(choices=HOSTEL_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))

#     cost_per_semester = forms.DecimalField(widget=forms.HiddenInput(), required=False)

#     def clean(self):
#         cleaned_data = super().clean()
#         hostel_type = cleaned_data.get("hostel_type")
#         cleaned_data["cost_per_semester"] = self.HOSTEL_TYPE_COST.get(hostel_type, 0)  # Set cost dynamically
#         return cleaned_data





from django import forms

HOSTEL_CHOICES = [
    ("Mfumbiro Hostels", "Mfumbiro Hostels"),
    ("Nyayo Hostels", "Nyayo Hostels"),
    ("Nyandarua Hostels", "Nyandarua Hostels"),
    ("New Menengai Hostels", "New Menengai Hostels"),
    ("New Ruwenzori Hostels", "New Ruwenzori Hostels"),
    ("Usambara Hostels", "Usambara Hostels"),
    ("Longonot Hostels", "Longonot Hostels"),
    ("Kilimambogo Hostels", "Kilimambogo Hostels"),
    ("Chania Hostels", "Chania Hostels"),
    ("Tana Hostels", "Tana Hostels"),
    ("New Aberdares Hostels", "New Aberdares Hostels"),
    ("Old Aberdares Hostels", "Old Aberdares Hostels"),
    ("Ngong Hostels", "Ngong Hostels"),
    ("Old Ruwenzori Hostels", "Old Ruwenzori Hostels"),
    ("Lukenya Hostels", "Lukenya Hostels"),
    ("Athi Hostels", "Athi Hostels"),
]

class HostelApplicationForm(forms.Form):
    HOSTEL_TYPE_COST = {
        'Single Room': 12000,
        'Double Room': 10000,
        'Triple Room': 9000,
        'Quadruple Room': 8800,
        'Quintuple Room': 8000,
        'Sextuple Room': 7600,
    }

    YEAR_CHOICES = [
        ('Year One', 'Year One'),
        ('Year Two', 'Year Two'),
        ('Year Three', 'Year Three'),
        ('Year Four', 'Year Four'),
        ('Year Five', 'Year Five'),
        ('Year Six', 'Year Six'),
    ]

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    reg_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    year_of_study = forms.ChoiceField(
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='Year One'  # Set default placeholder
    )
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.Select(attrs={'class': 'form-control'}))
    hostel_type = forms.ChoiceField(
        choices=[(key, key) for key in HOSTEL_TYPE_COST.keys()], 
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_hostel_type'})
    )
    location = forms.ChoiceField(choices=[('On-campus', 'On-campus'), ('Off-campus', 'Off-campus')], widget=forms.Select(attrs={'class': 'form-control'}))
    hostel_name = forms.MultipleChoiceField(choices=HOSTEL_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))

    cost_per_semester = forms.DecimalField(widget=forms.HiddenInput(), required=False)

    def clean(self):
        cleaned_data = super().clean()
        hostel_type = cleaned_data.get("hostel_type")
        cleaned_data["cost_per_semester"] = self.HOSTEL_TYPE_COST.get(hostel_type, 0)  
        return cleaned_data