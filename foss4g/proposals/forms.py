from django import forms
from django.utils.safestring import mark_safe

from .models import TalkProposal, WorkshopProposal


class ProposalForm(forms.ModelForm):

    def clean_description(self):
        value = self.cleaned_data["description"]
        if len(value) > 400:
            raise forms.ValidationError(
                u"The description must be less than 400 characters"
            )
        return value


class TalkProposalForm(ProposalForm):

    class Meta:
        FOOTNOTE = '<sup><a href="#fn1" title="Open source definition">1</a></sup>'

        model = TalkProposal
        fields = [
            "title",
            "abstract",
            "additional_notes",
            "recording_release",
            "foss_is",
            "foss_is_links",
            "foss_contributing",
            "foss_contributing_links",
            "foss_using",
            "foss_using_links",
        ]
        labels = {
            'foss_is': mark_safe(
                "This talk is about a project that is open source{}"
                .format(FOOTNOTE)),
            'foss_contributing': mark_safe(
                "This talk is about a project that is actively contributing "
                "to open source{} projects".format(FOOTNOTE)),
            'foss_using': mark_safe(
                "This talk is about a project that is using open source{}"
                .format(FOOTNOTE)),
        }
        widgets = {
          'foss_is_links': forms.Textarea(attrs={'rows': 3}),
          'foss_contributing_links': forms.Textarea(attrs={'rows': 5}),
          'foss_using_links': forms.Textarea(attrs={'rows': 5}),
        }


class WorkshopProposalForm(ProposalForm):

    class Meta:
        model = WorkshopProposal
        fields = [
            "title",
            "abstract",
            "additional_notes",
        ]