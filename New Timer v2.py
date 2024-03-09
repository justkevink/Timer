import time

# Recursive function
def countdown(start_number):
    start_number -= 1
    return start_number

run = True
while run:

# User makes a selection
# If invalid selection, ask again

    select = True
    while select:
        timer = int(input("Select a timer: "
                          "\n\n (1) = 5 secs "
                          "\n (2) = 10 secs "
                          "\n (3) = 15 secs "
                          "\n (4) = 30 secs "
                          "\n (5) = 60 secs"
                          "\n\n>>> "))
        if timer not in range(1,6):
            select = True
            print("\n!Invalid selection!\n")
            time.sleep(1)
        else:
            select = False

# Assign value numeric value to start number

    if timer == 1:
        start_number = 5
    elif timer == 2:
        start_number = 10
    elif timer == 3:
        start_number = 15
    elif timer == 4:
        start_number = 30
    elif timer == 5:
        start_number = 60
    if start_number > 1:
        count = True
        print("\nTimer start!\n")
        print(start_number, end=" ")
        # 1 second delay
        time.sleep(1)

        while count:

            # Calls function to return and print new number
            start_number = countdown(start_number)
            print(f"\r{start_number} ", end="")

            # 1 second delay
            time.sleep(1)

            if start_number == 1:
                count = False

    print("\rTime's up!")
    if not input("Start a new timer? (y/n): ") == "y":
        run = False