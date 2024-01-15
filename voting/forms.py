from django import forms
from .models import *
from account.forms import FormSettings


class VoterForm(FormSettings):
    class Meta:
        model = Voter
        fields = [
            "phone",
            "constituency",
            "uvc",
        ]

        # Add widgets
        widgets = {
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "constituency": forms.Select(attrs={"class": "form-control"}),
            "uvc": forms.TextInput(attrs={"class": "form-control"}),
        }

        def __init__(self, *args, **kwargs):
            super(VoterForm, self).__init__(*args, **kwargs)
            self.fields[
                "constituency"
            ].choices = Voter.CONSTITUENCY_CHOICES  # Set choices for the dropdown


class PositionForm(FormSettings):
    class Meta:
        model = Position
        fields = ["name", "max_vote"]


class CandidateForm(FormSettings):
    class Meta:
        model = Candidate
        fields = ["fullname", "bio", "position", "photo"]
