# Exercises XP
# What We Will Learn
# Django Models


# Exercise 1 : Animals
# This Exercise Is Inspired By The Exercise Of Yesterday. Follow The Below Instructions.
# This Exercise Is Using MODELS Instead Of A Json File
# We will create a simple Django-based web application to manage information about different animals.

# Create a new directory for your project with a new virtual environment. Call the directory animal-info.
# Activate your new virtual environment, then install Django.
# Create a new project using Django called animals, and then create a new app inside it called info.

# Our project should have the following models:
# Animal, with properties:
# id
# legs – an integer, the number of legs the animal has
# weight – the average weight of an adult animal of this type
# height – the average height of an adult animal of this type
# speed – the maximum speed at which this animal can move
# family – the family to which this animal belongs. (Must reference the Family model - see below).
# Family, representing an animal group or family, with properties:
# id
# name

# Make any database migrations that you need, and run the migration(s).

# Create 3 views, corresponding to the following URLs:
# /family/X, where X is the ID (primary key) of the given family. Should show a list of all animals in that family.
# /animal/X, where X is the ID (primary key) of the given animal. Should show all the information about the given animal.
# /animals/ - should show a list of all the animals. When you click on any of the animals in the list, you should be taken to /animal/X (see above).

# Create three templates rendered by the three views above

# Add a few families to your app, using the app itself. Recommended families:
# mammal
# reptile
# insect
# arachnid
# amphibian
# etc.

# Add a few animals to your database. (You will have to do this using SQL, as the foreign key reference between the Animal and Family entities requires some extra coding which you might not know about, yet.) Make sure that they show up in the relevant views.