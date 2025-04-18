    Foods=[]

    def Add_foods():
        food = input('Add your foods')
        Foods.append(food)
        print(f'your food list have been added by {food}')

    def Display_foods_by_name():
        if not Foods:
            print('your list is empty')
        else:
            for i,y in enumerate(Foods):
                print(f'{i+1} your food list is {y}')

    def Remove_foods_by_name():
        if not Foods:
            print('your list in empty')

        else:
            removed_foods = input('Remove your foods by name')
            if removed_foods in Foods:
                Foods.remove(removed_foods)
                print(f'your food list have been removed by {removed_foods}')
            else:
                print(f"{removed_foods} not in your list")

    def Remove_foods_by_index():
        if not Foods:
            print('your list in empty')
        else:
            removed_foods_index = int(input('Remove your foods by index'))
            if removed_foods_by_index == Foods.pop(removed_foods_index -1):
                print(f'your food list have been removed by {removed_foods_by_index}')
            else:
                print(f"{removed_foods_by_index} not in your list")

    def Display_foods_by_index():
        if not Foods:
            print('your list is empty')
        else:
            display_by_index = int(input('Display foods by index'))
            if display_by_index < Foods.size():
                print(Foods[display_by_index])
            else:
                print('Index out of range')

while True:
    print('\n *** Food Manager ***')
    print('1. Add_foods')
    print('2. Remove_foods_by_name')
    print('3. Display_foods_by_name')
    print('4. Remove_foods_by_index')
    print('5. Display_foods_by_index')
    print('6. Exit')

    Choice = int(input('Enter your food from (1:6)'))

    if Choice == 1:
        Add_foods()

    elif Choice == 2:
        Remove_foods_by_name()

    elif Choice == 4:
        Remove_foods_by_index()

    elif Choice == 3:
        Display_foods()
    
    elif Choice == 5:
        Display_foods_by_index()

    elif Choice == 6:
        print('Exit the program')
        break
    else:
        print('Invalid Choice')
