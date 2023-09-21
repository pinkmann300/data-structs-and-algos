
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


"""




def convert(s: str, numRows: int) -> str:
    converted_str = ""
    #Initialise an empty string
    
    for j in range(numRows):
        for i in range(numRows-1):
            totalSkip = (2 * (numRows) - 2 - j)
            converted_str = converted_str + s[j + (i * totalSkip)]
    return converted_str


print(convert("PAYPALISHIRING",4))

