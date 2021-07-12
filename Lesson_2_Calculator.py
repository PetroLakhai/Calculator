# --------------------------------------------------------------------------------------------------
# CONSTANTS
# --------------------------------------------------------------------------------------------------

symbol_ender_text = 'Please, enter symbol (use + or - or * or /): '
symbol_ender_no_division_text = 'Please, enter symbol (use + or - or *): '


# --------------------------------------------------------------------------------------------------
# FUNCTIONS 
# Python does not read them until you call it, like: int_value1 = get_input_number(order_number="first")
# --------------------------------------------------------------------------------------------------

def get_input_number(order_number):
    """
    Returns the input number to calculate and checks the int and float type.
    """
    enter_number_text = f'Please, enter the {order_number} number: '
    int_value = input(enter_number_text)
    if int_value == 'EXIT':
        exit()
    else:
        pass
    
    condition = True
    while condition:

        try:
            float(int_value) 
            float(int_value)
            break

        except ValueError:
            print('It is not a number, please enter a number!')
            int_value = input(enter_number_text)
            condition = False

        condition = True

    return float(int_value)


def validate_incoming_symbols(symbol):
    """
    Checks the incomming symbol and ZeroDivision for the second number.
    Returns
    """
    while symbol not in ["+", "-", "*", "/"]:
        print('It is not a math symbol, please, use +, -, *, /!')
        symbol = input(symbol_ender_text)

    while int_value2 == 0 and symbol in ['/', '']:
        if symbol == '/':
            print ('You can`t divide by 0!')
            symbol = input(symbol_ender_no_division_text)
        else:
            print ('You didn`t write a symbol!')
            symbol = input(symbol_ender_no_division_text)
    return symbol


def get_result(math_operations, validated_symbol):
    result = math_operations[validated_symbol]  # search a symbol as a key "+" and returns 'int_value1 + int_value2'
    print(result)
    return result 


def get_math_operation():
    symbol = input(symbol_ender_text)  # User entered the symbol: /, +, a, q, " "
    validated_symbol = validate_incoming_symbols(symbol)  # +, -, *,  /

    if validated_symbol != '/':
        math_operations = {
            '+': int_value1 + int_value2,
            '-': int_value1 - int_value2,
            '*': int_value1 * int_value2,
        }
    else:
        math_operations = {
            '/': int_value1 / int_value2,
        }
    return math_operations, validated_symbol


# --------------------------------------------------------------------------------------------------
# RUN SCRIPT
# --------------------------------------------------------------------------------------------------

print("If you want to close the calculator, please write EXIT, instead number! ")
int_value1 = get_input_number(order_number="first")  # User enters first number
int_value2 = get_input_number(order_number="next")  # User enters second number
math_operations, validated_symbol = get_math_operation()

while True:
    int_value1 = get_result(math_operations, validated_symbol) # Result from previus action
    int_value2 = get_input_number(order_number="next")  # User enters second number
    math_operations, validated_symbol = get_math_operation()
       