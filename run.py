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
    "Professionalism",
    "Clarity of Advice",
    "Responsiveness",
    "Product Knowledge",
    "Trustworthiness",
    "Empathy",
    "Communication",
    "Overall Experience"
]


#Functions 

def get_survey_data():
    """
    Cue user to enter ratings as intergers between 1-10 for survey questions.
    """

    print("\n Adviser Survey: Please rate the following categories from 1 to 10 \n")
    ratings = []
    for q in Questions:
        while True:
            try:
                value = int(input(f"{q}: "))
                if 1 <= value <= 10:
                    ratings.append(value)
                    break
                else:
                    print("Please enter a number between 1 and 10.\n")
            except ValueError:
                print("Invalid input. Please enteer a valid integer.\n")
    return ratings

print(get_survey_data())

"""
    Function to Validate inputs
    """

    """
    Append a row of data to the applicable worksheet
    """    
    

    """
    Function to get all responses
    """
    
    """
    Calculate Averages
    """

    """
    Calculate Weighted Averages
    """

    """
    Function to find extremes
    """

    """
    Function to find trends
    """