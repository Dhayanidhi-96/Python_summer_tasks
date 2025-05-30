file = open("D:\python\Python_summer_tasks\Task_04\sample.txt","r")
content = file.read()
file.close()

#count charcters(including spaces and newlines)
charcter_count = len(content)

#count lines
file = open("D:\python\Python_summer_tasks\Task_04\sample.txt","r")
lines = file.readlines()
file.close()

line_count = 0
for line in lines:
    line_count += 1

words = content.split()
word_count = 0
for word in words:
    word_count += 1

punctuations =  ".,!,?,;,:"
cleaned_words =[]
for word in words :
    word = word.lower()
    for p in punctuations:
        word = word.strip(p)
    cleaned_words.append(word)
print(cleaned_words)

word_frequency = {}
for word in cleaned_words:
    if word in word_frequency:
        word_frequency[word] += 1
    else :
        word_frequency[word]=1

sorted_words = sorted(word_frequency.items(),key=lambda item: item[1],reverse=True)
top_5 = sorted_words[:5]

# Print results
print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", charcter_count)
print("Most Frequent Words:")
for word, count in top_5:
    print(word + ":", count)