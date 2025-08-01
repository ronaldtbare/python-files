# Lesson Plan: If-Else Statements in Python  
**Duration:** 3 sessions (45 minutes each)  
**Target Audience:** Beginner Python learners  
**Objective:** Students will understand and implement if-else conditional statements in 
Python.  

---

### **Session 1: Introduction to If-Else Statements**  
**Time:** 45 minutes  

**Materials:** Whiteboard, laptops, Python code editor  

**Learning Outcomes:**  
1. Understand the basic syntax of if-else statements.  
2. Practice writing simple conditional logic.  

**Activities:**  
1. **Introduction (10 minutes):**  
   - Explain the purpose of if-else statements (decision-making in code).  
   - Show example: `if condition: print("Condition is true") else: print("Condition is 
false")`.  

2. **Code Example (15 minutes):**  
   - Write a simple program to check if a number is even or odd.  
   ```python
   number = int(input("Enter a number: "))
   if number % 2 == 0:
       print(f"{number} is even.")
   else:
       print(f"{number} is odd.")
   ```  

3. **Practice (10 minutes):**  
   - Students write code to determine if a student passed (score ≥ 60) or failed (score < 60). 
 
   - Teacher circulates to provide feedback.  

---

### **Session 2: Advanced If-Else Logic**  
**Time:** 45 minutes  

**Learning Outcomes:**  
1. Use if-else statements with multiple conditions.  
2. Apply logic to real-world scenarios (e.g., comparing values).  

**Activities:**  
1. **Concept Review (10 minutes):**  
   - Discuss how to combine conditions (e.g., `if a > b and a < c`).  
   - Example: `if (age >= 18) and (score >= 80): print("Eligible for voting")`.  

2. **Code Example (15 minutes):**  
   - Write a program to determine if a person is eligible to vote (age ≥ 18 and score ≥ 80).  
   ```python
   age = int(input("Enter age: "))
   score = int(input("Enter score: "))
   if age >= 18 and score >= 80:
       print("Eligible for voting.")
   else:
       print("Not eligible.")
   ```  

3. **Practice (10 minutes):**  
   - Students create a program to check if a fruit is a fruit (e.g., "apple" or "banana") or a 
vegetable (e.g., "carrot").  
   - Teacher provides examples for edge cases (e.g., "grape" is a fruit).  

---

### **Session 3: Application & Real-World Use Cases**  
**Time:** 45 minutes  

**Learning Outcomes:**  
1. Apply if-else statements to solve real-world problems.  
2. Debug and test code for logical errors.  

**Activities:**  
1. **Real-World Scenario (10 minutes):**  
   - Example: A simple "Grade Calculator" that assigns grades based on scores (A: 90–100, B: 
80–89, etc.).  
   - Code:  
     ```python
     score = int(input("Enter score: "))
     if 90 <= score <= 100:
         print("A")
     elif 80 <= score <= 89:
         print("B")
     elif 70 <= score <= 79:
         print("C")
     else:
         print("D")
     ```  

2. **Practice (15 minutes):**  
   - Students code a program to check if a user is in a specific age group (e.g., "adult" or 
"teen").  
   - Example:  
     ```python
     age = int(input("Enter age: "))
     if age >= 18:
         print("Adult")
     else:
         print("Teenager")
     ```  

3. **Debugging (10 minutes):**  
   - Students identify and fix logical errors in provided code (e.g., incorrect conditionals 
or missing `else` clauses).  

---

### **Teacher Notes**  
- Encourage students to test code with sample inputs.  
- Use visual aids (e.g., whiteboard) to demonstrate code step-by-step.  
- Provide feedback on code structure and readability.  

**Assessment:**  
- Code correctness and logical reasoning in practice exercises.  
- Participation and ability to apply knowledge to real-world scenarios.  

---  
**Printed Format Summary:**  
- Session 1: Basic syntax, number checks.  
- Session 2: Advanced logic, real-world scenarios.  
- Session 3: Application, debugging, and real-world problem-solving.  
