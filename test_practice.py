from practice import *

# This should pass 
def test_add_6_4():
	assert(add_two_numbers(4, 6) == 10)
	
# This should fail
def test_incorrect_6_4():
	assert(add_two_numbers_incorrect(4, 6) == 10)
	
