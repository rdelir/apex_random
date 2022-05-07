import random

legends = ['Ash', 'Bangalore', 'Bloodhound', 'Caustic', 
           'Crypto', 'Fuse', 'Gibraltar', 'Horizon', 
           'Lifeline', 'Loba', 'Maggie', 'Mirage', 
           'Octane', 'Pathfinder', 'Rampart', 'Revenant', 
           'Seer', 'Valkyrie', 'Wattson', 'Wraith']

first_legend = legends.pop(legends.index(random.choice(legends)))
print("Your First Legend is", first_legend)

second_legend = legends.pop(legends.index(random.choice(legends)))
print("Your Second Legend is", second_legend)

third_legend = legends.pop(legends.index(random.choice(legends)))
print("Your Third Legend is", third_legend)
