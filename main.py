# Grade Calculator
from pyscript import display, document # pyright: ignore[reportMissingImports]

def calculate_gwa(e):
    document.getElementById('profile_info').innerHTML = ""  # Clear Output
    document.getElementById('gwa_result').innerHTML = ""    # Clear Output

    # Student Details
    first_name = document.getElementById("fname").value.strip()
    surname = document.getElementById("lname").value.strip()

    # Subjects
    fil = int(document.getElementById('filipino').value)
    eng = int(document.getElementById('english').value)
    math = int(document.getElementById('mathematics').value)
    sci = int(document.getElementById('science').value)
    ss = int(document.getElementById('ss').value)
    ict = int(document.getElementById('ict').value)

    grades = [fil, eng, math, sci, ss, ict] # List of subjects
    units = (3, 5 , 5, 4, 3, 1) # Units of each subject

    # Calculating the GWA
    total_units = sum(units)    # Getting the sum of the units
    weighted_sum = sum(grades[i] * units[i] for i in range(len(grades)))    # Multiplies each grade by its subject unit and sum to get the GWA
    gwa = weighted_sum / total_units    # Weighted sum divided by total units

    # Displaying the result of inputted values
    display(f"Name: {first_name} {surname}", target="profile_info")
    display(f"Your General Weighted Average is: {gwa}", target = 'gwa_result')