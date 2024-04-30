from currency_converter import currency_converter
from password_generator import password_generator
from todo_list import todo_list
from weather_forecast import display_weather

while 1:
    print("""Choose one program you want to run.
    1. Todo List
    2. Currency Converter
    3. Password Generator
    4. Weather Forecast
Press Enter to close.""")

    try:
        choice = input("Select a program from above (1-4): ")
        if choice == "":
            break
        else:
            choice = int(choice)
    except ValueError:
        print("Invalid Value. Try again.")
        continue

    if choice == 1:
        todo_list()
    elif choice == 2:
        currency_converter()
    elif choice == 3:
        password_generator()
    elif choice == 4:
        display_weather()

