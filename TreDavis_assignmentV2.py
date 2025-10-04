# Part 1
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number:"))
step_count = 0
print(" Sequence:", current_number, end=" ")
while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
        
    else:
        current_number = (current_number * 3) + 1
    
    step_count = step_count + 1
    print(current_number, end=" ")

print("\nSteps:", step_count)
print()
#part 2
print("=== Challenge 2: Prime Number Checker ===")
user_input = int(input(f"Enter a number: "))
print(f"Testing divisors from 2 to {user_input - 1}...") 

for num in range(2, (user_input - 1)):
    if user_input % num == 0:
        user_input / 2
        print(f"{user_input} is not prime (divisible by 3)")
        break

else:
    print(f"{user_input} is prime!")

print()