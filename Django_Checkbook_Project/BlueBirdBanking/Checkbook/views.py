from django.shortcuts import render, redirect, get_object_or_404

from .forms import AccountForm, TransactionForm

from .models import Account, Transaction

# This function will render the Home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None) # Retrieve form
    # Checks if request method is POST
    if request.method == 'POST':
        pk =  request.POST['account'] # If the form is submitted, retrieve which account the user wants to view
        return balance(request, pk) # Call balance function to render that account's balance sheet
    content = {'form': form} # Pass content to the template in a dictionary
    # Adds content of form to page
    return render(request, 'checkbook/index.html', content)

# This function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)  # Retrieve the Account form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # Check to see if the submitted form is valid and if so, saves the form
            form.save()  # Saves new account
            return redirect('index')  # Returns user back to the home page
    content = {'form': form}  # Saves content to the template as a dictionary
    # Adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)

def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # Retrieve the requested account
    transactions = Transaction.Transactions.filter(account=pk).order_by('date')  # Retrieve all transactions for the account
    current_total = account.initial_deposit  # Start with the initial deposit

    # Add a running balance to each transaction
    for transaction in transactions:
        if transaction.type == 'Deposit':
            current_total += transaction.amount
        else:  # Withdrawal
            current_total -= transaction.amount
        transaction.balance = current_total  # Dynamically add a 'balance' attribute to each transaction

    # Pass account, total balance, and transactions to the template
    content = {'account': account, 'transactions': transactions, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# This function will render the Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # Retrieve the Transaction form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # Check to see if the submitted form is valid and if so, saves the form
            pk = request.POST['account'] # Retrieve which account the transaction was for
            form.save()  # Saves the transaction form
            return balance(request, pk) # Renders  balance of the accounts Balance Sheet
            return redirect('index')  # Redirects the user to the home page after form submission
    # Pass content to the template in a dictionary
    content = {'form': form}
    # Adds content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)

