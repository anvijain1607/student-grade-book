
# ================================

# STUDENT GRADE BOOK

# ================================

# ---------- PART 1: the dictionary ----------

# YOUR CODE HERE

# Make a dictionary called grades with five students.

# Each key is a name and each value is a score.

# ---------- PART 2: class average ----------

# YOUR CODE HERE

# Make total = 0. Loop over grades and add each score to total.

# Divide total by len(grades) and print the class average.

# ---------- PART 3: highest score ----------

# YOUR CODE HERE

# Make top_name = "" and top_score = 0.

# Loop over grades. If a score is higher than top_score,

# save that name in top_name and that score in top_score.

# Print the highest scorer and the score.

# ---------- PART 4: look up a student ----------

# YOUR CODE HERE

# Ask for a student name with input().

# Print the score with .get(). Use "Not found" if the name is not in grades.

print("welcome to student grade book")
students={"Alice":99,"Sam":89,"Ram":75,"Rose":80, "Anvita":98}
total=0
for name in students:
    total+=students[name]
class_average=total/5
top_score=max(students,key=students.get)
low_score=min(students,key=students.get)
print("The class average is:",class_average)
print( "lowest scorer is: ",low_score)
print("Highest scorer is : ",top_score)
name=input("enter a name to look up a student: ")
print(name,":",students.get(name,"Not found"))

