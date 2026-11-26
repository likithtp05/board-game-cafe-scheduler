def is_weekend(day):
    if day == "saturday" or day == "sunday":
        return True
    else:
        return False


def show_menu(day, total_seats, occupied, chess, carrom, rummy, poker):
    free = total_seats - occupied
    print()
    print("Day:", day.capitalize())
    print("Seats:", occupied, "/", total_seats, "| Free:", free)
    print("1. Chess (2 players) | Left:", chess, "| Fee: Rs. 50")
    print("2. Carrom (2-4 players) | Left:", carrom, "| Fee: Rs. 100")
    print("3. Rummy (2-6 players) | Left:", rummy, "| Fee: Rs. 150")
    print("4. Poker (2-8 players) | Left:", poker, "| Fee: Rs. 200")
    if is_weekend(day):
        print("Offer: 20% Weekend Offer (3 or more hours)")
    else:
        print("Offer: No Offer (Weekends 3+ hours only)")


def check_game(choice, players, chess, carrom, rummy, poker):
    if choice == 1:
        if chess == 0:
            print("Chess is not available.")
            return False
        if players != 2:
            print("Chess is only for 2 players.")
            return False
        return True
    elif choice == 2:
        if carrom == 0:
            print("Carrom is not available.")
            return False
        if players < 2 or players > 4:
            print("Carrom is for 2 to 4 players.")
            return False
        return True
    elif choice == 3:
        if rummy == 0:
            print("Rummy is not available.")
            return False
        if players < 2 or players > 6:
            print("Rummy is for 2 to 6 players.")
            return False
        return True
    elif choice == 4:
        if poker == 0:
            print("Poker is not available.")
            return False
        if players < 2 or players > 8:
            print("Poker is for 2 to 8 players.")
            return False
        return True
    else:
        print("Wrong game choice.")
        return False


def calculate_bill(players, hours, choice, day):
    seat_cost = 0
    for i in range(hours):
        seat_cost = seat_cost + (players * 100)

    if choice == 1:
        game_fee = 50
    elif choice == 2:
        game_fee = 100
    elif choice == 3:
        game_fee = 150
    else:
        game_fee = 200

    total = seat_cost + game_fee

    if is_weekend(day) and hours >= 3:
        discount = total * 0.20
    else:
        discount = 0

    final_amount = total - discount
    return seat_cost, game_fee, discount, final_amount


def cafe_booking():
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = input("Enter day (Monday to Sunday): ").lower()
    while day not in days:
        print("Invalid day.")
        day = input("Enter day (Monday to Sunday): ").lower()

    total_seats = 20
    occupied = 0
    chess = 3
    carrom = 2
    rummy = 2
    poker = 2
    total_income = 0
    bookings = 0
    again = "yes"

    while again == "yes":
        free = total_seats - occupied
        if free == 0:
            print("All seats are full.")
            break
        if chess == 0 and carrom == 0 and rummy == 0 and poker == 0:
            print("All games are booked.")
            break

        show_menu(day, total_seats, occupied, chess, carrom, rummy, poker)

        players = int(input("Enter number of players: "))
        while players <= 0:
            print("Enter at least 1 player.")
            players = int(input("Enter number of players: "))

        if players > free:
            print("Not enough seats. Only", free, "left.")
        else:
            choice = int(input("Choose game (1-Chess, 2-Carrom, 3-Rummy, 4-Poker): "))
            if check_game(choice, players, chess, carrom, rummy, poker):
                hours = int(input("Enter hours: "))
                while hours <= 0:
                    print("Enter at least 1 hour.")
                    hours = int(input("Enter hours: "))

                occupied = occupied + players
                if choice == 1:
                    chess = chess - 1
                elif choice == 2:
                    carrom = carrom - 1
                elif choice == 3:
                    rummy = rummy - 1
                else:
                    poker = poker - 1

                seat_cost, game_fee, discount, final_amount = calculate_bill(players, hours, choice, day)
                bookings = bookings + 1
                total_income = total_income + final_amount

                print()
                print("Booking Confirmed - No.", bookings)
                print("Day:", day.capitalize())
                print("Hours:", hours)
                print("Seat Cost: Rs.", round(seat_cost, 2))
                print("Game Fee: Rs.", round(game_fee, 2))
                if discount > 0:
                    print("Weekend Offer (20%): -Rs.", round(discount, 2))
                elif is_weekend(day):
                    print("Offer: Rs. 0 (Need 3 or more hours)")
                else:
                    print("Offer: Rs. 0 (Weekday)")
                print("Final Bill: Rs.", round(final_amount, 2))

        again = input("Book another? (yes/no): ").lower()

    print()
    print("Day Summary -", day.capitalize())
    print("Total Bookings:", bookings)
    print("Seats Occupied:", occupied, "/", total_seats)
    print("Total Income: Rs.", round(total_income, 2))


cafe_booking()
