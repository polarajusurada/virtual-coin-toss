import random

def coin_toss_simulation():
    while True:
        try:
            num_flips = int(input("Enter the number of coin flips: "))
            if num_flips <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        
        heads = 0
        tails = 0
        
        for _ in range(num_flips):
            if random.choice(["Heads", "Tails"]) == "Heads":
                heads += 1
            else:
                tails += 1
        
        total = heads + tails
        heads_percentage = (heads / total) * 100
        tails_percentage = (tails / total) * 100
        
        print(f"\nResults:")
        print(f"Heads: {heads} ({heads_percentage:.2f}%)")
        print(f"Tails: {tails} ({tails_percentage:.2f}%)")
        
        repeat = input("\nDo you want to flip again? (yes/no): ").strip().lower()
        if repeat not in ('yes', 'y'):
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    coin_toss_simulation()
