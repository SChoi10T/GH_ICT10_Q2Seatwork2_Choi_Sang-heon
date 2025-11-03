# Grade Calculator
from pyscript import display, document # pyright: ignore[reportMissingImports]

def getting_gwa(e):
    document.getElementById('output1').innerHTML = "" # Clear Output
    document.getElementById('output2').innerHTML = "" # Clear Output

    # Student Details
    first_name = document.getElementById("fname").value.strip()
    surname = document.getElementById("lname").value.strip()

    fil = int(document.getElementById('filipino').value)
    eng = int(document.getElementById('english').value)
    math = int(document.getElementById('mathematics').value)
    sci = int(document.getElementById('science').value)
    ss = int(document.getElementById('ss').value)
    ict = int(document.getElementById('ict').value)

    grades = [fil, eng, math, sci, ss, ict]
    units = (3, 5 , 5, 4, 3, 1)

    total_units = sum(units)
    weighted_sum = sum(grades[i] * units[i] for i in range(len(grades)))
    gwa = weighted_sum / total_units

    # gwa = (fil * units[0]) + (eng * units[1]) + (math * units[2]) + (sci * units[3]) + (ss* units[4]) + (ict * units[5]) // 21

    display(f"Name: {first_name} {surname}", target="output1")
    display(f"Your General Weighted Average is: {gwa}", target = 'output2')