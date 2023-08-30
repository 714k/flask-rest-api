from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
  "Fairy": {
    "firstname": "Tooth",
    "lastname": "Fairy",
    "timestamp": get_timestamp(),
  },
  "Ruprecht": {
    "firstname": "Knecht",
    "lastname": "Ruprecht",
    "timestamp": get_timestamp(),
  },
  "Bunny": {
    "firstname": "Easter",
    "lastname": "Bunny",
    "timestamp": get_timestamp(),
  }
}

def read_all():
    return list(PEOPLE.values())


def create(person):
    # if lastname:
    lastname = person.get("lastname")
    firstname = person.get("firstname", "")

    if lastname and lastname not in PEOPLE:
        PEOPLE[lastname] = {
            "lastname": lastname,
            "firstname": firstname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lastname], 201
    else:
        abort(
            406,
            f"Person with last name {lastname} already exist",
        )


def read_one(lastname):
    print(lastname in PEOPLE)
    if lastname in PEOPLE:
        return PEOPLE[lastname]
    else:
        abort(
            404,
            f"Person with last name {lastname} not found"
        )


def update(lastname, person):
    if lastname in PEOPLE:
        PEOPLE[lastname]["firstname"] = person.get("firstname", PEOPLE[lastname]["firstname"])
        PEOPLE[lastname]["lastname"] = person.get("lastname", PEOPLE[lastname]["lastname"])
        PEOPLE[lastname]["timestamp"] = get_timestamp()
        return PEOPLE[lastname]
    else:
        abort(
          404,
          f"Person with last name {lastname} not found"  
        )


def delete(lastname):
    if lastname in PEOPLE:
        del PEOPLE[lastname]
        return make_response(
            f"{lastname} successfully deleted",
            200
        )        
    else:
        abort(
            404,
            f"Person with last name {lastname} not found"
        )            