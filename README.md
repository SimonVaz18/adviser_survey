# Adviser Survery Insights Tool

Project 3 - Simon Vaz

View github repository:
Vieww live deployed project on Heroku: 

## Overview

The **Aviser Survery Insights Tool** is a phyton based terminal application that helps an Investment Management company track and analyse the performace of their advisers based on client/investor feedback. The tool prompts users to input 8 different ratings on different service areas. It then imports and stores the data in a Google Sheet. Calculations via functions implemented in the code provide meaningful insights such as weighted overall score, performance trends and category averages. This should help the firm make data-informed decisions to improve client experience.

## Purpose 

- Quantifies strengths and weaknesses of adviser performance
- Calculates a weighted average to prioritise the most important service areas
- Shows trends in performance over time
- Displays and stores raw data as well as insights for transparency and reporting

## Intended Users 

- Administrators - input the client feedback
- Management teams - review and act on adviser quality
- Advisers - Review and reflect on responses/insights to create actionable objectives

## Features

### 1. Survey Input (Function: 'get_survey_data')

This function prompts users to rate 8 adviser service categories on a scale from 1 to 10:

- Professionalism
- Clarity of Advice
- Responsiveness
- Product Knowledge
- Trustworthiness
- Empathy
- Communication
- Overall Experience

Each rating is validated to ensure it's a valid integer between 1 and 10. If incorrect input is detected (e.g. a letter, number above 10, etc.), the user is informed of the invalid input and prompted again.

---

### 2. Data Storage (Function: 'update_worksheet')

Once a full set of 8 ratings is entered, the data is appended as a new row in the `responses` worksheet within the connected Google Sheet. This maintains a full history of all responses.

The `insights` worksheet is also updated after analysis is performed. 

---

### Analysis Functions

### 3. Function: 'get_all_responses'

This function pulls all numeric data from the `responses` worksheet and returns it as a list of integer lists with each row being one complete survey.

---

### 4. Function: 'calculate_averages'

This function calculates the average rating per category from all recorded responses. Each time a user submits their survey ratings, a new row is added to the responses worksheet. Analysis is done using the following steps:

1. The 'data' in 'calculate_averages(data)' is a list of lists with each inner being one row in the responses sheet
2. 'zip(*data)' transposes the data and turns the rows into columns so you can calculate the average per category
3. Each column, now a list of all scores for that category, is summed and divided by how many entries exist
4. This provides a list of 8 averages, one per survey question

---

### 5. Function: 'calculate_weighted_average

Constants have been set at the start of the code that assigns weights to each survey question based on how important the category is. These weights are used in the function to calculate a more meaningful overall score across all categories.

1. The 'averages' in 'calculate_weighted_average' is the average score taken from the 'calculate_averages' function
2. Each score is multiplied by its weight in order to give more points to more important questions
3. All the new weighted scores are summed and all the wweights are summed
4. The total score is then divided by the total weights to give a funal weighted average score

---

### 6. Function: 'find_outliers'

This is a simple function used to identify the highest and lowest rated categories. Averages are input and indexed against the questions match thee highest/lowest score with a particular question. The function then returns a readable sting displaying the results. 

The intention of this function is to provide quick insights into where advisers are doing particularly well and where improvements are needed.

### 7. Function: 'calculate_trend'

This function compares the most recent two rows in the 'insights' sheet to determine how the overall weighted score has been changed. It has been designed to track how overall performance is changing over time based on past survey data:
- If the score is improving: "Improving"
- If the score decreased: "Declining"
- If the score stayed the same: "Steady"

The code is executed as below:

1. The insights sheet is accessed to retrieve all past insights rows as a list of lists
2. A check is in place to ensure there is enough data i.e. 2 entries. If there is not, 'N/A' is returned
3. The previous and current weighted average values are extracted from the 9th column in the insights sheet
4. These 2 scores are then compared and a readable ouput is output

## Supporting Imagery

### Initial Prompt
![initial-prompt](assets/images/initial_prompt.png)