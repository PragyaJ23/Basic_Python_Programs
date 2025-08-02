def count_special_characters(n):
    special_characters="@#$^*&^%!"
    count=0
    for i in n:
        if i in special_characters:     #special_characters find
            count+=1
    return count
text=input("enter string")
print(count_special_characters(text))