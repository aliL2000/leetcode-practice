#Question can be found here:
#https://leetcode.com/problems/encode-and-decode-strings/

class Solution:
    #The delimiter in this case is : and we add the length of string too
    def encode(self, strs):
        result = ""
        for string in strs:
            #Add the length of the string with the delimiter
            result+=len(string)+":"+string
        return result 
    def decode(self, str):
        result, i = [],0
        while i < len(str):
            j=i
            while str[j] != ":":
                j += 1
            #determine the length of the string
            length = int(str[i:j])
            #Add the string to the array
            result.append(str[j+1:j+1+length])
            #Reset the index, and keep going for the next string
            i = j+1+length
        return result
