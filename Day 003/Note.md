The program employs a single traversal approach to check array is sorted or not. This ensures efficiency with a time complexity of O(n), where n is the size of the array.

# ALGORITHM STEP:-

### Step 1 Initialization:

The variables "arr" contain list of values.

### Step 2 Iteration Through Array:

def is_sorted function:<br>
&nbsp;&nbsp;&nbsp;For each num in the array:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compare the num greater than num + 1:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If it is greater, return False.<br>
&nbsp;&nbsp;&nbsp;otherwise return True.

### Step 3 Result:

After completing the loop, "is_sorted" function return true or false according array..

# Time and Space Complexity

Time Complexity : O(n)<br>
Space Complexity : O(1) 
