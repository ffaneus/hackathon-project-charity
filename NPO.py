from donor import Donor
from volunteer import Volunteer


class NPO():
    def __init__(self, website, name, email, number, target_donors, target_volunteers, image, description):
        self.donors = []
        self.volunteers = []
        self.website = website
        self.name = name
        self.email = email
        self.number = number
        self.target_donors = target_donors
        self.target_volunteers = target_volunteers
        self.image = image
        self.volunteer_num = 0
        self.description = description
        npos.append(self)
    def delete(self):
        """Delete using html or flask and delete from database"""
    def add_volunteer(self, days, hours):
        """adds volunteer and the total volunteers is displayed using flask or html"""
        self.volunteer_num += 1
        volunteer = Volunteer(self.name, self, days, hours)
        self.volunteers.append(volunteer)
    def add_donor(self, item, amount):
        """adds donor using Donor class to the NPO"""
        donor = Donor(self.name, self, item, amount)
        self.donors.append(donor)
