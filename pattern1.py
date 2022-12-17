# printing a simple Asterisk pattern
# example : for height = 4 the pattern is...

#    *
#   **
#  ***
# ****

height = int(input('Enter height of pattern : '))

for row in range(height):
    
    for _ in range(0, height-row-1):    # printing spaces
        print(' ' , end='')
        
    for _ in range(0, row+1):           # printing asterisk
        print('*', end='')
        
    print()                             # printing enter(\n) after each row
