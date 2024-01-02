
def solution(s: str):
    letters_and_numbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    new_string = ""
    i = 0
    while i < len(s):
        if s[i] == "%":
            if s[i+1] in letters_and_numbers and s[i-1] != "%":
                new_string += "{}"
                i += 1
            else:
                if s[i-1] != "%":
                    new_string += s[i]
                
        else:
            new_string += s[i]
            if s[i-1] == "%" and s[i-2] == "%" and s[i-3] == "%":
                new_string = "%" + new_string
          
        i += 1
    return new_string








# test 
s = "We expect the %f%% growth this week"
print(solution(s)) # We expect the {}% growth this week
s = "%d%d%%-growth in products is expected quite soon" 
print(solution(s)) # "{}{}%-growth in products is expected quite soon"
s = "%%%%x"
print(solution(s)) # "%%x"