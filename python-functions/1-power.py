import decimal

def pow(a, b):
    decimal.getcontext().prec = 30  # Set the precision to a sufficient number of decimal places
    a_decimal = decimal.Decimal(str(a))
    result = decimal.Decimal('1')
    
    if b >= 0:
        for _ in range(b):
            result *= a_decimal
    else:
        for _ in range(abs(b)):
            result /= a_decimal

    return int(result)
