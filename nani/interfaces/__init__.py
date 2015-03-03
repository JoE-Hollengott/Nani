
from nani.interfaces.en_wikipedia_interface import En_Wikipedia
from nani.interfaces.stackoverflow_interface import Stackoverflow
from nani.interfaces.cplusplus_interface import Cplusplus
from nani.interfaces.tutorialspoint_interface import Tutorialspoint


# Add all the classes here. like as above.
#
# Make sure all added interface classes have an __init__(self)
# Make sure all added interface classes have an 
# analyze_page(self, page, search)
#
# The analyze_page method must return a tuple of
# (question, answers[], ratings[])
# There MUST be the same amount of ratings as there are answers.
# The question is a single string, the answers is a list of strings, ratings
# is a list of ints OR the string'NA'
# The Results field can be individual vote system on the site or how many
# refrences the page has.
#
# For error checking, because the classes are called dynamically you must 
# output your error's to a log or to standard out.
#
# As for naming the filename is the base website domain name. if there is
# preceeding subdomain replace the dot with an underscore.
# (see en_wikipedia_interface) then put _interface onto the end of the 
# filename.
#
# NO POST DOMAIN (eg, .com .org .net )
#
# The classname is the same as the domain however it starts with a capital.
# Eg (En_Wikipedia)
# If there is a sub domain both words start with capitals.

