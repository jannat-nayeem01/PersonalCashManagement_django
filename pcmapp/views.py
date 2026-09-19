from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegistrationForm,LoginForm,AddCashForm,ExpenseForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum



def registration(request):
    if(request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'Registration Successful')
            return redirect('loginview')
            
    form = RegistrationForm()
    return render(request,'registration.html',{'form':form})
def loginview(request):
    if(request.method == 'POST'):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, 'Login successful.')
                return redirect('profile')
    form = LoginForm()
    return render(request,'login.html',{'form':form})

def logoutview(request):
    user = request.user
    logout(request,user)
    return redirect('Logged Out Successfully')

@login_required
def profile(request):
    return render(request,'profile.html',{'user':request.user})


@login_required
def transaction(request):
    cash_entries = AddCash.objects.filter(user=request.user)
    cash_result = cash_entries.aggregate(total=Sum('amount'))
    total_cash = cash_result['total'] or 0

    expense_entries = Expense.objects.filter(user=request.user)
    expense_result = expense_entries.aggregate(total=Sum('amount'))
    total_expense = expense_result['total'] or 0

    available_balance = total_cash - total_expense

    cash_form = AddCashForm(prefix='cash')
    expense_form = ExpenseForm(prefix='expense')
    expense_form.fields['amount'].widget.attrs['placeholder'] = f'Available balance: ৳{available_balance}'

    if request.method == 'POST':
        if request.POST.get('form_type') == 'cash':
            cash_form = AddCashForm(request.POST, prefix='cash')
            if cash_form.is_valid():
                cash = cash_form.save(commit=False)
                cash.user = request.user
                cash.save()
                messages.success(request, 'Cash Added Successfully')
                return redirect('transaction')

        elif request.POST.get('form_type') == 'expense':
            expense_form = ExpenseForm(request.POST, prefix='expense')
            expense_form.fields['amount'].widget.attrs['placeholder'] = f'Available balance: ৳{available_balance}'

            if expense_form.is_valid():
                new_expense_amount = expense_form.cleaned_data['amount']

                if new_expense_amount > available_balance:
                    messages.error(
                        request,
                        f'Insufficient balance. Available: ৳{available_balance}, Attempted: ৳{new_expense_amount}'
                    )
                else:
                    expense = expense_form.save(commit=False)
                    expense.user = request.user
                    expense.save()
                    messages.success(request, 'Expense Added Successfully')
                    return redirect('transaction')

    return render(request, 'transaction.html', {
        'cash_form': cash_form,
        'expense_form': expense_form,
        'available_balance': available_balance,
    })
def dashboard(request):
    user = request.user
    cash_entries = AddCash.objects.filter(user=request.user)
    cash_result = cash_entries.aggregate(total=Sum('amount'))
    total_cash = cash_result['total'] or 0
    expense_entries = Expense.objects.filter(user=user)
    expense_result = expense_entries.aggregate(total=Sum('amount'))
    total_expense = expense_result['total'] or 0
    
    balance = total_cash-total_expense
    context = {
        'total_cash': total_cash,
        'total_expense': total_expense,
        'balance': balance,
    }


    return render(request,'dashboard.html',context=context)

