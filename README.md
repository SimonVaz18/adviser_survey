# Adviser Survery Insights Tool

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

### Analysis Functions

### 3. Function: 'get_all_responses'

This function pulls all numeric data from the `responses` worksheet and returns it as a list of integer lists with each row being one complete survey.

### 4. Function: 'calculate_averages'

This function calculates the average rating per category from all recorded responses. Each time a user submits their survey ratings, a new row is added to the responses worksheet. Analysis is done using the following steps:

1. The 'data' in 'calculate_averages(data)' is a list of lists with each inner being one row in the responses sheet
2. 'zip(*data)' transposes the data and turns the rows into columns so you can calculate the average per category
3. Each column, now a list of all scores for that category, is summed and divided by how many entries exist
4. This provides a list of 8 averages, one per survey question