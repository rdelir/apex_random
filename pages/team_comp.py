import random

legends = ['Ash', 'Bangalore', 'Bloodhound', 'Caustic', 
           'Crypto', 'Fuse', 'Gibraltar', 'Horizon', 
           'Lifeline', 'Loba', 'Maggie', 'Mirage', 'Newcastle', 
           'Octane', 'Pathfinder', 'Rampart', 'Revenant', 
           'Seer', 'Valkyrie', 'Wattson', 'Wraith']

def playstation():
    first_legend = legends.pop(legends.index(random.choice(legends)))
    return("The First Legend is", first_legend)

def xbox():
    second_legend = legends.pop(legends.index(random.choice(legends)))
    return("The Second Legend is", second_legend)

def pc():
    third_legend = legends.pop(legends.index(random.choice(legends)))
    return("The Third Legend is", third_legend)
