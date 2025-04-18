numbers = []
file_path = "numbers.txt" 
with open(file_path, "r") as file:
    for line in file:
        line = line.strip()  
        print(line)  
        if line != "": 
            number = float(line)  
            numbers.append(number)
average = sum(numbers) / len(numbers)
print("avrage= ", average)