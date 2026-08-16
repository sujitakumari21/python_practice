# PARAGRAPH
paragraph = """
Python is one of the most popular programming language in the world .
it is simple to learn, easy to read , and widely used for web development,
data science, artificial intelligence, automation, and software development ,
practicing typing regularly helps improve your typing speed and accuracy .
"""
print("="*70)
print("     PYTHON TYPING SPEED TEST     ")
print("=" * 70)

print("\nType the following paragraph exactly as shown . \n")
print(paragraph)
input("\nPress Enter whin you are ready to start .....")
print("\nStart Typing Below:\n")

#Start Timer

start_time = time.time()
typed_text = input()

#End timer 

end_time = time.time()

#...................................................................
#Time calculation

#-------------------------------------------------------------------
time_taken = end_time - start_time
#-------------------------------------------------------------------

#Word calculation
#------------------------------------------------------------------
original_words = paragraph.strip().sprit()
type_words = typed_text.strip().split

total_words = len(typed_words)
correct_words = 0
for i in range(min(len(original_words), len(type_words))):
    if original_words[i]== type_words[1]:
        correct_words += 1

#-----------------------------------------------------------------------
#Accuracy calculation
#-----------------------------------------------------------------------

if len(original_words) > 0:
    accuracy = (correct_words / len(original_words))*100
else:
    accuracy=0
#------------------------------------------------------------------------
#Typing 
