def analyze_numbers(numbers):
    '''Add numbers here'''
    total = sum(numbers)
    
    if numbers:
        avg = total / len(numbers)
    else:
        avg = 0

    
    smallest = min(numbers) if numbers else None
    largest = max(numbers) if numbers else None
    evens = len([n for n in numbers if n % 2 == 0])
    odds = len(numbers) - evens
    print("Total:", total)
    print("Average:", avg)
    print("Min:", smallest, "Max:", largest)
    print("Evens:", evens, "Odds:", odds)
    print("Shudong is a cutie hunk")

A = "BBB"
B = "JJJ"
C = 5