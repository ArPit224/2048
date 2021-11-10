import mesh_functions as mf

def test(input):
    i = 0 + k
    while i<=input:
        print("test")
        i += 1



def up(input):
    # checking in first row 0 4 8 12, second row 1, 5, 9, 13 etc etc 
    #DONE
    
    k = 0
    while k < 4:
        i = 0
        while i < 3:
            if input[4 + k] == input[0 + k] or input[k] == 0:

                input[0 + k] = input[4 + k] + input[0 + k]
                input[4 + k] = input[8 + k]
                input[8 + k] = input[12 + k]
                input[12 + k] = 0

            if input[8 + k] == input[4 + k] or input[4 + k] == 0:

                input[4 + k] = input[8 + k] + input[4 + k]
                input[8 + k] = input[12 + k]
                input[12 + k] = 0

            if input[12 + k] == input[8 + k] or input[8 + k] == 0:

                input[8 + k] = input[12 + k] + input[8 + k]
                input[12 + k] = 0

            i += 1
        k += 1
     

def down(input):
    # checking in first row 0 4 8 12, second row 1, 5, 9, 13 etc etc 
    #Done
    
    k = 0
    while k < 4:
        i = 0
        while i < 3:

            if input[k + 12] == input[k + 8] or input[k + 12] == 0:

                input[k + 12] = input[k + 12] + input[k + 8]
                input[k + 8] = input[k + 4]
                input[k + 4] = input[k + 0]
                input[k + 0] = 0

            if input[k + 8] == input[k + 4] or input[k + 8] == 0:

                input[k + 8] = input[k + 4] + input[k + 8]
                input[k + 4] = input[k + 0]
                input[k + 0] = 0

            if input[k + 4] == input[k + 0] or input[k + 4] == 0:

                input[k + 4] = input[k + 0] + input[k + 4]
                input[k + 0] = 0

            i += 1
        k += 1


def right(input):
    # checking in first column 0 1 2 3, second row 4, 5, 6, 7 etc etc 
    #Done
    
    k = 0
    while k < 4:
        i = 0
        while i < 3:

            if input[4 * k + 3] == input[4 * k + 2] or input[4 * k + 3] == 0:

                input[4 * k + 3] = input[4 * k + 2] + input[4 * k + 3]
                input[4 * k + 2] = input[4 * k + 1]
                input[4 * k + 1] = input[4 * k + 0]
                input[4 * k + 0] = 0

            if input[4 * k + 2] == input[4 * k + 1] or input[4 * k + 2] == 0:

                input[4 * k + 2] = input[4 * k + 2] + input[4 * k + 1]
                input[4 * k + 1] = input[4 * k + 0]
                input[4 * k + 0] = 0

            if input[4 * k + 1] == input[4 * k + 0] or input[4 * k + 1] == 0:

                input[4 * k + 1] = input[4 * k + 0] + input[4 * k + 1]
                input[4 * k + 0] = 0

            i += 1
        k += 1


def left(input):
    # checking in first column 0 1 2 3, second row 4, 5, 6, 7 etc etc 
    #not Done
    
    k = 0
    while k < 4:
        i = 0
        while i < 3:
            if input[4 * k + 0] == input[4 * k + 1] or input[4 * k] == 0:

                input[4 * k + 0] = input[4 * k + 0] + input[4 * k + 1]
                input[4 * k + 1] = input[4 * k + 2]
                input[4 * k + 2] = input[4 * k + 3]
                input[4 * k + 3] = 0
            
            if input[4 * k + 1] == input[4 * k + 2] or input[4 * k + 1] == 0:

                input[4 * k + 1] = input[4 * k + 2] + input[4 * k + 1]
                input[4 * k + 2] = input[4 * k + 3]
                input[4 * k + 3] = 0
            
            if input[4 * k + 2] == input[4 * k + 3] or input[4 * k + 2] == 0:

                input[4 * k + 2] = input[4 * k + 3] + input[4 * k + 2]
                input[4 * k + 3] = 0
            
            i += 1
        k += 1





