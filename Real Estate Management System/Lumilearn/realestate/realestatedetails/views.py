from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import RealEstate,details,sellers,plotsDetails,bi,plotinfo,client_req
from django.contrib import messages


def LoginForm(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['user_pass']
        role = request.POST['role']

        try:
            user = RealEstate.objects.get(username=username)
            if user.role == role:
                if user.password == password:
                    if role == 'User':
                        return redirect('user_home')
                    elif role == 'Admin':
                        return redirect('admin_home')
                    else:
                        messages.error(request, 'Invalid role selected')
                else:
                    messages.error(request, 'Invalid password')
            else:
                messages.error(request, f'The selected role does not match the registered role ({user.role})')
        except RealEstate.DoesNotExist:
            messages.error(request, 'You have not registered yet')

    return render(request, 'LoginForm.html')# Create your views here.
def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']
        contact_No = request.POST['contactNo']
        role= request.POST['role']
        if password != confirm_password:
            messages.error(request,'Passwords do not match')
        else:

            RealEstate.objects.create(
            username = username,
            password = password,
            confirm_password = confirm_password,
            contact_no = contact_No,
            email = email,
            role = role,
            )
            return redirect('LoginForm')
    return render(request, 'Register.html')

def User(request):
    return render(request, 'User.html')

def Admin(request):
    return render(request, 'Admin.html')


def Client(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        father_name = request.POST.get('father_name', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        qualification = request.POST.get('qualification', '')
        occupation = request.POST.get('occupation', '')
        mobile = request.POST.get('mobile', '')
        email = request.POST.get('email', '')
        account_no = request.POST.get('account_no', '')
        ifsc_code = request.POST.get('ifsc_code', '')
        bank_name = request.POST.get('bank_name', '')
        branch_name = request.POST.get('branch_name', '')
        plots_purchased = request.POST.get('plots_purchased', '')
        details.objects.create(
        name = name,
        father_name = father_name,
        age = age,
        gender = gender,
        address = address,
        qualification = qualification,
        occupation = occupation,
        mobile = mobile,
        email = email,
        account_no = account_no,
        ifsc_code = ifsc_code,
        bank_name = bank_name,
        branch_name = branch_name,
        plots_purchased = plots_purchased,
        )
        return redirect('client_details')
    return render(request, 'Client Reg.html')

def client_details(request):
    run=details.objects.all()
    return render(request, 'client_details.html',{'run':run})

def Seller(request):
    if request.method == 'POST':
        company_name=request.POST['company_name']
        gst_number=request.POST['gst_number']
        address=request.POST['address']
        contact_no=request.POST['contact_no']
        email=request.POST['email']
        sellers.objects.create(
        company_name=company_name,
        gst_number=gst_number,
        address=address,
        contact_no=contact_no,
        email=email,
        )
        return redirect('seller_details')
    return render(request, 'Seller Reg.html')

def seller_details(request):
    fun=sellers.objects.all()
    return render(request, 'seller_details.html',{'fun':fun})

def PlotDetails(request):
    if request.method == 'POST':
        area_name=request.POST['area_name']
        No_of_plots=request.POST['No_of_plots']
        square_feet_rate=request.POST['square_feet_rate']
        amenities = request.POST.getlist('amenities')
        Amenities = ', '.join(amenities)
        plotsDetails.objects.create(
            area_name=area_name,
            No_of_plots=No_of_plots,
            square_feet_rate=square_feet_rate,
            amenities=Amenities,
        )
        return redirect('display_plotdetails')
    return render(request, 'PlotDetails.html')

def display_plotdetails(request):
  gun = plotsDetails.objects.all()  # Use 'plots' for better readability
  return render(request,'display_plotdetails.html',{'gun': gun})

def BI(request):
    if request.method == 'POST':
        client_name=request.POST['client_name']
        contact_no=request.POST['contact_no']
        area_name=request.POST['area_name']
        booked_amount=request.POST['booked_amount']
        reg_amt=request.POST['reg_amt']
        reg_date=request.POST['reg_date']
        bi.objects.create(
            client_name=client_name,
            contact_no=contact_no,
            area_name=area_name,
            booked_amount=booked_amount,
            reg_amt=reg_amt,
            reg_date=reg_date,
        )
        return redirect('display_bi')
    return render(request, 'BI.html')

def display_bi(request):
    done=bi.objects.all()
    return render(request,'display_bi.html',{'done':done})


def Plotinfo(request):
    if request.method == 'POST':
        area_name = request.POST['area_name']
        No_of_plots = request.POST['No_of_plots']
        square_feet_rate = request.POST['square_feet_rate']
        amenities = request.POST.getlist('amenities')
        Amenities = ', '.join(amenities)  # Join the amenities into a single string

        plotinfo.objects.create(
            area_name=area_name,
            No_of_plots=No_of_plots,
            square_feet_rate=square_feet_rate,
            Amenities=Amenities,
        )
        return redirect('display_plotinfo')
    return render(request, 'Plotinfo.html')

def display_plotinfo(request):
    king = plotinfo.objects.all()
    return render(request, 'display_plotinfo.html', {'king': king})
def Viewed(request):
    if request.method == 'POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        plot_seen=request.POST['plot_seen']
        amount_Details=request.POST['amount_Details']
        requirements=request.POST['requirements']
        client_req.objects.create(
            name=name,
            mobile=mobile,
            email=email,
            plot_seen=plot_seen,
            amount_Details=amount_Details,
            requirements=requirements,
        )
        return redirect('display_viewed')
    return render(request, 'Viewed.html')

def display_viewed(request):
    son=client_req.objects.all()
    return render(request,'display_viewed.html',{'son':son})
