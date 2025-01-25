def mask_account_card(account_number):
    if len(account_number) != 16:
        return "Invalid card number"
    return f"{account_number[:12]}**** {account_number[-4:]}"
