n =254585
m =25425
c =5
print()
print(">>>>>>>>>>>>>>>>>>>>hello Guys so today we will create formulas for example \"binomial theorem\". \n>>>>>>>>>>>>>>>>>>>>and we will prove that \"LHS=RHS\"")
print()
# First equation
print("                    <---------------{prove this formula \"a2 + b2= (a - b)2 +2ab\"}----------------->")
print("so this is answer \n\"LHS=RHS\"",n * n + m * m, "=", (n - m) * (n - m) + 2 * n * m)
# second equation
print()
print("                    <---------------{prove this formula \"a² - b²= (a - b)(a + b)\"}----------------->") 
print("so this is answer \n\"LHS=RHS\"", n * n - m * m, "=", (n - m) * (n + m))
# third equation
print()
print("                    <---------------{prove this formula \"(a + b)2 = a2 + b2 + 2ab\"}----------------->") 
print("so this is answer \n\"LHS=RHS\"", (n + m) * (n + m), "=", (n * n) + (m * m) + 2 * n * m)
# forth equation
print()
print("                    <---------------{prove this formula \"(a - b)2 = a2 + b2 - 2ab\"}----------------->") 
print("so this is answer \n\"LHS=RHS\"", (n - m) * (n - m), "=", (n * n) + (m * m) - 2 * n * m)
# fifth equation
print()
print("                    <---------------{prove this formula \"(a + b + c)2 = a2 + b2 - 2ab\"}----------------->") 
print("so this is answer \n\"LHS=RHS\"", (n + m + c) * (n + m + c), "=", (n * n) + (m * m) + (c * c)  + 2 * n * m + 2 * n * c + 2 * m * c)
# six equation
print()
print("                    <---------------{prove this formula \"(a + b + c)2 = a2 + b2 - 2ab\"}----------------->") 
print("so this is answer \n\"LHS=RHS\"", (n - m - c) * (n - m - c), "=", (n * n) + (m * m) + (c * c)  - 2 * n * m - 2 * n * c + 2 * m * c)
# seventh equation
print()
print("                    <---------------{prove this formula \"a3 - b3 = (a - b) (a2 + ab + b2)\"}----------------->") 
print("so this is answer \n\"LHS=RHS\"", (n * n * n ) - (m * m * m), "=", (n - m) * (n * n) + (n - m) * (n * m) + (n - m) * (m * m))
# eighth equation
print()
print("                    <---------------{prove this formula \"a3 + b3 = (a - b) (a2 - ab + b2)\"}----------------->") 
print("so this is answer \n\"LHS=RHS\"", (n * n * n ) + (m * m * m), "=", (n + m) * (n * n) - (n + m) * (n * m) + (n + m) * (m * m))

print()
print("                    <---------------{prove this formula \"(a + b)3 = a3 + 3a2b + 3ab2 + b3\"}----------------->") 
print("so this is answer \n\"LHS=RHS\"", (n + m) * (n + m) * (n +m), "=", (n * n * n) + (3 * n * n) * m + (3 * m * m) * n + (m * m * m))

print()
print("                    <---------------{prove this formula \"(a - b)3 = a3 - 3a2b + 3ab2 - b3\"}----------------->") 
print("so this is answer \n\"LHS=RHS\"", (n - m) * (n - m) * (n - m), "=", (n * n * n) - (3 * n * n) * m + (3 * m * m) * n - (m * m * m))
