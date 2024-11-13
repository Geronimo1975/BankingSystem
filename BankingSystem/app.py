import streamlit as st
from classes.customer import Customer
from classes.saving_account import SavingAccount
from classes.current_account import CurrentAccount

# Titlul aplicației
st.title("Banking System Interface")

# Opțiuni pentru navigare
operation = st.sidebar.selectbox("Choose Operation", ["Create Account", "Deposit", "Withdraw", "View Statement"])

# Crearea unui cont nou
if operation == "Create Account":
    st.header("Create New Account")

    # Detalii cont
    username = st.text_input("Mariana")
    password = st.text_input("Password", type="password")
    phone = st.text_input("Phone Number")
    account_type = st.selectbox("Account Type", ["Saving", "Current"])

    if st.button("Create Account"):
        customer = Customer(username=username, password=password, phone=phone, account_type=account_type.lower())
        account = customer.create_account(account_type.lower())
        st.success(f"Account created successfully for {username} with account ID: {account.account_id}")

# Depunere de bani
elif operation == "Deposit":
    st.header("Deposit Funds")
    account_id = st.text_input("Account ID")
    amount = st.number_input("Amount to Deposit", min_value=0.0, step=0.1)

    if st.button("Deposit"):
        # Aici ar trebui să încarci contul pe baza `account_id` - exemplu de instanță de test
        customer = Customer(username="testuser", password="hashedpassword", phone="+1234567890", account_type="saving")
        account = customer.create_account("saving")  # Presupunem contul de economii
        account.deposit(amount)
        st.success(f"Successfully deposited {amount:.2f} EUR. New balance: {account.balance:.2f} EUR")

# Retragere de bani
elif operation == "Withdraw":
    st.header("Withdraw Funds")
    account_id = st.text_input("Account ID")
    amount = st.number_input("Amount to Withdraw", min_value=0.0, step=0.1)

    if st.button("Withdraw"):
        # Aici ar trebui să încarci contul pe baza `account_id`
        customer = Customer(username="testuser", password="hashedpassword", phone="+1234567890", account_type="saving")
        account = customer.create_account("saving")
        success = account.withdraw(amount)
        if success:
            st.success(f"Successfully withdrew {amount:.2f} EUR. New balance: {account.balance:.2f} EUR")
        else:
            st.error("Insufficient funds or invalid amount.")

# Vizualizarea extrasului de cont
elif operation == "View Statement":
    st.header("View Account Statement")
    account_id = st.text_input("Account ID")

    if st.button("Generate Statement"):
        # Aici ar trebui să încarci contul pe baza `account_id`
        customer = Customer(username="testuser", password="hashedpassword", phone="+1234567890", account_type="saving")
        account = customer.create_account("saving")
        st.subheader(f"Transaction History for Account {account_id}")
        for txn in account.transaction_history:
            st.write(f"{txn['date']}: {txn['type']} of {txn['amount']:.2f} EUR, Balance after: {txn['balance_after']:.2f} EUR")
