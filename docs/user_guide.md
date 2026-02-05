# Personal Finance Manager - User Guide

## Overview
**Personal Finance Manager** is a command-line Python application that helps users track daily expenses, categorize spending, generate summaries and reports, search entries, and maintain data persistence using a CSV file.

**Main features:**
- Add new expenses with amount, category, date, and description
- View all recorded expenses (sorted by date)
- View category-wise spending summary
- Generate monthly expense reports
- Search expenses by keyword
- Backup and restore expense data
- Input validation and friendly error messages

Data is automatically saved to `data/expenses.csv` and loaded on startup.

## Requirements
- Python 3.8 or higher  
  (The project was developed and tested with Python 3.12)
- No external packages required  
  (Uses only Python's standard library: csv, datetime, os, shutil, collections, sys)

## Installation & Running the Application

1. **Download / Clone the project**
   - Get the complete folder: `personal-finance-manager`

2. **Open the project**
   - Recommended: Open the folder in Visual Studio Code
   - File → Open Folder → Select `personal-finance-manager`

3. **Run the program**
   - Open the integrated terminal in VS Code:
     - Terminal → New Terminal  
       (or press `Ctrl + `` )
   - Make sure you are in the project root folder (where `main.py` is located)
   - Type and press Enter:
     ```bash
     python main.py

     
## Contact / Support
- If you face any issues: Check the Troubleshooting section above.
- For questions: Reach out to [lekhasrimeka@gmail.com] or the project maintainer.

Happy expense tracking!   
Created by LekhaSri – February 2026