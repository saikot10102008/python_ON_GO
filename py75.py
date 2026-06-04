# =====================================================
# FORMAT SPECIFIERS IN PYTHON
# Using {:flags} inside f-strings for formatting values
# =====================================================

print("=== Format Specifiers in f-strings ===\n")

# Basic examples
price = 1234.5678
item = "Coffee"

print(f"Basic: {item} costs ${price}")

# :.2f  = Round to 2 decimal places (fixed point)
print(f"Rounded to 2 decimals: ${price:.2f}")

# :.0f  = Round to 0 decimal places
print(f"Rounded to whole number: ${price:.0f}")

# :,    = Add comma as thousand separator
print(f"With comma separator: ${price:,.2f}")


print("\n=== Alignment and Width ===\n")

# :(number) = Allocate that many spaces (right aligned by default)
print(f"Right aligned (10 spaces): {item:>10}")

# :<     = Left aligned
print(f"Left aligned (10 spaces): {item:<10}")

# :^     = Center aligned
print(f"Centered (10 spaces): {item:^10}")


print("\n=== Zero Padding ===\n")

number = 42

# :0(number) = Zero pad to that many digits
print(f"Zero padded to 5 digits: {number:05}")
print(f"Zero padded to 8 digits: {number:08}")


print("\n=== Multiple Format Specifiers ===\n")

pi = 3.1415926535

print(f"Pi (default): {pi}")
print(f"Pi (3 decimals): {pi:.3f}")
print(f"Pi (right aligned 10 chars): {pi:10.3f}")
print(f"Pi (centered 12 chars): {pi:^12.4f}")


print("\n=== Combining Multiple Format Specifiers at Once ===\n")

# You can combine several specifiers in one placeholder
value = 12345.6789

print(f"Combined - Comma + 2 decimals: ${value:,.2f}")
print(f"Combined - Right align 15 chars + 2 decimals: {value:>15.2f}")
print(f"Combined - Center + comma + 1 decimal: {value:^20,.1f}")
print(f"Combined - Zero pad 8 digits + 3 decimals: {value:08.3f}")


print("\n=== Practical Examples ===\n")

# Example 1: Currency formatting
balance = 98765.4321
print(f"Account balance: ${balance:,.2f}")

# Example 2: Table-like output
products = [("Laptop", 1299.99), ("Mouse", 29.50), ("Keyboard", 89.99)]

print("\nProduct List:")
print("-" * 40)
for product, price in products:
    print(f"{product:<12} ${price:>10,.2f}")


print("\n=== Key Format Specifiers ===\n")
print("• :.nf     → Round to n decimal places")
print("• :,       → Thousand separator (comma)")
print("• :>n      → Right align in n spaces")
print("• :<n      → Left align in n spaces")
print("• :^n      → Center align in n spaces")
print("• :0n      → Zero pad to n digits")
print("• :n.mf    → Width n, m decimals")
print("• You can combine them: e.g. :>12,.2f")

