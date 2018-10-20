class Volunteer():
    def __init__(self, days, hours):
        self.days = days
        self.hours = hours
    def submit(self):
        """Confirm you are volunteering/ send to"""
        volunteers.append(self)
