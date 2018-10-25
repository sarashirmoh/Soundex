
# coding: utf-8

# In[ ]:


#DON'T FORGET TO HANLE UPPERCASE
from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """
    vowels = ['a', 'A','e','E','h','H','i','I','o','O','u','U','w','W','y','Y']
    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    f1.add_state('start')
    f1.add_state('s11')
    f1.add_state('s22')
    f1.add_state('s33')
    f1.add_state('s44')
    f1.add_state('s55')
    f1.add_state('s66')
    f1.add_state('s1')
    f1.add_state('s2')
    f1.add_state('s3')
    f1.add_state('sv')
    f1.add_state('s4')
    f1.add_state('s5')
    f1.add_state('s6')
    
    
    f1.add_state('next')
    f1.initial_state = 'start'

    # Set all the final states
    f1.set_final('next')

    # Add the rest of the arcs
    for letter in string.ascii_letters:
        #f1.add_arc('start', 'next', (letter), (letter))
        #f1.add_arc('next', 'next', (letter), ('0'))

        if letter in vowels:
            f1.add_arc('start', 'sv', (letter), (letter))
            f1.add_arc('s11','sv',(letter),())
            f1.add_arc('s33','sv',(letter),())
            f1.add_arc('s22','sv',(letter),())
            f1.add_arc('s44','sv',(letter),())
            f1.add_arc('s55','sv',(letter),())
            f1.add_arc('s66','sv',(letter),())
            f1.add_arc('sv','sv',(letter),())
            f1.add_arc('s1','sv',(letter),())
            f1.add_arc('s2','sv',(letter),())
            f1.add_arc('s3','sv',(letter),())
            f1.add_arc('s4','sv',(letter),())
            f1.add_arc('s6','sv',(letter),())
            f1.add_arc('s5','sv',(letter),())
            #f1.add_arc('s3','s4',(letter),(letter))            
        elif letter in "Ll":
            f1.add_arc('start', 's44', (letter), (letter))
            f1.add_arc('s44','s4',(letter),())
            f1.add_arc('s11','s4',(letter),('4'))
            f1.add_arc('s22','s4',(letter),('4'))
            f1.add_arc('s33','s4',(letter),('4'))
            f1.add_arc('s55','s4',(letter),('4'))
            f1.add_arc('s66','s4',(letter),('4'))
            f1.add_arc('s4','s4',(letter),())
            f1.add_arc('s1','s4',(letter),('4'))
            f1.add_arc('s2','s4',(letter),('4'))
            f1.add_arc('s3','s4',(letter),('4'))
            f1.add_arc('s5','s4',(letter),('4'))
            f1.add_arc('s6','s4',(letter),('4'))
            f1.add_arc('sv','s4',(letter),('4'))
        elif letter in 'Rr': 
            f1.add_arc('start', 's66', (letter), (letter))
            f1.add_arc('s66','s6',(letter),())
            f1.add_arc('s22','s6',(letter),('6'))
            f1.add_arc('s33','s6',(letter),('6'))
            f1.add_arc('s44','s6',(letter),('6'))
            f1.add_arc('s55','s6',(letter),('6'))
            f1.add_arc('s11','s6',(letter),('6'))
            f1.add_arc('s6','s6',(letter),())
            f1.add_arc('s1','s6',(letter),('6'))
            f1.add_arc('s2','s6',(letter),('6'))
            f1.add_arc('s3','s6',(letter),('6'))
            f1.add_arc('s5','s6',(letter),('6'))
            f1.add_arc('s4','s6',(letter),('6'))
            f1.add_arc('sv','s6',(letter),('6'))
        elif letter in "bfpvBFPV":
            f1.add_arc('start', 's11', (letter), (letter))
            f1.add_arc('s11','s1',(letter),())
            f1.add_arc('s22','s1',(letter),('1'))
            f1.add_arc('s33','s1',(letter),('1'))
            f1.add_arc('s44','s1',(letter),('1'))
            f1.add_arc('s55','s1',(letter),('1'))
            f1.add_arc('s66','s1',(letter),('1'))
            f1.add_arc('s1','s1',(letter),())
            f1.add_arc('s5','s1',(letter),('1'))
            f1.add_arc('s2','s1',(letter),('1'))
            f1.add_arc('s3','s1',(letter),('1'))
            f1.add_arc('s4','s1',(letter),('1'))
            f1.add_arc('sv','s1',(letter),('1'))
            f1.add_arc('s6','s1',(letter),('1'))
        elif letter in "cgjkqsxzCGJKQSXZ":
            f1.add_arc('start', 's22', (letter), (letter))
            f1.add_arc('s22','s2',(letter),())
            f1.add_arc('s11','s2',(letter),('2'))
            f1.add_arc('s33','s2',(letter),('2'))
            f1.add_arc('s44','s2',(letter),('2'))
            f1.add_arc('s55','s2',(letter),('2'))
            f1.add_arc('s66','s2',(letter),('2'))
            f1.add_arc('s2','s2',(letter),())
            f1.add_arc('s5','s2',(letter),('2'))
            f1.add_arc('s1','s2',(letter),('2'))
            f1.add_arc('s3','s2',(letter),('2'))
            f1.add_arc('s4','s2',(letter),('2'))
            f1.add_arc('sv','s2',(letter),('2'))
            f1.add_arc('s6','s2',(letter),('2'))
        elif letter in "mnMN":
            f1.add_arc('start', 's55', (letter), (letter))
            f1.add_arc('s55','s5',(letter),())
            f1.add_arc('s11','s5',(letter),('5'))
            f1.add_arc('s44','s5',(letter),('5'))
            f1.add_arc('s33','s5',(letter),('5'))
            f1.add_arc('s22','s5',(letter),('5'))
            f1.add_arc('s66','s5',(letter),('5'))
            f1.add_arc('s5','s5',(letter),())
            f1.add_arc('s2','s5',(letter),('5'))
            f1.add_arc('s1','s5',(letter),('5'))
            f1.add_arc('s3','s5',(letter),('5'))
            f1.add_arc('s4','s5',(letter),('5'))
            f1.add_arc('sv','s5',(letter),('5'))
            f1.add_arc('s6','s5',(letter),('5'))
        elif letter in "dtDT":
            f1.add_arc('start', 's33', (letter), (letter))
            f1.add_arc('s33','s3',(letter),())
            f1.add_arc('s11','s3',(letter),('3'))
            f1.add_arc('s44','s3',(letter),('3'))
            f1.add_arc('s55','s3',(letter),('3'))
            f1.add_arc('s22','s3',(letter),('3'))
            f1.add_arc('s66','s3',(letter),('3'))
            f1.add_arc('s3','s3',(letter),())
            f1.add_arc('s2','s3',(letter),('3'))
            f1.add_arc('s1','s3',(letter),('3'))
            f1.add_arc('s5','s3',(letter),('3'))
            f1.add_arc('s4','s3',(letter),('3'))
            f1.add_arc('sv','s3',(letter),('3'))
            f1.add_arc('s6','s3',(letter),('3'))
    """    else:
            f1.add_arc('s1','s5',(letter),('1'))
            f1.add_arc('s4','s5',(letter),('1'))
            f1.add_arc('s6','s5',(letter),('1'))
            f1.add_arc('s44','s5',(letter),('1'))
            f1.add_arc('s66','s5',(letter),('1'))
            f1.add_arc('s3','s5',(letter),('1'))

            #f1.add_arc('s5','s5',(letter),())   """
    f1.add_arc('s11','next',(),())
    f1.add_arc('s22','next',(),())
    f1.add_arc('s33','next',(),())
    f1.add_arc('s44','next',(),())
    f1.add_arc('s55','next',(),())
    f1.add_arc('s66','next',(),())
    f1.add_arc('s1','next',(),())
    f1.add_arc('s2','next',(),())
    f1.add_arc('s3','next',(),())
    f1.add_arc('sv','next',(),())
    f1.add_arc('s4','next',(),()) 
    f1.add_arc('s5','next',(),())
    f1.add_arc('s6','next',(),())
    return f1

    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('ste')
    f2.add_state('L1')
    f2.add_state('N1')
    f2.add_state('N2')
    f2.add_state('N3')
    f2.add_state('next1')
    f2.initial_state = 'ste'
    
    f2.set_final('next1')
    for letter in string.letters:
        f2.add_arc('ste', 'L1', (letter), (letter))
    for n in range(10):
        f2.add_arc('ste', 'N1',(str(n)), (str(n)))
        f2.add_arc('L1', 'N1',(str(n)), (str(n)))
        f2.add_arc('N1', 'N2', (str(n)), (str(n)))
        f2.add_arc('N2', 'N3', (str(n)), (str(n)))
        f2.add_arc('N3', 'N3', (str(n)), ())
    # Add the arcs
    """for letter in string.letters:
        f2.add_arc('1', '1', (letter), (letter))

    for n in range(10):
        f2.add_arc('1', '1', (str(n)), (str(n)))"""
    f2.add_arc('L1','next1',(),())
    f2.add_arc('N1','next1',(),())
    f2.add_arc('N2','next1',(),())
    f2.add_arc('N3','next1',(),())

    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('st')
    f3.add_state('L1')
    f3.add_state('N1')
    f3.add_state('N2')
    f3.add_state('N3')
    f3.add_state('P1')
    f3.add_state('P2')
    f3.add_state('P3')
    
    f3.initial_state = 'st'
    f3.set_final('N3')
    f3.set_final('P3')

    for letter in string.letters:
        f3.add_arc('st', 'L1', (letter), (letter))
    for number in xrange(10):
        f3.add_arc('st', 'N1', (str(number)), (str(number)))
        f3.add_arc('L1', 'N1', (str(number)), (str(number)))
        f3.add_arc('N1', 'N2', (str(number)), (str(number)))
        f3.add_arc('N2', 'N3', (str(number)), (str(number)))
    
    f3.add_arc('L1', 'P1', (), ('0'))
    f3.add_arc('N1', 'P2', (), ('0'))
    f3.add_arc('N2', 'P3', (), ('0'))
    f3.add_arc('P1', 'P2', (), ('0'))
    f3.add_arc('P2', 'P3', (), ('0'))
    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))

