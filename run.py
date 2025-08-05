import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('adviser_survey')

# Constants 
Questions = [
"Service", "Product", "Price", "Website", "Delivery", "Support", "Communication", "Overall"
]

#Functions 

def get_survey_data():
    """
    Cue user to enter survey data as 8 intergers between 1-10 and returns data as integers.
    """

    while True:
        print("Please enter 8 survey ratings (1-10) sparated by commas.")
        print("Order " + ", ".join(Questions))
        print("Example: 8,7,6,5,4,3,2,1\n")

        data_str = input("Enter your data here:\n")
        data = data_str.split(",")

        if validate_data(data):
            break

        return [int(num) for num in data]
    
    
    

