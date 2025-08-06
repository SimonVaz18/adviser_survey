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
QUESTIONS = [
    "Professionalism",
    "Clarity of Advice",
    "Responsiveness",
    "Product Knowledge",
    "Trustworthiness",
    "Empathy",
    "Communication",
    "Overall Experience"
]

WEIGHTS = [1, 1.3, 0.9, 1.1, 1.1, 0.9, 1, 1.3]

#Functions 

def get_survey_data():
    """
    Cue user to enter ratings as intergers between 1-10 for survey questions.
    """

    print("\n Adviser Survey: Please rate the following categories from 1 to 10 \n")
    ratings = []
    for q in QUESTIONS:
        while True:
            try:
                value = int(input(f"{q}: "))
                if 1 <= value <= 10:
                    ratings.append(value)
                    break
                else:
                    print("Please enter a number between 1 and 10.\n")
            except ValueError:
                print("Invalid input. Please enter a valid integer.\n")
    return ratings


def update_worksheet(data,worksheet_name):
    """
    Append a row of data to the applicable worksheet
    """ 
    print(f"\n Updating '{worksheet_name}' worksheet...")
    worksheet = SHEET.worksheet(worksheet_name)
    worksheet.append_row(data)
    print(f"'{worksheet_name}' updated successfully.\n")

def get_all_responses():
    """
    Gets all rows from the responses worksheet as lists of integers
    """
    rows = SHEET.worksheet("responses").get_all_values()
    return [[int(cell) for cell in row] for row in rows if all(cell.isdigit() for cell in row)]
    
def calculate_averages(data):
    """
    Calculates averages per question for all responses via transposing data
    """
    transposed = list(zip(*data))
    return [round(sum(col) / len(col), 1) for col in transposed]

def calculate_weighted_average(averages):
    """
    Applies weights to scores to calculate weighted averages for each question
    """
    weighted_total = sum(avg * weight for avg, weight in zip(averages,WEIGHTS))
    total_weights = sum(WEIGHTS)
    return round(weighted_total / total_weights, 2)
    
def main():
    ratings = get_survey_data()
    update_worksheet(ratings, "responses")

    all_data = get_all_responses()
    averages = calculate_averages(all_data)
    weighted_avg = calculate_weighted_average(averages)

    insights_row = averages + [weighted_avg]

    update_worksheet(insights_row, "insights")
    

if __name__ == "__main__":
    main()

    