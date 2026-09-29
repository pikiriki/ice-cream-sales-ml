error_a = abs(90 - 100)
error_b = abs(90 - 80)
error_c = abs(126 - 120)

total_error = error_a + error_b + error_c
mae = total_error / 3

print("Absolute error A:", error_a)
print("Absolute error B:", error_b)
print("Absolute error C:", error_c)
print("Total absolute error:", total_error)
print("Mean absolute error:", mae)