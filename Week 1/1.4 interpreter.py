def main():
    expression = input("Enter your expression in the appropriate format: ")
    x, y, z = expression.split(" ")
    print(binary_operation(x, y, z))

def binary_operation(a, b, c):
    a = int(a) #Given a number, change their datatype from "str" to "int"
    c = int(c) #Given a number, change their datatype from "str" to "int". Note that if we chose / for b and 0 for c, the program will crash
    match b: #The binary operator, with 4 possible options
        case "+":
            ans = a + c
            ans = float(ans)    #(+, -, *) on integers result in an integer, but python doesn't automatically convert its datatype to float
        case "-":
            ans = a - c
            ans = float(ans)
        case "*":
            ans = a * c
            ans = float(ans)
        case "/":
            ans = a / c #The datatype for result of / is already float, no conversion needed
    ans = round(ans, 1)
    return ans

main()
