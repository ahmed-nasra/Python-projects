votes = {}

def add_candidates():
    name = input('Enter your candidate name: ')
    if name in votes:
        print(f'Candidate {name} is already in the list')
    else:
        votes[name] = 0
        print(f'Candidate {name} added')

def cast_vote():
    name = input('Enter candidate name to vote for: ')
    if name in votes:
        votes[name] += 1
        print(f'Vote casted for {name}')
    else:
        print(f'{name} not in candidates list')

def view_result():
    if not votes:
        print('Candidates list is empty')
    else:
        for name, count in votes.items():
            print(f'{name}: {count} votes')

def view_winner():
    if not votes:
        print('Candidates list is empty')
    else:
        winner = 0
        winner_name = 'Arnold'
        for i in votes:
            if votes[i] > winner:
                winner = votes[i]
                winner_name = i
        print(f'The winner is {winner_name} with total votes {winner}')

def reset_votes():
    for name in votes:
        votes[name] = 0
        print('all votes have been reset')
while True:
    print('\n *** Voting System ***')
    print('1. add_candidates')
    print('2. cast_vote')
    print('3. view_result')
    print('4. view_winner')
    print('5. reset_votes')
    print('6. exit')

    choice = int(input('Enter your choice'))

    if choice == 1:
        add_candidates()

    elif choice == 2:
        cast_vote()

    elif choice == 3:
        view_result()

    elif choice == 4:
        view_winner()

    elif choice == 5:
        reset_votes()

    elif choice == 6:
        print('Exit')
        break

    else:
        print('invalid choice')
