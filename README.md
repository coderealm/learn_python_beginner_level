# The Programmer's Path

## Learn Python

## Build · Break · Master

### Beginner Level – Volume I


## Start your journey into real-world programming. This beginner-focused Volume I doesn’t just teach syntax. It teaches you how to think like a developer. Write code, break it, fix it, and understand why it works.


# Preview Chapter


## Get an exclusive first look inside **The Programmer’s Path: Learn Python**.

## This preview chapter introduces you to the book’s clear, hands-on teaching style, designed to help beginners not just learn Python syntax, but think like real developers. You’ll see how concepts are explained step by step, reinforced with practical examples, and connected to real-world programming habits.

## If you’ve ever felt overwhelmed by programming books that move too fast or explain too little, this chapter will show you a better way to learn, by building, breaking, and truly understanding your code.



# **Chapter 4: Variables**


## **What Is a Variable?**


## A **variable** is a named location in memory that stores a value. A variable is a **container for data**

## Programs use variables to **remember information** while they are running.

## **Real-World Analogy**

## Think of a variable as a **labeled box**:

*  ##  The **label** is the variable name
    
*  ##  The **content** is the value stored inside
    

## You can:

* ##  Put data into the box
    
* ##  Read the data
    
* ##  Replace the data
    

## **Creating a Variable**

## In Python, a variable is created using an **assignment statement operator**.

## The general syntax for creating a variable is 

## _variable_name = value_

## **Example:**

```

# file name: example_72.py             

age = 20

```

*  ##  age - variable name
   
*  ##  =  - assignment operator
    
*   ##  20 - value being stored
    


## The assignment operator (=) means **“assign this value to the variable”**, not “equals” as in mathematics.

## When the program runs:

*   ##  Python stores the value 20 in memory (RAM)
    
*   ##  The variable name age becomes a **reference** to that value
    

## **Variables as References**

## In Python, _**everything**_ **is an object**. This is a core idea of the language and explains why Python feels so consistent and flexible.

## An **object** has:

*  ##  **Identity** - where it lives in memory
    
*  ##  **Type** - what kind of object it is
    
*  ## **Value** - the data it holds
    

## In Python, variables do **not** store values directly. Instead, variable names act as **references to objects in memory**.

*  ## Assignment binds a **name** to an **object**
    
*  ## A variable can be reassigned at any time
    
*  ##  Reassigning does **not** change the original value
    

## **Variable Creation in Python vs Other Languages**

## In languages like **C++, C#, or Java**, variables must be declared before use.

## Python is different:

* ##  Python does **not** use separate variable declarations
    
* ##  Variables are created **only through assignment**
    
* ##  A value must be assigned when the variable is created
    
* ##  You cannot create a variable without giving it a value
    
* ##  A variable exists as soon as a value is assigned to a name
    

## **What Happens When a Variable Is Reassigned?**

## When a variable name is reassigned:

* ##   The original value is **not modified**
    
* ##   If no other variable refers to the old value, Python removes it from memory
    
* ##   If another variable still refers to it, the value remains
    

## **Why This Behavior Is Important**

## This reference-based behavior:

* ##  Prevents accidental data corruption
    
* ##  Allows Python to manage memory automatically
    
* ##  Makes programs easier to write, read, and understand
    

## **Using a Variable**

## Once a variable has been assigned a value, it can be used anywhere in your program.

## **Example:**

```

# file name: example_73.py

age = 20

print(age)

```

## **Output:**

```
20

```

## When this code runs:

* ## Python assigns 20 to age
    
* ## When print(age) runs, Python looks up the value in memory
    
* ## The value is displayed in the VS Code terminal (Console)
    

## **Updating a Variable**

## Variables can be reassigned to different values.

## When a variable is assigned a new value, it **stops referring to the old value** and begins referring to the **new value**.

## **Example:**

```

# file name: example_74.py

age = 20

age = 25

print(age)

```

## **Output:**

```

25

```

## In this example:

*  ##  The variable age first refers to the value 20
    
*  ##  After reassignment, age refers to the value 25
    
*  ##  A variable can refer to **only one value at a time**
    
*  ##  The most recently assigned value is the one that is accessible
    

## The earlier value (20) is no longer associated with the variable age. If no other variable refers to that value, Python may **automatically remove it from memory**.

## When you assign a new value to a variable, the variable **simply points to the new value**. The old value is no longer used by that variable.

## **Variable Scope**

## In Python, **variable scope** refers to the region of a program where a variable is **defined, accessible, and usable**. Understanding variable scope is critical for writing correct, readable, and maintainable Python programs. Misunderstanding scope often leads to common errors such as NameError, unexpected behavior, or bugs that are difficult to trace.

## Python determines variable scope based on **where and how a variable is created**, not where it is used.

## **Why Variable Scope Matters**

## Variable scope is important because it:

*  ##  Controls **accessibility** of variables
    
*  ##  Prevents **name collisions**
    
*  ##  Improves **code clarity and modularity**
    
*  ##  Helps Python manage **memory efficiently**
    
*  ##  Avoids unintended side effects in large programs
    

## Without proper scoping rules, programs would become unpredictable and hard to debug.

## **Python’s Scope Resolution: The LEGB Rule**

## Python follows the **LEGB rule** to resolve variable names. When Python encounters a variable, it searches for it in the following order:

## 1.  **L – Local scope**
    
## 2.  **E – Enclosing scope**
    
## 3.  **G – Global scope**
    
## 4.  **B – Built-in scope**
    

## If the variable is not found in any of these scopes, Python raises a NameError.

## **Local Scope**

## A **local variable** is a variable defined **inside a function**. It is accessible only within that function and exists only while the function is executing.

## **Characteristics of Local Variables**

*   ## Created when a function is called
    
*   ## Destroyed when the function finishes execution
    
*   ## Cannot be accessed outside the function
    
*   ## Have the highest priority in scope resolution
    

## **Example: Local Scope**

```

# file name: example_75.py

def greet():

    message = "Hello, Python!"

    print(message)

greet()

```

## **Output:**

```

Hello, Python!

```

## Here, message is a local variable. Attempting to access it outside the function will raise an error:

```

# file name: example_76.py

def greet():

    message = "Hello, Python!"

    print(message)

print(message)  # NameError

```

## **Output:**

```
NameError

```

## NameError occurs when a variable is not found in any scope.

## **Global Scope**

## A **global variable** is a variable defined **outside all functions**, usually at the top level of a script or module. It is accessible throughout the program.

**Characteristics of Global Variables**

*   ## Created when the program starts
    
*   ## Available inside and outside functions (read-only by default inside functions)
    
*  ##  Exist until the program terminates
    
*  ##  Can be shared across multiple functions
    

## **Example: Global Scope**

```

# file name: example_77.py

language = "Python"

def show_language():

    print(language)

show_language()

print(language)

```

## **Output:**

```
Python

Python

```

## Both calls can access the variable language.

## **Local vs Global Variables**

## **Shadowing Global Variables**

## If a variable with the same name exists in both local and global scopes, the **local variable takes precedence**.

```

# file name: example_78.py

number = 10

def print_number():

    number = 5

    print(number)

print_number()  # Output: 5

print(number)   # Output: 10

```
## **Output:**

```
5

10

```

## Here, the local number shadows the global number.

## **The global Keyword**

## By default, functions **cannot modify global variables**. To modify a global variable inside a function, you must use the global keyword.

## **Example: Without global**

```

# file name: example_79.py

count = 0

def increment():

    count = count + 1 

    print(count)  # UnboundLocalError

Python treats count as a local variable, leading to an error.

```

## **Output:**

```
UnboundLocalError

```

## UnboundLocalError occurs when Python treats a variable as local but it is referenced before assignment

## **Example: With global**

```

# file name: example_80.py

count = 0

def increment():

    global count

    count += 1

increment()

print(count)  # Output: 1

```

## **Output:**

```
1

```

## **Best Practices for global**

*   ## Use sparingly
    
*   ## Avoid in large projects
    
*   ## Prefer passing variables as function arguments
    
*   ## Excessive use reduces readability and maintainability
    

## **Enclosing Scope: Nonlocal Variables**

## An **enclosing scope** exists in **nested functions**. It refers to variables defined in an outer function but not global.

## **Example: Enclosing Scope**

```

# file name: example_81.py

def outer():

    msg = "Outer message"

    def inner():

        print(msg)

    inner() # Outer message

outer()

Here, msg belongs to the enclosing scope of inner().

```

**Output:**

```

Outer message

```

## **The nonlocal Keyword**

## The nonlocal keyword allows modification of variables in the **enclosing (non-global) scope**.

## **Example: Without nonlocal**

```

# file name: example_82.py

def outer():

    x = 10

    def inner():

        x = 20  # Creates a new local variable

    inner()

    print(x)  # Output: 10

```

## **Output:**

```
10

```

## **Example: With nonlocal**

```

# file name: example_83.py

def outer():

    x = 10

    def inner():

        nonlocal x

        x = 20

    inner()

    print(x)  # Output: 20

```

## **Output:**

```
20

```

## **Built-in Scope**

## The **built-in scope** contains Python’s built-in names such as:

*   ## print
    
*   ## len
    
*   ## type
    
*   ## range
    

## These are always available in every scope level unless explicitly overridden.

## **Overriding Built-ins (Not Recommended)**

```

# file name: example_84.py

print = "Hello"

print(print)  # TypeError

```

## **Output:**

```
TypeError

```

## Overriding built-ins can break functionality and should be avoided.

## **TypeError** is raised when an operation or function is applied to an object of an **inappropriate type**.

## **TypeError** occurs when Python knows _which_ variable you are using, but the **type of the value is incompatible** with what the code expects.

## **Scope and Mutable vs Immutable Objects**

## **Immutable Objects**

## Immutable objects (e.g., int, float, str, tuple) cannot be modified directly.

## **Example:**

```

# file name: example_85.py

x = 10

def change():

    x = 20

change()

print(x)  # Output: 10

```

## **Output:**

```
10

```

## **Mutable Objects**

## Mutable objects (e.g., list, dict, set) can be modified without global.

## **Example:**

```

# file name: example_86.py

numbers = [1, 2, 3]

def modify():

    numbers.append(4)

modify()

print(numbers)  # Output: [1, 2, 3, 4]

```

## **Output:**


```

[1, 2, 3, 4]

```

**Best Practices for Managing Scope**

*  ##  Keep variables **as local as possible**
   
*  ##  Minimize use of global variables
   
*  ##  Use descriptive variable names
    
*  ##  Pass values explicitly to functions
   
*  ##  Avoid overriding built-in names
   
*  ##  Use nonlocal and global only when necessary
 
*  ##  Python uses **LEGB** rule for scope resolution
  
*  ##  **Local scope** is limited to functions
   
*  ##  **Global scope** spans the entire module
    
*  ##  **Enclosing scope** exists in nested functions
   
*  ##  **Built-in scope** contains Python’s predefined names
    
*  ##  global and nonlocal allow controlled scope modification
    

## A strong understanding of variable scope is essential for writing reliable, efficient, and professional Python code.



## Where to Buy the Book


## 1. [Amazon](https://example.com)
## 2. [Barnes & Noble](https://example.com)
## 3. [Apple Books](https://example.com)
## 4. [Google Play Books](https://example.com)
## 5. [Kobo](https://example.com)
## 6. [Publisher Website](https://example.com)
## 7. [IndieBound](https://example.com)
## 8. [Bookshop.org](https://example.com)
## 9. [Audible (Audiobook)](https://example.com)
## 10. [Local Retailer / Other](https://example.com)


![Book Cover](./assets/learn_python_cover.png)

---

## About the Book

##  This book explores **Python Programming** and is designed for **beginners**.
##  It focuses on:

*  ##  Setting up development environment
*  ##  Python Syntax Fundamentals
*  ##  Variables
*  ##  Data Types
*  ##  Working with Strings
*  ##  Numbers & Maths
*  ##  Conditional Statements & Loops
*  ##  Functions
*  ##  Data Structures
*  ##  Mastering classes

## This repository source code is intended to **complement the book**, not replace it.


## About This Repository

## This repository contains **source code, examples, and supporting materials** referenced throughout the book.

## What you'll find here:

* ##  Chapter-based folders that mirror the book structure
* ##  Runnable examples and experiments
* ##  Supplementary notes, fixes, and updates
* ##  References and external resources

## Each folder or file is labeled to match the corresponding chapter or section in the book.


## Getting Started (for Code)

```bash
# Clone the repository
git clone https://github.com/coderealm/learn_python_beginner_level.git

# Navigate into the project
cd your-repo
```

## Additional setup instructions may be found in chapter-specific folders.


## How the Code Maps to the Book

| Book Chapter | Folder |
|--------------|---------------|
| Chapter 1    | `1_introduction` |
| Chapter 2    | `2_installing_visual_studio_code_and_python` |
| Chapter 3    | `3_programming_syntax_fundamentals` |
| Chapter 4    | `4_variables` |
| Chapter 5    | `5_primitive_data_types` |
| Chapter 6    | `6_working_with_strings` |
| Chapter 7    | `7_numbers_and_maths` |
| Chapter 8    | `8_conditional_statements_and_loops` |
| Chapter 9    | `9_functions` |
| Chapter 10   | `10_data_structures` |
| Chapter 11   | `11_mastering_python_classes` |
| Chapter 12   | `12_getting_started_with_ the_python_repl`|


##  If code changes or improvements occur after publication, they will be documented here.

---


## License

## The **source code** in this repository is licensed under the **MIT License**

## The **book content** is © 2026 **D.K. Julius**. All rights reserved.


## Author

## **D.K. Julius**


## Support

## If you find this book helpful:

* ##  Star this repository
* ##  Leave a review where you purchased the book
* ##  Share it with others who might benefit

## Thank you for reading!
