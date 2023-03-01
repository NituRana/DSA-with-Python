'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April andgot a refund of 200$. Make a correction to your monthly expense list
based on this
'''
len = int(input("Enter the lengthof the array :- "))
arr = []
for i in range (len):
    element = int(input("Enter the array elements {} :- ".format(i)))
    arr.append(element)
print("This is your list of expense :- ", arr)

# ************************************** SOLUTION 1 **********************************************
feb_extra_exp = arr[1] - arr[2]
print("In the month feburary you expense "+str(feb_extra_exp)+" $ extra from january")

# ************************************** SOLUTION 2  ***********************************************
len = int(input("Enter the num of the month for count the total expenses of these months :- "))
arr = []
total = 0
for i in range (len):
    element = int(input("Enter the expense of month {} :- ".format(i)))
    total = total + element
    arr.append(element)
print(" This is your list of months :- ", arr)
print(" the total expense of these month is :- ", total)

# ************************************** SOLUTION 3  ***********************************************