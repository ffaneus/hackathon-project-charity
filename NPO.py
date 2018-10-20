class NPO():
    def __init__(self, website, name, email, number, donor, volunteer, image, description):
        self.website = website
        self.name = name
        self.email = email
        self.number = number
        self.donor = donor
        self.volunteer = volunteer
        self.image = image
        self.volunteer_num = 0
        self.description = description

    def post(self):
        """Post using html or flask and save into database"""
        npos.append(self)
    def delete(self):
        """Delete using html or flask and delete from database"""
    def add_volunteer(self, volunteer_num):
        """adds volunteer and the total volunteers is displayed using flask or html"""
        self.volunteer_num += 1

