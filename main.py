from sheets_connector import read_from_sheet, write_to_sheet
import os

creds = os.getenv("GOOGLE_SHEETS_CREDENTIALS", "credentials/psychic-raceway-459107-q0-4e66ae2a0716.json")
sheet_id = os.getenv("GOOGLE_SHEET_ID", "14cQkxZSrMiTBlMMrFXg7V3M-sF1vMdErvHiX29yXFgU")

# Read
input_data = read_from_sheet(sheet_id, 'Sheet1!A1:E10', creds)
print("Input Data:", input_data)

# Write test
test_output = [["Player", "Team", "Salary"], ["Test Player", "XYZ", 4500]]
updated_cells = write_to_sheet(sheet_id, 'Sheet1!G1', test_output, creds)
print(f"{updated_cells} cells updated.")

