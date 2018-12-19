<<<<<<< HEAD
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from myaccount.forms import SignupForm, LoginForm
from myaccount.models import Myuser
from django.contrib.auth.decorators import login_required
=======
from django.http import HttpResponse
from django.shortcuts import render
from myaccount.models import Myuser
from theory.models import Semester,Syllabus,OldQuestion,Year,Note,Solution
>>>>>>> 794b9fcd06e90d7bc2734af66bd8544f20384baf

def home(request):
    context={
    'sem':Semester.objects.all(),
    }
    return render(request,'index.html',context)


def dashboard(request):
    context={
    # 'user': Myuser.objects.get(Myuser_id=request.user.id)
    }
    return render(request,'dashboard.html',context)

def question(request):
    return render(request,'question.html')


def syllabus(request):
    context={
    'sem':Semester.objects.all()
    }
    return render(request,'syllabus.html',context)


def syllabus_detail(request,id):
    context={
    'sem':Semester.objects.all(),
    's': Semester.objects.get(pk=id),
    'sy': Syllabus.objects.filter(sem_id=id)
    }
    return render(request,'sy_detail.html',context)



def old_questions(request):
    context={
    'sem':Semester.objects.all()
    }
    return render(request,'oldquestions.html',context)

def oldquestions_detail(request,id):
    context={
    'sem':Semester.objects.all(),
    's': Semester.objects.get(pk=id),
    'year':Year.objects.all()
    }
    return render(request,'sy_detail.html',context)


def oldquestions_sub(request,id):
    context={
    'sem':Semester.objects.all(),
    'old': OldQuestion.objects.filter(year_id=id),
    'y':Year.objects.get(pk=id)
    }
    return render(request,'sy_detail.html',context)



def notes(request):
    context={
    'sem':Semester.objects.all()
    }
    return render(request,'notes.html',context)


def notes_details(request,id):
    context={
    'sem':Semester.objects.all(),
    's': Semester.objects.get(pk=id),
    'note':Note.objects.filter(sem_id=id),
    }
    return render(request,'sy_detail.html',context)


def solutions(request):
    context={
    'sem':Semester.objects.all()
    }
    return render(request,'solution.html',context)

def solutions_detail(request,id):
    context={
    'sem':Semester.objects.all(),
    's': Semester.objects.get(pk=id),
    'yr':Year.objects.all()
    }
    return render(request,'sy_detail.html',context)

def solutions_sub(request,id):
    context={
    'sem':Semester.objects.all(),
    'sol': Solution.objects.filter(year_id=id),
    'y':Year.objects.get(pk=id),
    's': Semester.objects.get(pk=id)
    }
<<<<<<< HEAD
    return render(request,'index.html')


def signup(request):
    if request.method=='GET':
        context={
        'form': SignupForm(),
        }
        return render(request,'signup.html',context)
    else:
        form=SignupForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # username=request.POST.get('username')
                # password=request.POST.get('password')
                # print("asdfsdaf")
                # user=authenticate(username=username,password=password)
                # print("sagn")
                return redirect('login')
                # if password==re_password:
                #     form.save()
                #     return redirect('login')
                # else:
                #     return render(request,'signup.html',{'form':form,'errmsg':'Password field didnt match.'})

            except:
                return render(request,'signup.html',{'form':form,'errmsg':'Something went worng dsafsdfsdW'})
        else:
            return render(request,'signup.html',{'form':form,'errmsg':'Something went worng'})

def login(request):
    if request.method=='GET':
        context={
        'form':LoginForm(),
        }
        return render(request,'login.html',context)
    else:
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            try:
                username=request.POST.get('username')
                password=request.POST.get('password')
                user=authenticate(username=username,password=password)
                if user is not none:
                    return render(request,'user_dashboard.html')
                else:
                    return render(request,'login.html',{'errmsg':'Something went wrong with your login'})
                # all_users=Myuser.objects.all()
                # for x in all_users:
                #     if (x.username != username):
                #         continue
                #         # return render(request,'login.html',{'form':LoginForm(),'errmsg': 'Username is wrong'})
                #     else:
                #         if (x.password != password):
                #             return render(request,'login.html',{'form':LoginForm(),'errmsg': 'Password is wrong'})
                #         else:
                #             return redirect('dashboard')
                #             break
                # return render(request,'login.html',{'form':LoginForm(),'errmsg': 'Username and password is wrong'})

            except:
                return render(request,'login.html',{'form':LoginForm(),'errmsg':'Something went wrong'})

        else:
            return render(request,'login.html',{'form':LoginForm(),'errmsg':'Something went wrong with your login'})


# @login_required(login_url='/login/')
# def user_dashboard(request):
#     print(request.user.is_authenticated())
#     if request.user.is_authenticated():
#         if request.method=='GET':
#             print(request.user.username)
#             context={
#             'detail':Myuser.objects.get(username=request.user.username)
#             }
#             return render(request,'user_dashboard.html',context)
#         else:
#             pass
#     else:
#         return redirect('home')
=======
    return render(request,'sy_detail.html',context)
>>>>>>> 794b9fcd06e90d7bc2734af66bd8544f20384baf
