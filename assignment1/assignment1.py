# Task 1:
def hello():
    return ("Hello!")

hello()
print("------------------------------------------------------")
#Task 2:
def greet(name):
    return (f"Hello, {name}!")
greeting = greet("James")
print(greeting)
print("------------------------------------------------------")
#Task 3:
def calc(x,y,operation="multiply"):
    try:
        if operation == "add":
            return x + y
        elif operation == "subtract":
            return x - y
        elif operation == "multiply":
            return x * y
        elif operation == "divide":
            return "You can't divide by 0!" if y == 0 else x / y
        elif operation == "modulo":
            return x % y
        else:
            return "You can't multiply those values!"
    except TypeError:
        return "You can't multiply those values!"
    
print(calc(5,6))
print(calc(5,6,"add"))
print(calc(20,5,"divide"))
print(calc(14,2.0,"multiply"))
print(calc(12.6, 4.4, "subtract"))
print(calc(9,5, "modulo"))
print(calc(10,0,"divide"))
print(calc("first", "second", "multiply"))
print("------------------------------------------------------")

#Task 4: Data Type Conversion

def data_type_conversion(value,name):
    try:
        if name == "int":
            return int(value)
        elif name == "float":
            return float(value)
        elif name == "str":
            return str(value)  
        else:
            return f"You can't convert {value} into a {name}."
    except:
        return f"You can't convert {value} into a {name}."

print(data_type_conversion("101", "int"))     #101
print(data_type_conversion("5.5", "float"))   #5.5
print(data_type_conversion(7,"float"))         #7.0
print(data_type_conversion(91.1,"str"))        #"91.0"
print(data_type_conversion("banana", "int"))   #"You can't convert banana into a int."

print("------------------------------------------------------")

#Task 5:
# def test_grade():
#     assert a1.grade(75,85,95) == "B"
#     assert a1.grade("three", "blind", "mice") == "Invalid data was provided." 

def grade(*args):
    try:
        if args:
            sum = 0
            for n in args:
                sum = sum + n
                count = len(args)
            average = sum / count
        if average >= 90:
            return "A"
        elif 80 <= average < 90:
            return "B"
        elif 70 <= average < 80:
            return "C"
        elif 60 <= average < 70:
            return "D"
        elif average < 60:
            return "F"
        else: 
            return "Invalid data was provided."
    except:
        return "Invalid data was provided."       

print(grade(75,85,95))  #B
# print(grade(40,15))    #F
print(grade("three", "blind", "mice")) #"Invalid data was provided".

print("------------------------------------------------------")
#Task 6: Use a For Loop with a Range
# def test_repeat():
#     assert a1.repeat("up,", 4) == "up,up,up,up,"

def repeat(string, count):
    for s in range(4):
        return string * count

print(repeat("up,", 4))

print("------------------------------------------------------")

#Task 7: Student Scores, Using **kwargs
# def test_student_scores():
#     assert a1.student_scores("mean", Tom=75, Dick=89, Angela=91) == (75 + 89 + 91) / 3
#     assert a1.student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50 ) == "Angela"

def student_scores(option,**kwargs):
    if option == "mean":
        scores = kwargs.values()
        return sum(scores) / len(scores)
    elif option == "best":
        return max(kwargs, key=kwargs.get)
    else:
        return "Invalid option"
        

print(student_scores("mean", Tom=75, Dick=89, Angela=91))      #(75 + 89 + 91) / 3
print(student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50)) #"Angela"

print("------------------------------------------------------")
#Task 8: Titleize, with String and List Operations
def titleize(words):
    words = words.split()
    little_words = ["a", "an", "the", "and", "on", "in", "of", "is"]
    for i,word in enumerate(words):
        if i == 0 or i ==len(words) -1 or word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()               
    return " ".join(words)
print(titleize("war and peace"))  #"War and Peace"
print(titleize("a separate peace")) #"A Separate Peace"
print(titleize("after on"))  #"After On"

print("------------------------------------------------------")
#Task 9
def hangman(secret, guess):
    return "".join(letter if letter in guess else "_" for letter in secret)

print(hangman("difficulty", "ic"))  # _i_ic___

print("------------------------------------------------------")
#Task 10: Pig Latin, Another String Manipulation Exercise

def pig_latin(sentence):
    words = sentence.split()
    vowels = "aeiou"
    pig_latin_words = []
    
    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(word + "ay")
        elif word.startswith("qu"):
            pig_latin_words.append(word[2:] + "quay")
        else:
            if "qu" in word:
                qu_index = word.index("qu") + 2
                pig_latin_words.append(word[qu_index:] + word[:qu_index] + "ay")
            else:
                for i, letter in enumerate(word):
                    if letter in vowels:
                        pig_latin_words.append(word[i:] + word[:i] + "ay")
                        break
         
    return " ".join(pig_latin_words)
        
print(pig_latin("apple"))      #"appleay"
print(pig_latin("banana"))     #"ananabay"
print(pig_latin("cherry"))     #"errychay"
print(pig_latin("quiet"))      #"ietquay"
print(pig_latin("square"))     #"aresquay"
print(pig_latin("the quick brown fox"))  #"ethay ickquay ownbray oxfay"

