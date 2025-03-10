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
    ("New Menengai Hostels", "New Menengai Hostels"),
    ("New Aberdares Hostels", "New Aberdares Hostels"),
    ("Old Aberdares Hostels", "Old Aberdares Hostels"),
    ("Ngong Hostels", "Ngong Hostels"),
    ("Old Ruwenzori Hostels", "Old Ruwenzori Hostels"),
    ("Usambara Hostels", "Usambara Hostels"),
    ("Lukenya Hostels", "Lukenya Hostels"),
    ("Athi Hostels", "Athi Hostels"),
    ("Tana Hostels", "Tana Hostels"),
]



from django import forms

class HostelApplicationForm(forms.Form):
    HOSTEL_TYPE_COST = {
        'Single Room': 12000,
        'Double Room': 10000,
        'Triple Room': 9000,
        'Quadruple Room': 8800,
        'Quintuple Room': 8000,
        'Sextuple Room': 7600,
    }

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    reg_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    year_of_study = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.Select(attrs={'class': 'form-control'}))
    hostel_type = forms.ChoiceField(
        choices=list(HOSTEL_TYPE_COST.items()),  # Choices from dictionary keys
        widget=forms.Select(attrs={'class': 'form-control', 'onchange': 'updateCost()'})
    )
    location = forms.ChoiceField(choices=[('On-campus', 'On-campus'), ('Off-campus', 'Off-campus')], widget=forms.Select(attrs={'class': 'form-control'}))
    hostel_name = forms.MultipleChoiceField(choices=HOSTEL_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))

    # ✅ Add cost_per_semester as a hidden field
    cost_per_semester = forms.DecimalField(widget=forms.HiddenInput(), required=False)

    def clean(self):
        cleaned_data = super().clean()
        hostel_type = cleaned_data.get("hostel_type")
        cleaned_data["cost_per_semester"] = self.HOSTEL_TYPE_COST.get(hostel_type, 0)  # Set cost dynamically
        return cleaned_data





# class HostelApplicationForm(forms.Form):
#     HOSTEL_TYPE_COST = {
#         'Single Room': 12000,
#         'Double Room': 10000,
#         'Triple Room': 9000,
#         'Quadruple Room': 8800,
#         'Quintuple Room': 8000,
#         'Sextuple Room': 7600,
#     }

#     name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     reg_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     year_of_study = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.Select(attrs={'class': 'form-control'}))
#     hostel_type = forms.ChoiceField(
#         choices=list(HOSTEL_TYPE_COST.items()),  # Choices from dictionary keys
#         widget=forms.Select(attrs={'class': 'form-control', 'onchange': 'updateCost()'})
#     )
#     location = forms.ChoiceField(choices=[('On-campus', 'On-campus'), ('Off-campus', 'Off-campus')], widget=forms.Select(attrs={'class': 'form-control'}))
#     hostel_name = forms.MultipleChoiceField(choices=HOSTEL_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))

#     def clean(self):
#         cleaned_data = super().clean()
#         hostel_type = cleaned_data.get("hostel_type")
#         cleaned_data["cost_per_semester"] = self.HOSTEL_TYPE_COST.get(hostel_type, 0)  # Set cost dynamically
#         return cleaned_data







# class HostelApplicationForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    reg_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    year_of_study = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.Select(attrs={'class': 'form-control'}))
    hostel_type = forms.ChoiceField(
        choices=[
            ('Single Room', 'Single Room'),
            ('Double Room', 'Double Room'),
            ('Triple Room', 'Triple Room'),
            ('Quadruple Room', 'Quadruple Room'),
            ('Quintuple Room', 'Quintuple Room'),
            ('Sextuple Room', 'Sextuple Room'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    location = forms.ChoiceField(choices=[('On-campus', 'On-campus'), ('Off-campus', 'Off-campus')], widget=forms.Select(attrs={'class': 'form-control'}))
    hostel_name = forms.MultipleChoiceField(choices=HOSTEL_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    cost_per_semester = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))