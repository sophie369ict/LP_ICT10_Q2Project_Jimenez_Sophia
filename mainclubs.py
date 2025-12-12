from js import document

#Storing all club data in a single dictionary 
clubs = {
    "The Dead Poets Society": {
        "Name": "The Dead Poets Society",
        "Description": "A club for readers, writers, and poets by heart to share their love for literature and creative writing.",
        "Meeting Time": "Every Monday at 3:00 PM to 5:00 PM",
        "Location": "Room 101",
        "Advisor": "Ms. Philie Watson-Park and Mr. Rex Dela Cruz",
        "Number of Members": 15,
        "Category": "Academic",
        "Image": "dps.png",
    },
    "The MathSci Nexus": {
        "Name": "The MathSci Nexus",
        "Description": "A club for math and science enthusiasts to explore advanced topics, conduct experiments, and participate in competitions.",
        "Meeting Time": "Every Tuesday at 3:00 PM to 5:00 PM",
        "Location": "Room 202",
        "Advisor": "Mr. Will Yu and Mr. Milo Park",
        "Number of Members": 10,
        "Category": "Academic",
        "Image": "msc.png",
    },
    "The Renaissance Racers": {
        "Name": "The Renaissance Racers",
        "Description": "A club for born artists and musicians to hone their skills, collaborate on projects, and showcase their talents.",
        "Meeting Time": "Every Wednesday at 3:00 PM to 5:00 PM",
        "Location": "Room 303",
        "Advisor": "Ms. Charlotte Yu and Ms. Sienna McAllister",
        "Number of Members": 18,
        "Category": "Non-Academic",
        "Image": "renaissance.png",
    },
    "The Grandmasters Circle": {
        "Name": "The Grandmasters Circle",
        "Description": "A club for chess nerds and strategists to improve their skills, participate in tournaments, and engage in friendly matches.",
        "Meeting Time": "Every Wednesday at 3:00 PM to 5:00 PM",
        "Location": "Room 404",
        "Advisor": "Mr. Julius Schneider and Mr. Adler Windsor",
        "Number of Members": 9,
        "Category": "Non-Academic",
        "Image": "chess.png",
    },
    "The IT Elite": {
        "Name": "The IT Elite",
        "Description": "A club for computer geeks and tech enthusiasts to explore programming, software development, and emerging technologies.",
        "Meeting Time": "Every Thursday at 3:00 PM to 5:00 PM",
        "Location": "Room 505",
        "Advisor": "Mr. Milo Park",
        "Number of Members": 10,
        "Category": "Academic",
        "Image": "comp.png",
    },
    "The Kickfire League": {
        "Name": "The Kickfire League",
        "Description": "A club for student athletes and sport lovers to join the official school varsity teams and compete in inter-school tournaments.",
        "Meeting Time": "Every Friday at 3:00 PM to 5:00 PM",
        "Location": "Room 505",
        "Advisor": "Mr. Arlo Thompson and Mr. Peavey Jackson",
        "Number of Members": 10,
        "Category": "Non-Academic",
        "Image": "sports.png",
    },
}


def show_club_info(event=None):
    """
    This function runs when I click the 'Show Club Information' button.
    It reads the chosen club from the dropdown and fills in the card.
    """
    # Getting the selected club name from select element
    select = document.getElementById("clubSelect")
    club_name = select.value

    #If user doesn't select any club, nothing happens
    club = clubs.get(club_name)
    if club is None:
        return

    #Filling in the text fields inside the card
    document.getElementById("club_name").innerText = club["Name"]
    document.getElementById("club_category").innerText = club["Category"]
    document.getElementById("club_description").innerText = club["Description"]
    document.getElementById("club_time").innerText = club["Meeting Time"]
    document.getElementById("club_location").innerText = club["Location"]
    document.getElementById("club_advisor").innerText = club["Advisor"]
    document.getElementById("club_members").innerText = str(club["Number of Members"])

    #Making sure the card and its image are visible
    document.getElementById("club_card").style.display = "block"
    img = document.getElementById("club_image")
    img.src = club["Image"]
    img.style.display = "block"
