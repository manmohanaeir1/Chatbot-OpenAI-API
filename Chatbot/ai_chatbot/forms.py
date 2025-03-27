from django import forms
import re
import dateparser

# Chat Form
class ChatForm(forms.Form):
    message = forms.CharField(label="Ask me anything", widget=forms.Textarea(attrs={"rows": 3, "class": "form-control"}))

# Appointment Booking Form
class AppointmentForm(forms.Form):
    date_query = forms.CharField(label="Enter Date (e.g., 'Next Monday')", widget=forms.TextInput(attrs={"class": "form-control"}))

    def clean_date_query(self):
        query = self.cleaned_data["date_query"]
        parsed_date = dateparser.parse(query)

        if not parsed_date:
            raise forms.ValidationError("Invalid date format. Please enter a specific date.")

        return parsed_date.strftime("%Y-%m-%d")

# User Details Form
class UserDetailsForm(forms.Form):
    name = forms.CharField(label="Full Name", widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    phone = forms.CharField(label="Phone Number", widget=forms.TextInput(attrs={"class": "form-control"}))

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not re.match(r"^\+?\d{10,15}$", phone):
            raise forms.ValidationError("Invalid phone number format.")
        return phone
