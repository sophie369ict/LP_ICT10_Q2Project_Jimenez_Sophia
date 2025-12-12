from pyscript import document, display


def grade_average(event):
    """
    This function computes the student's General Weighted Average (GWA)
    based on the six subject grades and their corresponding units.
    """

    #Keeping subjects and their unit weights aligned by index
    subjects = ["Math", "English", "Science", "Social Studies", "P.E.", "Foreign Languages"]
    units = (3, 3, 4, 2, 1, 2)

    #Clearing of previous outputs
    document.getElementById("show_name").innerHTML = ""
    document.getElementById("show_grade").innerHTML = ""
    document.getElementById("show_ave").innerHTML = ""

    # Reading the student's name from the text fields
    first_name = document.getElementById("fname").value.strip()
    last_name = document.getElementById("lname").value.strip()

    #Collecting all six grades from the inputs.
    grades = []
    for i in range(1, 7):
        value = document.getElementById(f"grd{i}").value

 #In case any field is empty, warning shows
        if value.strip() == "":
            display("⚠️ Please fill in all fields before computing.", target="show_ave")
            return

        grades.append(float(value))

    #Computation of the weighted sum and average
    total_weighted = 0
    total_units = 0

    for i in range(len(subjects)):
        total_weighted += grades[i] * units[i]
        total_units += units[i]

    gwa = total_weighted / total_units

    #Full name of student displayed
    display(f"Student Name: {first_name} {last_name}", target="show_name")

    #Simple HTML to show each subject and its weighted grade 
    grade_output = ""
    for i in range(len(subjects)):
        grade_output += f"{subjects[i]} ({units[i]} units): {grades[i]}<br>"
    document.getElementById("show_grade").innerHTML = grade_output

    #Showing the computed GWA rounded to 2 decimal places 
    display(f"General Weighted Average (GWA): {gwa:.2f}", target="show_ave")
