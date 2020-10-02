def menu():
	print("1. Sum of '2' and '3'")
	print("2. Multiplication of '2' and '3'")
	print("3. Cube of '2'")
	print("4. Area of 2 unit length Square")
	print("5. Perimeter of 2 unit wide and 3 unit length Rectangle")
def add(a,b):
    print(a+b)

def multiply(a,b):
    print(a*b)

def cube(a,b):
    print(a**b)

def square_area(a):
    area = a**2
    print(area)

def rectangle_perimeter(width, height):
    perimeter = (width + height)* 2
    print(perimeter)

if __name__ == "__main__":
	menu()
	inp = input("Enter Choice: ")
	if inp == '1':
		add(2,3)
	elif inp == '2':
		multiply(2,3)
	elif inp == '3':
		cube(2,3)
	elif inp == '4':
		square_area(2)
	elif inp == '5':
		rectangle_perimeter(2,3)
	else:
		print("Invalid Keyword !")
		
