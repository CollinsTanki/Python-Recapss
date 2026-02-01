#If applicant has_high_income or has_good_credit then Elligble for loan
from logical_and import has_high_income, has_good_credit

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Elligible for loan")
