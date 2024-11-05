def main():
    height = int(input("Enter the height of the triangle: "))
    pyramid(height)
            
def pyramid(height):
    for i in range(height + 1):
        print("#" * i)
              

if __name__ == "__main__":
    main()

