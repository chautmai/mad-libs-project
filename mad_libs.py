#GREETING
print('WELCOME!')
print('This is a text-based introduction of yourself. You will be asked to asnswer\nmultiple questions and the introduction will be automatically generated as\na paragraph with your answers concatinated.')

while True:
    #Ready to play the game?
    ready = input('\nAre you ready? (y/n) ')

    if ready == 'y':
        print('You answer \'y\' = (Yes). Okay let\'s begin.')
        # QUESTIONARES
        name = str(input('What is your name? ').title())
        age = int(input('What is your age? '))
        hometown = str(input('Where is your original hometown? ').title())
        place_moved = str(input('Where have you moved to? ').title())
        years_ago = int(input('How many years have you moved to that place? '))
        like_to = str(input('What do you like to do in your spare time? '))
        family_members = int(input('How many members are in your household? '))
        nth_child = input('What place are you in your family? (first, second, third, fouth) ')
        number_of_children = int(input('How many children does your family have? '))
        high_school = str(input('What high school did you attend? ').title())
        years_graduated_hs = int(input('How many years did that take you to complete High School? '))
        college = str(input('What college did you go to? ').title())
        years_graduated_college = int(input('How many years later did you complete your degree? '))
        degree_type = str(input('What type of degree was it? ').title())
        major = str(input('What was your major? ').title())
        field = str(input('What field did that major relate to? ').title())
        things_to_create = str(input('What do you want to create in that field? '))
        want_to_be = str(input('What do you want to become? ').title())

        #SUCCESS
        print('\nCongratulations!!! Intro generated successfully.')
        print('\nThis is the intro we generated for you.')

        #INTRO LOG
        print('\nHello, my name is',name+'. I am', str(age),'years old. I am origially from',hometown +'. I first moved to the',place_moved, 'about', str(years_ago), 'years ago. I like to', like_to,  'in my spare time.\nWe have', str(family_members), 'members in the family. I am the', str(nth_child),'child in', str(number_of_children), 'children of my family. I went to high school at', high_school, 'High School.\nI graduated High School about', str(years_graduated_hs), 'years ago. Then I went on and attended', college, 'years later. It took me', str(years_graduated_college), 'years to complete my', degree_type, 'degree in',major,'.\nI love working with', field, 'where I can create', things_to_create, 'as a career. I want to become a', want_to_be + '.')

        print('\nThank you for participating. See you again.')

        
    if ready == 'n':
        print('You answered \'n\' = (No), let\'s not begin. Good bye.')
        print('Program exited.')
        break

    else:
        print('Answer not valid. Let\'s try again.')
