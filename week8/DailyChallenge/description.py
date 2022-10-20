# Daily Challenge : People


# What You Will Learn :
# Django views and templates


# Instructions
# You have the following list of dictionaries:

# people = [
#   {
#     'id': 1,
#     'name': 'Bob Smith',
#     'age': 35,
#     'country': 'USA'
#   },
#   {
#     'id': 2,
#     'name': 'Martha Smith',
#     'age': 60,
#     'country': 'USA'
#   },
#   {
#     'id': 3,
#     'name': 'Fabio Alberto',
#     'age': 18,
#     'country': 'Italy'
#   },
#   {
#     'id': 4,
#     'name': 'Dietrich Stein',
#     'age': 85,
#     'country': 'Germany'
#   }
# ]


# Create a Django projects with two views:
# The first view is /people which renders the list of people along with the rest of the information they have, sorted by age.

# The second view is /people/{id} where id is the id of the person. This view presents information about a single person.
# Make sure that the template rendered in /people contains links to people/{id}
# Requirements : Use as many templates filters as you can