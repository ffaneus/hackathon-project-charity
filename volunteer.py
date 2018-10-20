class Volunteer():
    def __init__(self, days, hours, name):
        self.days = days
        self.hours = hours
        self.name = name
    def submit(self):
        """Confirm you are volunteering/ send to"""
        volunteers.append(self)
