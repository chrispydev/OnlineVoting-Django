from django.shortcuts import render, redirect, reverse
from .email_backend import EmailBackend
from django.contrib import messages
from .forms import CustomUserForm
from voting.forms import VoterForm
from django.contrib.auth import login, logout
import random

# Create your views here.
VALID_UVCS = [
    "HH64FWPE",
    "BBMNS9ZJ",
    "KYMK9PUH",
    "WL3K3YPT",
    "JA9WCMAS",
    "Z93G7PN9",
    "WPC5GEHA",
    "RXLNLTA6",
    "7XUFD78Y",
    "DBP4GQBQ",
    "ZSRBTK9S",
    "B7DMPWCQ",
    "YADA47RL",
    "9GTZQNKB",
    "KSM9NB5L",
    "BQCRWTSG",
    "ML5NSKKG",
    "D5BG6FDH",
    "2LJFM6PM",
    "38NWLPY3",
    "2TEHRTHJ",
    "G994LD9T",
    "Q452KVQE",
    "75NKUXAH",
    "DHKVCU8T",
    "TH9A6HUB",
    "2E5BHT5R",
    "556JTA32",
    "LUFKZAHW",
    "DBAD57ZR",
    "K96JNSXY",
    "PFXB8QXM",
    "8TEXF2HD",
    "N6HBFD2X",
    "K3EVS3NM",
    "5492AC6V",
    "U5LGC65X",
    "BKMKJN5S",
    "JF2QD3UF",
    "NW9ETHS7",
    "VFBH8W6W",
    "7983XU4M",
    "2GYDT5D3",
    "LVTFN8G5",
    "UNP4A5T7",
    "UMT3RLVS",
    "TZZZCJV8",
    "UVE5M7FR",
    "W44QP7XJ",
    "9FCV9RMT",
]


# accout Login
def account_login(request):
    if request.user.is_authenticated:
        if request.user.user_type == "1":
            return redirect(reverse("adminDashboard"))
        else:
            return redirect(reverse("voterDashboard"))

    if request.method == "POST":
        user = EmailBackend.authenticate(
            request,
            username=request.POST.get("email"),
            password=request.POST.get("password"),
        )
        if user != None:
            login(request, user)
            if user.user_type == "1":
                return redirect(reverse("adminDashboard"))
            else:
                return redirect(reverse("voterDashboard"))
        else:
            messages.error(request, "Invalid details")
            return redirect("/")
    context = {}

    return render(request, "voting/login.html", context)


# register Page

# def account_register(request):
#     userForm = CustomUserForm(request.POST or None)
#     voterForm = VoterForm(request.POST or None)

#     if request.method == "POST":
#         if userForm.is_valid() and voterForm.is_valid():
#             user = userForm.save(commit=False)
#             voter = voterForm.save(commit=False)
#             voter.admin = user
#             user.save()
#             voter.save()
#             messages.success(request, "Account created. You can login now!")
#             return redirect(reverse("account_login"))
#         else:
#             messages.error(request, "Provided data failed validation")


#     context = {"form1": userForm, "form2": voterForm}
#     return render(request, "voting/reg.html", context)
def account_register(request):
    userForm = CustomUserForm(request.POST or None)
    voterForm = VoterForm(request.POST or None)

    if request.method == "POST":
        uvc = request.POST.get("uvc")

        # Check if the entered UVC is valid
        if uvc not in VALID_UVCS:
            messages.error(request, "Invalid UVC. Please enter a valid UVC.")
            return redirect(reverse("account_register"))

        if userForm.is_valid() and voterForm.is_valid():
            user = userForm.save(commit=False)
            voter = voterForm.save(commit=False)
            voter.admin = user
            voter.uvc = uvc  # Save the UVC to the voter
            user.save()
            voter.save()
            messages.success(request, "Account created. You can login now!")
            return redirect(reverse("account_login"))
        else:
            messages.error(request, "Provided data failed validation")

    context = {"form1": userForm, "form2": voterForm}
    return render(request, "voting/reg.html", context)


def account_logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        messages.success(request, "Thank you for visiting us!")
    else:
        messages.error(request, "You need to be logged in to perform this action")

    return redirect(reverse("account_login"))
