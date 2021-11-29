from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.contrib.auth.models import User , auth
from main_app.models import patient , doctor
from datetime import datetime
import json
from web3 import Web3
import ipfshttpclient
client=ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
# Create your views here.
patient_list=[]
doctor_list=[]
public_key="0x7201d435280b3365718DaBe98Df78c70A16206Bc"
private_key="584175c9c0f46b672e29420179c72fecfa3ddd9478bc00da46b9ea6bdaf098ea"

url='https://ropsten.infura.io/v3/67ceab9d2ad04104a3c36665374c2a15'

web3=Web3(Web3.HTTPProvider(url))

address = web3.toChecksumAddress('0xc65bab8229d53119A324747CA67644206F769980')

abi=json.loads('''[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "username",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "email",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "age",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "addres",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "mobile",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "registrationNo",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "qualification",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "password",
				"type": "string"
			}
		],
		"name": "newDoctorCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "username",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "email",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "age",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "addres",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "mobile",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "password",
				"type": "string"
			}
		],
		"name": "newPatientCreated",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "doctorCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "doctorList",
		"outputs": [
			{
				"internalType": "string",
				"name": "username",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "email",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "age",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "addres",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "mobile",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "registrationNo",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "qualification",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "password",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "patientList",
		"outputs": [
			{
				"internalType": "string",
				"name": "username",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "email",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "age",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "addres",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "mobile",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "password",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "pidCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_username",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_email",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_age",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_addres",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_mobile",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_registraionNo",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_qualification",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_password",
				"type": "string"
			}
		],
		"name": "setDoctorData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_username",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_email",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_age",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_addres",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_mobile",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_password",
				"type": "string"
			}
		],
		"name": "setPatientData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]''')

contract = web3.eth.contract(address=address,abi=abi)


def logout(request):
    auth.logout(request)
    request.session.pop('patientid', None)
    request.session.pop('doctorid', None)
    request.session.pop('adminid', None)
    return render(request,'homepage/index.html')




def sign_in_admin(request):
  

    if request.method == 'POST':

          username =  request.POST.get('username')
          password =  request.POST.get('password')
 
          user = auth.authenticate(username=username,password=password)

          if user is not None :
             
              try:
                 if ( user.is_superuser == True ) :
                     auth.login(request,user)

                     return redirect('admin_ui')
               
              except :
                  messages.info(request,'Please enter the correct username and password for a admin account.')
                  return redirect('sign_in_admin')


          else :
             messages.info(request,'Please enter the correct username and password for a admin account.')
             return redirect('sign_in_admin')


    else :
      return render(request,'admin/signin/signin.html')

def setup_client():
    web3.eth.defaultAccount='0x7201d435280b3365718DaBe98Df78c70A16206Bc'
    nonce = web3.eth.getTransactionCount(web3.eth.defaultAccount)
    tx={
    'to':'0x502b253db108BCBEaC7ca288E825D1946a0DCB0B',
    'nonce': nonce,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
    }
    sign_transaction=web3.eth.account.signTransaction(tx,'584175c9c0f46b672e29420179c72fecfa3ddd9478bc00da46b9ea6bdaf098ea')
    balance=web3.eth.getBalance('0x7201d435280b3365718DaBe98Df78c70A16206Bc')

def signup_patient(request):


    if request.method == 'POST':
      
      if request.POST['email'] and  request.POST['name'] and request.POST['dob'] and request.POST['gender'] and request.POST['address']and request.POST['mobile']and request.POST['password']and request.POST['password1'] :

          email =  request.POST['email']
          age=request.POST['age']
          name =  request.POST['name']
          dob =  request.POST['dob']
          gender =  request.POST['gender']
          address =  request.POST['address']
          mobile_no = request.POST['mobile']
          password =  request.POST.get('password')
          password1 =  request.POST.get('password1')

          if password == password1:
              if User.objects.filter(email = email).exists():
                messages.info(request,'email already taken')
                return redirect('signup_patient')
                
              else :
                lst=[name,email,password]
                username=client.add_json(lst)
                contract.functions.setPatientData(username,name,email,int(age),address,int(mobile_no),password).call()
                setup_client()
                user = User.objects.create_user(username=username,password=password,email=email)   
                user.save()
                
                patientnew = patient(user=user,name=name,dob=dob,gender=gender,address=address,mobile_no=mobile_no)
                patientnew.save()
                patient_list.append(username)
                messages.info(request,["Your username is: ",username])

              return redirect('sign_in_patient')

          else:
            messages.info(request,'password not matching, please try again')
            return redirect('signup_patient')

      else :
        messages.info(request,'Please make sure all required fields are filled out correctly')
        return redirect('signup_patient') 


    
    else :
      return render(request,'patient/signup_Form/signup.html')



def sign_in_patient(request):
  

    if request.method == 'POST':

          username =  request.POST.get('username')
          password =  request.POST.get('password')
          if username in patient_list:
              name,email,password=client.get_json(username)			   
          user = auth.authenticate(username=username,password=password)
          
          if user is not None :
             
              try:
                 if ( user.patient.is_patient == True ) :
                     auth.login(request,user)

                     request.session['patientusername'] = user.username

                     return redirect('patient_ui')
               
              except :
                  messages.info(request,'invalid credentials')
                  return redirect('sign_in_patient')


          else :
             messages.info(request,'invalid credentials')
             return redirect('sign_in_patient')


    else :
      return render(request,'patient/signin_page/index.html')


def savepdata(request,patientusername):

  if request.method == 'POST':
    name =  request.POST['name']
    mobile_no=request.POST['mobile_no']
    dob =  request.POST['dob']
    gender =  request.POST['gender']
    address =  request.POST['address']
    dobdate = datetime.strptime(dob,'%Y-%m-%d')
    puser = User.objects.get(username=patientusername)

    patient.objects.filter(pk=puser.patient).update(name=name,dob=dobdate,gender=gender,address=address,mobile_no=mobile_no)

    return redirect('pviewprofile',patientusername)





#doctors account...........operations......
    

def signup_doctor(request):

    if request.method == 'GET':
    
       return render(request,'doctor/signup_Form/signup.html')


    if request.method == 'POST':
      
      if request.POST['email'] and  request.POST['name'] and request.POST['dob'] and request.POST['gender'] and request.POST['address']and request.POST['mobile'] and request.POST['password']and request.POST['password1']  and  request.POST['registration_no'] and  request.POST['year_of_registration'] and  request.POST['qualification'] and  request.POST['specialization'] :

          email =  request.POST['email']
          name =  request.POST['name']
          age=request.POST['age']
          dob =  request.POST['dob']
          gender =  request.POST['gender']
          address =  request.POST['address']
          mobile_no = request.POST['mobile']
          registration_no =  request.POST['registration_no']
          year_of_registration =  request.POST['year_of_registration']
          qualification =  request.POST['qualification']
          specialization =  request.POST['specialization']

          password =  request.POST.get('password')
          password1 =  request.POST.get('password1')

          if password == password1:
              if User.objects.filter(email = email).exists():
                messages.info(request,'email already taken')
                return redirect('signup_doctor')
                
              else :
                lst=[name,email,password,registration_no]
                username=client.add_json(lst)
                contract.functions.setDoctorData(username,name,email,int(age),address,int(mobile_no),int(registration_no),'we',qualification,password).call()
                user = User.objects.create_user(username=username,password=password,email=email)   
                user.save()
                doctornew = doctor( user=user, name=name, dob=dob, gender=gender, address=address, mobile_no=mobile_no, registration_no=registration_no, year_of_registration=year_of_registration, qualification=qualification, specialization=specialization )
                doctornew.save()
                doctor_list.apped(username)
                messages.info(request,('Your Username is: ',username))
                print("doctorcreated")
                
              return redirect('sign_in_doctor')

          else:
            messages.info(request,'password not matching, please try again')
            return redirect('signup_doctor')

      else :
        messages.info(request,'Please make sure all required fields are filled out correctly')
        return redirect('signup_doctor') 






def sign_in_doctor(request):

    if request.method == 'GET':
    
       return render(request,'doctor/signin_page/index.html')

  
    if request.method == 'POST':

          username =  request.POST.get('username')
          password =  request.POST.get('password')
          if username in doctor_list: 
              name,email,password,registration_no=client.get_json(username)
          user = auth.authenticate(username=username,password=password)

          if user is not None :
              
              try:

                if ( user.doctor.is_doctor == True ) :
                  auth.login(request,user)
                  
                  request.session['doctorusername'] = user.username

                  return redirect('doctor_ui')
               
              except :
                  messages.info(request,'invalid credentials')
                  return redirect('sign_in_doctor')

          else :
             messages.info(request,'invalid credentials')
             return redirect('sign_in_doctor')


    else :
      return render(request,'doctor/signin_page/index.html')





def saveddata(request,doctorusername):

  if request.method == 'POST':

    name =  request.POST['name']
    dob =  request.POST['dob']
    gender =  request.POST['gender']
    address =  request.POST['address']
    mobile_no = request.POST['mobile_no']
    registration_no =  request.POST['registration_no']
    year_of_registration =  request.POST['year_of_registration']
    qualification =  request.POST['qualification']
    specialization =  request.POST['specialization']
    

    
    dobdate = datetime.strptime(dob,'%Y-%m-%d')
    yor = datetime.strptime(year_of_registration,'%Y-%m-%d')

    duser = User.objects.get(username=doctorusername)

    doctor.objects.filter(pk=duser.doctor).update( name=name, dob=dob, gender=gender, address=address, mobile_no=mobile_no, registration_no=registration_no, year_of_registration=yor, qualification=qualification, State_Medical_Council=State_Medical_Council, specialization=specialization )

    return redirect('dviewprofile',doctorusername)

