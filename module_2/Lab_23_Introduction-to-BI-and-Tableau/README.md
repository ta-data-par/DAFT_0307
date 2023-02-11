![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | Introduction to BI and Tableau

## Introduction

In this lab, we will practice loading data into Tableau, inspecting and modifying data types, and creating tabular views with metrics based on the information contained in the data set. We will be working with the given dataset.

If you get stuck on any of the tasks in this lab, you can reference the excellent training video resources provided on the [Tableau website](https://www.tableau.com/learn/training). We have also referenced specific articles on topics such as binning variables and creating aliases that should be helpful in completing this lab.

## Getting Started

To complete this lab, follow each of the steps below.

1. Open the [data set](https://docs.google.com/spreadsheets/d/1pQ2VFsuuwLqBstYYTY3fcZY32WLigw3Pzxnikkce6IA/edit?usp=sharing) in a browser.
2. Add the data set to your Google Drive.
3. Launch the Tableau Public application.
4. Import the data set from Google Sheets into Tableau.
5. Create a new calculated field called Year_Month as a date based on Year, Month and 1st of the month. 
    - Use the drop down arrow on either the year or month column and select create calculated field
    - Use the Date() function, and as input concatonate a date string in this format "YYYY-MM-DD" using the str() function with the provided year and month fields and a constant for the day
6. Move to your first sheet
7. Drag your newly created Year_Month calculated field to rows and click the [+] on the pill in rows so you see both the year and quarter.
8. Create a new worksheet for each of the following tabular views:
    - Total Retail Sales by Year/Quarter (rows).
    - Average Retail Sales by Year/Quarter (rows).
    - Total Retail Sales by Year/Month (rows) and Item Type (columns).
    - Average Retail Sales by Year/Month (rows) and Item Type (columns).
    - Total Retail Transfers by Year/Quarter (rows).
    - Average Retail Transfers by Year/Quarter (rows).
    - Total Retail Transfers by Year/Month (rows) and Item Type (columns).
    - Average Retail Transfers by Year/Month (rows) and Item Type (columns).
    - Total Warehouse Sales by Year/Quarter (rows).
    - Average Warehouse Sales by Year/Quarter (rows).
    - Total Warehouse Sales by Year/Month (rows) and Item Type (columns).
    - Average Warehouse Sales by Year/Month (rows) and Item Type (columns).
9. (Optional) Create a dashboard and bring all the sheets into the dashboard.
10. Save your work to Tableau Public, ensure that your workbook is viewable, and copy the URL for the workbook into the deliverables file for this lab. It might take several minutes for this workbook to save to Tableau Public due to the number of records in the data set.

## Deliverables

- `main.txt` file with a link to your Tableau Public workbook.

## Submission

Upon completion, add your deliverables to git. Then commit git and push your branch to the remote.

## Resources

- [Google Sheets - Tableau](https://onlinehelp.tableau.com/current/pro/desktop/en-us/examples_googlesheets.htm)

- [Data Types - Tableau](https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_typesandroles_datatypes.htm)

- [Create Bins from a Continuous Measure](https://onlinehelp.tableau.com/current/pro/desktop/en-us/calculations_bins.htm)

- [Create Aliases to Rename Members in the View](https://onlinehelp.tableau.com/current/pro/desktop/en-us/datafields_fieldproperties_aliases_ex1editing.htm)

- [Tableau Training Videos](https://www.tableau.com/learn/training)
