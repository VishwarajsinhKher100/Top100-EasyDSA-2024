The program employs a single traversal approach to remove duplicated values from array.

# ALGORITHM STEP:-

### Step 1 Initialization:

sorted_arr which contain list of value in sorted manner.

### Step 2 remove duplicated function:

define remove_duplicated function:
&nbsp;&nbsp;&nbsp;initializes empty "unique_arr" array.<br>
&nbsp;&nbsp;&nbsp;For each element in the array:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if unique_arr is empty or current number is not equal to last element of unique_arr:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;then add number to unique_arr.<br>
&nbsp;&nbsp;&nbsp;return unique_arr.

### Step 3 Result:

After completing the loop, function return unique elements.

# Time and Space Complexity

Time Complexity : O(n)<br>
Space Complexity : O(n) 
