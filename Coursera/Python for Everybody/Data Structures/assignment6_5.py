## Python for Everybody Coursera
## Assignment 6_5
## Gustavo Simas da Silva - 2017
## Python Data Structures, String Manipulation

text = "X-DSPAM-Confidence:    0.8475"
t = text.find('0')
new_text = text[t:]
result = float(new_text)
print(result)
