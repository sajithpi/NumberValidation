
# TODO:Validating number whether it is in minimum-max range
def validateNum(min,max,arr,num):
    if (num > min) & (num < max):
       return True;
    else:
        return False;

# TODO:Searching the user input values exist in disabled list
def b_search(arr,low,high,num):
    if(num<arr[-1]):
        if  high >= low:
            mid =int((high+low)/2)
            if arr[mid] == num:
                # Exists
                return True;
            elif arr[mid] > num:
                return b_search(arr,low,mid-1,num)
            else:
                return b_search(arr,mid+1,high,num)
        else:
            # Not Exists
            return False
    else:
        # Not Exists
        return -1

# Reading Minimum,Maximum values
ready=0
while(ready!=1):
    # Try block for evaluate user input
    try:
        min = int(input("Enter the minimum number: "))
        max = int(input("\nEnter the maximum number: "))
        ready = 1
    except ValueError:
        print("Only Integer values are accepted \n")
        ready=0
ch=1;
val = 0;
run=1;
disabled_numbers=[];
#TODO: It will loop until user want to stop giving input numbers to the disabled numbers list
while(ch!='0'):
    print("\n***Choices***\n\n1.Add Number\n2.Quit:\n");
    ch=input("Your choice: ");
    if ch=='1':
        # Try block for evaluate user input
        try:
            val = int(input("Enter your element: "))
            # TODO:Adding values in to disabled list
            disabled_numbers.append(int(val))
        except ValueError:
            print("Only Integer numbers are allowed as input")
    elif ch=='2':
        break;
    else:
        print("\nPlease Choose Proper number");

# Sorting the disabled number array and copying to new arr list
arr = sorted(disabled_numbers)
print("Disabled List: ",arr)
# This loop will run until the checking number not in disabled list
while(run!=0):
    num = int(input("Enter Your Checking Number: "))
    result = validateNum(min,max,arr,num)
    if(result==True):
        # print("True")
        search_result = b_search(arr,0,len(arr),num)
        if search_result == True:
            print(f"\n{num} Element exists in disabled numbers list")
            print(arr)
            num += 1
            run=1
        else:
            print(f"\n{num} Number is not exist in disabled list")
            run=0
    else:
        print("\nInvalid Output")
        run=0






