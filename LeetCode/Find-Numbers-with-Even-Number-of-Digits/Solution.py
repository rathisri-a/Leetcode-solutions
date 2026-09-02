function hasEvenDigits(num)
{    
    digitCount = 0
    while num is not 0
    {
        digit = num % 10
        digitCount = digitCount + 1
        num = num / 10
    }

    if digitCount % 2 == 0
        return true
    else
        return false
}