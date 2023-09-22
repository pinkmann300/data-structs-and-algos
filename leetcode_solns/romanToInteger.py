def romanToInt(self, s: str) -> int:
    int_val = 0
    prev_char = ""

    char_list = ['I','V','X','L','C','D','M']
    num_val = [1,5,10,50,100,500,1000]

    for i in range(len(s)):
        current_char = s[i]
        if (((current_char == 'V') or (current_char == 'X')) and (prev_char == 'I')) or (((current_char == 'L') or (current_char == 'C')) and (prev_char == 'X')) or (((current_char == 'D') or (current_char == 'M')) and (prev_char == 'C')) :
            int_val = int_val + (num_val[char_list.index(current_char)] - 2* num_val[char_list.index(prev_char)])
        else:
            int_val += num_val[char_list.index(current_char)]
        
        prev_char = current_char

    return int_val

