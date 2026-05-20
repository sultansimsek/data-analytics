with open("about_me.txt", "a") as f:
    pass

with open("about_me.txt", "a") as f:
    f.write("\nPerfect night out:\n")
    f.write("I'd start with dinner at a rooftop restaurant downtown,\n")
    f.write("then catch a live jazz set, and finish with late-night tacos.\n")

with open("about_me.txt", "r") as f:
    print(f.read()) 

    with open("about_me.txt", "r") as f:
     print(f.read(50))   
     print(f.read(50))

with open("about_me.txt", "r") as f:
    print(f.readline(10))   
    print(f.readline()) 

    for i in range(1, 5):
        print(f.readline())

with open("about_me.txt", "r") as f:
    print(f.readlines(1))    
    print(f.readlines(1))    
    print(f.readlines(10))   
    print(f.readlines(10))

with open("about_me.txt", "r") as f:

    
    first_50 = f.read(50)

    
    next_lines = []
    for i in range(1, 5):
        next_lines.append(f.readline())

        next_100 = f.readlines(100)

print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {next_lines}")
print(f"Next 100 characters, as list by line, rounded up: {next_100}")