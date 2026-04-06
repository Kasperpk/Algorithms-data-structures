def repetitions(input_string):
    longest_subsquence = 1
    max_subsequence = 1
    i = 0
    while i <= len(input_string):
            if i+1 < len(input_string) and input_string[i] == input_string[i+1]: 
                while i+1 < len(input_string) and input_string[i] == input_string[i+1]:
                    longest_subsquence += 1
                    i+=1
                if longest_subsquence > max_subsequence:
                     max_subsequence = longest_subsquence
            longest_subsquence = 1
            i+=1
    return max_subsequence 


if __name__ == '__main__':
     input_string = input()
     result = repetitions(input_string=input_string)
     print(result)

