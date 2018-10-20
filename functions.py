from Npo import Npo

def create_npo(website, name, email, number, target_donors, target_volunteers, image, description):
    npo = Npo(website, name, email, number, target_donors, target_volunteers, image, description)
    npos.append(npo)