# 🚀 CONTROL FLOW & LOOPS IN PYTHON

# 🟢 Conditional Statements (if, elif, else)
print("\n\t\t\t🔹 CONDITIONAL STATEMENTS - Making decisions in Python\n")

age = int(input("Enter your age: "))  # Taking user input

if age >= 18:
    print("✅ You are eligible to vote because you are 18 or older.")
elif age == 17:
    print("⏳ Almost there! Just one more year until you can vote.")
else:
    print("❌ You are too young to vote. You must be at least 18 years old.")

# 🔄 Loops in Python

print("\n\t\t\t🔹 LOOPS - Used to repeat tasks multiple times")

# 🔸 While Loop
print("\n🔸 WHILE LOOP - Counting down from 5 to 1")
print("\nA while loop runs until a specified condition becomes False.")

count = 5
while count > 0:
    print(f"⏳ Countdown: {count}")  # Displaying current count
    count -= 1  # Decreasing count by 1

print("\n🚀 Lift off! The countdown is complete.")  # Executes after the loop ends


# 🔸 For Loop
print("\n\t\t\t🔸 FOR LOOP - Iterating over a list of fruits")
print("\nA for loop is used to iterate over a sequence (like a list, tuple, or string).")
fruits = ["🍏 Apple", "🍌 Banana", "🍒 Cherry"]
for fruit in fruits:
    print(f"\n📢 Currently processing: {fruit}")  # Displaying each fruit in the list

print("✅ All fruits have been processed!")  # After the loop ends


# 🔄 Loop Control Statements

print("\n🔹 LOOP CONTROL STATEMENTS - Modify loop execution")

# 🔸 Break Statement
print("\n🔸 BREAK - Stopping loop when 'Cherry' is found")
for fruit in fruits:
    if fruit == "🍒 Cherry":
        print("\n🍒 Found Cherry! Stopping the loop immediately.")
        break  # Exits the loop when "Cherry" is found
    print(f"\n✅ Processing: {fruit}")

print("\n🔚 Loop ended due to 'break' statement.")


# 🔸 Continue Statement
print("\n🔸 CONTINUE - Skipping 'Banana' and processing remaining items")
for fruit in fruits:
    if fruit == "🍌 Banana":
        print("\n🚫 Skipping Banana (continue statement used).")
        continue  # Skips the rest of the code for this iteration
    print(f"\n✅ Processing: {fruit}")

print("🏁 All fruits have been checked!")


# 🔸 Pass Statement
print("\n🔸 PASS - Placeholder for future code (does nothing for now)")
for fruit in fruits:
    if fruit == "🍌 Banana":
        pass  # To be implemented later
    print(f"\n✅ Currently processing: {fruit}")

print("\n🔚 The loop executed, but 'pass' didn't affect anything.")

