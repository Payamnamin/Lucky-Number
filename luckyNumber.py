import random

def get_player_name():
    """Frågar användaren om deras fullständiga namn och validerar det."""
    while True:
        player_name = input("Enter your full name (First Last): ").strip()
        # Kontrollerar att namnet består av exakt två delar utan siffror
        if len(player_name.split()) == 2 and all(part.isalpha() for part in player_name.split()):
            return player_name
        print("Invalid input. Please enter your full name with only letters.")

def get_birthdate():
    """Frågar användaren om deras födelsedatum och validerar det."""
    while True:
        birthdate = input("Enter your birthdate (yyyymmdd): ")
        # Kontrollerar att födelsedatumet följer formatet yyyymmdd
        if len(birthdate) == 8 and birthdate.isdigit():
            year, month, day = int(birthdate[:4]), int(birthdate[4:6]), int(birthdate[6:8])
            # Validerar år, månad och dag
            if year > 1900 and 1 <= month <= 12 and 1 <= day <= 31:
                return birthdate
        print("Invalid birthdate. Please try again.")

def calculate_age(birthdate):
    """Beräknar spelarens ålder baserat på födelsedatum."""
    year = int(birthdate[:4])
    return 2022 - year

def generate_lucky_list():
    """Genererar en lista med 9 lyckonummer och ett huvudlyckonummer."""
    lucky_list = random.sample(range(101), 9)  # 9 unika nummer mellan 0 och 100
    lucky_number = random.randint(0, 100)  # Ett lyckonummer
    lucky_list.append(lucky_number)  # Lägger till lyckonumret i listan
    return lucky_list, lucky_number

def main():
    """Huvudfunktionen som kör spelet."""
    player_name = get_player_name()  # Hämtar spelarens namn
    
    while True:
        player_birthdate = get_birthdate()  # Hämtar och validerar födelsedatum
        player_age = calculate_age(player_birthdate)  # Beräknar ålder
        
        if player_age >= 18:  # Kollar om spelaren är minst 18 år gammal
            break
        print("You must be at least 18 years old. Please re-enter your birthdate.")

    tries_count = 0  # Räkna försök
    while True:
        lucky_list, lucky_number = generate_lucky_list()  # Generera lyckonummer
        print("Lucky List:", lucky_list)  # Visa lyckolistan
        
        player_input = int(input("Pick a lucky number from the lucky list: "))  # Spelaren gör ett val
        tries_count += 1  # Öka antalet försök
        
        if player_input == lucky_number:  # Kollar om valet är rätt
            print(f"Congrats, game is over! And you got lucky number from try#{tries_count} :)")
            if input("Do you like to play again? (y/n): ").lower() != 'y':
                break
        else:
            # Skapa en ny lista med nummer inom 10 av det lyckonumret
            shorter_lucky_list = [num for num in lucky_list if lucky_number - 10 <= num <= lucky_number + 10]
            print(f"This is try#{tries_count} and new list is: {shorter_lucky_list}, choose the lucky number?")
            while True:
                player_input = int(input("Pick a lucky number from the new list: "))  # Nytt val
                if player_input in shorter_lucky_list:  # Kolla om valet finns i den nya listan
                    if player_input == lucky_number:
                        print(f"Congrats, game is over! And you got lucky number from try#{tries_count} :)")
                        break
                    else:
                        shorter_lucky_list.remove(player_input)  # Ta bort felaktigt val
                        if len(shorter_lucky_list) <= 2:  # Kolla om det bara finns två nummer kvar
                            print("Game over! Only two numbers left. You couldn't find the lucky number.")
                            break
                else:
                    print("Number not in list. Try again.")

if __name__ == "__main__":
    main()  # Starta spelet