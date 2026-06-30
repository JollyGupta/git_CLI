
# Monday: Your code works
def calculate_price(amount):
    return amount * 1.20  # 20% markup

price = 20

print("=== Monday ===")
print(f"Original Price : ${price}")
print(f"Final Price    : ${calculate_price(price):.2f}")


# --------------------------------------------------

# Tuesday: Boss wants 25% markup
def calculate_price(amount):
    return amount * 1.25  # Changed from 20% to 25%

print("\n=== Tuesday ===")
print(f"Original Price : ${price}")
print(f"Final Price    : ${calculate_price(price):.2f}")


# --------------------------------------------------

# Wednesday:
# Boss: "Actually, can we go back to 20%?"
#
# With Git:
#     git log
#     git checkout <Monday_commit>
#
# Without Git:
#     You have to manually remember and rewrite the old code!

print("\n=== Wednesday ===")
print("Boss: Let's go back to Monday's version!")

# Restored Monday's code
def calculate_price(amount):
    return amount * 1.20

print(f"Original Price : ${price}")
print(f"Final Price    : ${calculate_price(price):.2f}")

print("\nThanks to Git, restoring old code takes only a few seconds!")