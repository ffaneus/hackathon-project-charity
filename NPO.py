class Npo():
    def __init__(self, website, name, email, number, target_donors, target_volunteers, image, description):
        self.website = website
        self.name = name
        self.email = email
        self.number = number
        self.target_donors = target_donors
        self.target_volunteers = target_volunteers
        self.image = image
        self.description = description
    def delete(self):
        """Delete using html or flask and delete from database"""
        npos.remove(self)

