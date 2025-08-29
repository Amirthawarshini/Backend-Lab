def number_to_words(n):
    to19 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
            'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen',
            'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    
    # Words for tens multiples
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty',
            'Sixty', 'Seventy', 'Eighty', 'Ninety']

    # Recursive function to convert number to words
    def words(num):
        if num < 20:
            return to19[num]
        elif num < 100:
            return tens[num // 10] + ('' if num % 10 == 0 else ' ' + to19[num % 10])
        elif num < 1000:
            return to19[num // 100] + ' Hundred' + ('' if num % 100 == 0 else ' and ' + words(num % 100))
        else:
            return words(num // 1000) + ' Thousand' + ('' if num % 1000 == 0 else ' and ' + words(num % 1000))

    return words(n)

# Get number input from the user
try:
    user_input = int(input("Enter a number (0 - 9999): "))
    if 0 <= user_input <= 9999:
        print("In words:", number_to_words(user_input))
    else:
        print("Please enter a number between 0 and 9999.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
