# -*- coding: utf-8 -*-

# Variable: var_name
# Describe variable.
var_name = True


# Class: MyClass
# Describe the class here.
#
# Attributes:
#    attr1 - First attribute of the class
#    attr2 - Second one
class MyClass(models.Model):
    attr1 = []
    attr2 = ""
    # Constructor: __init__
    # Describe the constructor.
    #
    # Parameters:
    #   arg1 - The first argument.
    def __init__(self, arg1):
        self.attr1 = arg1
        self.attr2 = "attr2"

    # Method: method1
    # Describe the method here.
    #
    # Parameters:
    #   arg1 - The first argument.
    #   arg2 - The second argument.
    def method1(self, arg1, arg2):
        # Variable: var_name_02
        # Describe variable.
        #
        # Returns:
        # True
        var_name_02 = ""
        pass


# Function: test_test
# Description
#
# Returns:
# List
def test_test():
    pass

# Function: test_test_02
# describe
# - Bullet one.
# - Bullet two.
#  Bullet two continued.
# - Bullet three.
#
# Some text after the bullet list.
#
# Returns:
# [Tuple]
#
# See Also:
# <MyClass>
def test_test_02():
    pass

# Function: test_test_03
# describe
# *Bold text*
#
# _Underlined text_
#
# Paragraphs are broken by skipping lines.  So the two
# lines above each have their own paragraph, but these
# three lines are all part of the same one.
# (start code)
# 
# if (x == 0) {
#    DoSomething();
# }
# 
# return x;
# 
# (end)
#
# : a = b + c;
#
# >   +-----+     +-----+
# >   |  A  | --> |  B  |
# >   +-----+     +-----+
# >                  |
# >               +-----+
# >               |  C  |
# >               +-----+
#
# Visit <http://www.website.com> or send messages to
# email@address.com.
#
# Some text after the bullet list.
#
# Returns:
# [Tuple]
#
# : a = b + c;
def test_test_03():
    pass


