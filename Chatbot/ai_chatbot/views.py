from django.shortcuts import render
from .forms import ChatForm, AppointmentForm, UserDetailsForm
from .utils import get_answer

# Chatbot View
def chatbot_view(request):
    response = None
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            response = get_answer(form.cleaned_data["message"])
    else:
        form = ChatForm()

    return render(request, "chatbot.html", {"form": form, "response": response})

# Appointment Booking View
def book_appointment_view(request):
    response = None
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            response = f"Your appointment is booked for {form.cleaned_data['date_query']}."
    else:
        form = AppointmentForm()

    return render(request, "book_appointment.html", {"form": form, "response": response})

# User Details View
def user_details_view(request):
    response = None
    if request.method == "POST":
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            response = f"Thank you, {form.cleaned_data['name']}! We will contact you soon."
    else:
        form = UserDetailsForm()

    return render(request, "user_details.html", {"form": form, "response": response})
