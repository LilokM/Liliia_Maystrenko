def reverse(st):
    words_list = st.split()
    result=" ".join(words_list[::-1])
    return result

str_list = ["Hello World!", "Hi There."]
for string in str_list:
    print(reverse(string))

