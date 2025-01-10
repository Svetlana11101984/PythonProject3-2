from widget import mask_account_card, get_date

examples = [
    "Visa Platinum 7000792289606361",
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305"
]

for example in examples:
    masked_result = mask_account_card(example)
    print(f"{example} => {masked_result}")

date_examples = [
    "2024-03-11T02:26:18.671407",
    "2030-01-15T10:30:00.000000"
]

for date_example in date_examples:
    formatted_date = get_date(date_example)
    print(f"{date_example} => {formatted_date}")
