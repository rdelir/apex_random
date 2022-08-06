import random


legends = ['Ash', 'Bangalore', 'Bloodhound', 'Caustic', 'Crypto', 'Fuse', 'Gibraltar', 'Horizon', 'Lifeline', 'Loba', 'Mirage', 'Octane', 'Pathfinder', 'Rampart', 'Revenant', 'Seer', 'Valkyrie', 'Wattson', 'Wraith']
weapons = ['R-310','R-99','Alternator','RE-45','P2020','Rampage','Flatline', 'Hemlok', 'Prowler', 'C.A.R.', '30-30', 'Wingman', 'HAVOC', 'Devotion', 'L-Star', 'Triple Take', 'EVA-8','Mastiff', 'Mozambique', 'Peacekeeper', 'Charge Rifle', 'Longbow', 'Sentinel']
care_package = ['Volt', 'Spitfire', 'G7', 'Kraber', 'Nothing', 'Anything']
#attachments = []

def legend():
    starting_legend = random.choice(legends)
    return "Your Legend is", starting_legend

def primary():
    first_weapon = weapons.pop(weapons.index(random.choice(weapons)))
    #primary_attachment= random.choice(attachments)
    return("Your Primary Weapon is", first_weapon)

def secondary():
    second_weapon = weapons.pop(weapons.index(random.choice(weapons)))
    #secondary_atachment= random.choice(attachments)
    return("Your Secondary Weapon is", second_weapon)
    
def drop():
    extra = random.choice(care_package)
    return("Care Package gives", extra)
