def sanitize():
    f = open("slang.txt" , "r")
    list_slang = f.read().strip().split()
    f.close()
    text = input("Your text: ")
    text = text.split()
    sanitized_text = ""
    for word in text:
        if word in list_slang:
            word = ''.join(['*']*len(word)) 
        sanitized_text += word + ' '
    print(sanitized_text)
    
    cho = input("do you want to add more slang to help us?(Y/n)")
    if(cho.lower()=='y'):
        new_slang = input("Then input your slang (Only slang word, other good words can harm this): ")
        if new_slang in list_slang:
            print("It's already imported!")
        else:    
            f = open("slang.txt" , "a")
            f.write(" " + new_slang)
            f.close()
            sanitize()
    elif cho == "n" or cho == "N":
        print("Thanks for using us")
    else:
        print("Invalid choice\n thanks for using us")        

if __name__ == '__main__':
    sanitize()
