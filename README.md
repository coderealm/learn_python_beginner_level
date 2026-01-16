# The Programmer's Path

Learn Python

Build · Break · Master

#Beginner Level – Volume I


Start your journey into real-world programming. This beginner-focused Volume I doesn’t just teach syntax. It teaches you how to think like a developer. Write code, break it, fix it, and understand why it works.


# Preview Chapter


Get an exclusive first look inside **The Programmer’s Path: Learn Python**.

This preview chapter introduces you to the book’s clear, hands-on teaching style, designed to help beginners not just learn Python syntax, but think like real developers. You’ll see how concepts are explained step by step, reinforced with practical examples, and connected to real-world programming habits.

If you’ve ever felt overwhelmed by programming books that move too fast or explain too little, this chapter will show you a better way to learn, by building, breaking, and truly understanding your code.



# **Chapter 4: Variables**


**What Is a Variable?**


A **variable** is a named location in memory that stores a value. A variable is a **container for data**

Programs use variables to **remember information** while they are running.

**Real-World Analogy**

Think of a variable as a **labeled box**:

*   The **label** is the variable name
    
*   The **content** is the value stored inside
    

You can:

*  Put data into the box
    
*  Read the data
    
*  Replace the data
    

**Creating a Variable**

In Python, a variable is created using an **assignment statement operator**.

The general syntax for creating a variable is 

_variable_name = value_

**Example:**

```

# file name: example_72.py             

age = 20

```

*   age - variable name
   
*   =  - assignment operator
    
*    20 - value being stored
    


The assignment operator (=) means **“assign this value to the variable”**, not “equals” as in mathematics.

When the program runs:

*    Python stores the value 20 in memory (RAM)
    
*    The variable name age becomes a **reference** to that value
    

**Variables as References**

In Python, _**everything**_ **is an object**. This is a core idea of the language and explains why Python feels so consistent and flexible.

An **object** has:

*   **Identity** - where it lives in memory
    
*   **Type** - what kind of object it is
    
*  **Value** - the data it holds
    

In Python, variables do **not** store values directly. Instead, variable names act as **references to objects in memory**.

*  Assignment binds a **name** to an **object**
    
*  A variable can be reassigned at any time
    
*   Reassigning does **not** change the original value
    

**Variable Creation in Python vs Other Languages**

In languages like **C++, C#, or Java**, variables must be declared before use.

Python is different:

*  Python does **not** use separate variable declarations
    
*  Variables are created **only through assignment**
    
*  A value must be assigned when the variable is created
    
*  You cannot create a variable without giving it a value
    
*  A variable exists as soon as a value is assigned to a name
    

**What Happens When a Variable Is Reassigned?**

When a variable name is reassigned:

*   The original value is **not modified**
    
*   If no other variable refers to the old value, Python removes it from memory
    
*   If another variable still refers to it, the value remains
    

**Why This Behavior Is Important**

This reference-based behavior:

*  Prevents accidental data corruption
    
*  Allows Python to manage memory automatically
    
*  Makes programs easier to write, read, and understand
    

**Using a Variable**

Once a variable has been assigned a value, it can be used anywhere in your program.

**Example:**

```

# file name: example_73.py

age = 20

print(age)

```

**Output:**

```
20

```

When this code runs:

* Python assigns 20 to age
    
* When print(age) runs, Python looks up the value in memory
    
* The value is displayed in the VS Code terminal (Console)
    

**Updating a Variable**

Variables can be reassigned to different values.

When a variable is assigned a new value, it **stops referring to the old value** and begins referring to the **new value**.

**Example:**

```

# file name: example_74.py

age = 20

age = 25

print(age)

```

**Output:**

```

25

```

In this example:

*   The variable age first refers to the value 20
    
*   After reassignment, age refers to the value 25
    
*   A variable can refer to **only one value at a time**
    
*   The most recently assigned value is the one that is accessible
    

The earlier value (20) is no longer associated with the variable age. If no other variable refers to that value, Python may **automatically remove it from memory**.

When you assign a new value to a variable, the variable **simply points to the new value**. The old value is no longer used by that variable.

**Variable Scope**

In Python, **variable scope** refers to the region of a program where a variable is **defined, accessible, and usable**. Understanding variable scope is critical for writing correct, readable, and maintainable Python programs. Misunderstanding scope often leads to common errors such as NameError, unexpected behavior, or bugs that are difficult to trace.

Python determines variable scope based on **where and how a variable is created**, not where it is used.

**Why Variable Scope Matters**

Variable scope is important because it:

*   Controls **accessibility** of variables
    
*   Prevents **name collisions**
    
*   Improves **code clarity and modularity**
    
*   Helps Python manage **memory efficiently**
    
*   Avoids unintended side effects in large programs
    

Without proper scoping rules, programs would become unpredictable and hard to debug.

**Python’s Scope Resolution: The LEGB Rule**

Python follows the **LEGB rule** to resolve variable names. When Python encounters a variable, it searches for it in the following order:

1.  **L – Local scope**
    
2.  **E – Enclosing scope**
    
3.  **G – Global scope**
    
4.  **B – Built-in scope**
    

If the variable is not found in any of these scopes, Python raises a NameError.

**Local Scope**

A **local variable** is a variable defined **inside a function**. It is accessible only within that function and exists only while the function is executing.

**Characteristics of Local Variables**

*   Created when a function is called
    
*   Destroyed when the function finishes execution
    
*   Cannot be accessed outside the function
    
*   Have the highest priority in scope resolution
    

**Example: Local Scope**

```

# file name: example_75.py

def greet():

    message = "Hello, Python!"

    print(message)

greet()

```

**Output:**

```

Hello, Python!

```

Here, message is a local variable. Attempting to access it outside the function will raise an error:

```

# file name: example_76.py

def greet():

    message = "Hello, Python!"

    print(message)

print(message)  # NameError

```

**Output:**

```
NameError

```

NameError occurs when a variable is not found in any scope.

**Global Scope**

A **global variable** is a variable defined **outside all functions**, usually at the top level of a script or module. It is accessible throughout the program.

**Characteristics of Global Variables**

*   Created when the program starts
    
*   Available inside and outside functions (read-only by default inside functions)
    
*   Exist until the program terminates
    
*   Can be shared across multiple functions
    

**Example: Global Scope**

```

# file name: example_77.py

language = "Python"

def show_language():

    print(language)

show_language()

print(language)

```

**Output:**

```
Python

Python

```

Both calls can access the variable language.

**Local vs Global Variables**

**Shadowing Global Variables**

If a variable with the same name exists in both local and global scopes, the **local variable takes precedence**.

```

# file name: example_78.py

number = 10

def print_number():

    number = 5

    print(number)

print_number()  # Output: 5

print(number)   # Output: 10

```
**Output:**

```
5

10

```

Here, the local number shadows the global number.

**The global Keyword**

By default, functions **cannot modify global variables**. To modify a global variable inside a function, you must use the global keyword.

**Example: Without global**

```

# file name: example_79.py

count = 0

def increment():

    count = count + 1 

    print(count)  # UnboundLocalError

Python treats count as a local variable, leading to an error.

```

**Output:**

```
UnboundLocalError

```

UnboundLocalError occurs when Python treats a variable as local but it is referenced before assignment

**Example: With global**

```

# file name: example_80.py

count = 0

def increment():

    global count

    count += 1

increment()

print(count)  # Output: 1

```

**Output:**

```
1

```

**Best Practices for global**

*   Use sparingly
    
*   Avoid in large projects
    
*   Prefer passing variables as function arguments
    
*   Excessive use reduces readability and maintainability
    

**Enclosing Scope: Nonlocal Variables**

An **enclosing scope** exists in **nested functions**. It refers to variables defined in an outer function but not global.

**Example: Enclosing Scope**

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

**The nonlocal Keyword**

The nonlocal keyword allows modification of variables in the **enclosing (non-global) scope**.

**Example: Without nonlocal**

```

# file name: example_82.py

def outer():

    x = 10

    def inner():

        x = 20  # Creates a new local variable

    inner()

    print(x)  # Output: 10

```

**Output:**

```
10

```

**Example: With nonlocal**

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

**Output:**

```
20

```

**Built-in Scope**

The **built-in scope** contains Python’s built-in names such as:

*   print
    
*   len
    
*   type
    
*   range
    

These are always available in every scope level unless explicitly overridden.

**Overriding Built-ins (Not Recommended)**

```

# file name: example_84.py

print = "Hello"

print(print)  # TypeError

```

**Output:**

```
TypeError

```

Overriding built-ins can break functionality and should be avoided.

**TypeError** is raised when an operation or function is applied to an object of an **inappropriate type**.

**TypeError** occurs when Python knows _which_ variable you are using, but the **type of the value is incompatible** with what the code expects.

**Scope and Mutable vs Immutable Objects**

**Immutable Objects**

Immutable objects (e.g., int, float, str, tuple) cannot be modified directly.

**Example:**

```

# file name: example_85.py

x = 10

def change():

    x = 20

change()

print(x)  # Output: 10

```

**Output:**

```
10

```

**Mutable Objects**

Mutable objects (e.g., list, dict, set) can be modified without global.

**Example:**

```

# file name: example_86.py

numbers = [1, 2, 3]

def modify():

    numbers.append(4)

modify()

print(numbers)  # Output: [1, 2, 3, 4]

```

**Output:**


```

[1, 2, 3, 4]

```

**Best Practices for Managing Scope**

*   Keep variables **as local as possible**
   
*   Minimize use of global variables
   
*   Use descriptive variable names
    
*   Pass values explicitly to functions
   
*   Avoid overriding built-in names
   
*   Use nonlocal and global only when necessary
 
*   Python uses **LEGB** rule for scope resolution
  
*   **Local scope** is limited to functions
   
*   **Global scope** spans the entire module
    
*   **Enclosing scope** exists in nested functions
   
*   **Built-in scope** contains Python’s predefined names
    
*   global and nonlocal allow controlled scope modification
    

A strong understanding of variable scope is essential for writing reliable, efficient, and professional Python code.

--------------------------------------

**Chapter 2: Installing Visual Studio Code and Python**
=======================================================

This chapter walks you step by step through installing Visual Studio Code (VS Code) and Python on the three most common operating systems. It’s written for beginners, follow the steps in order, and you’ll be ready to start coding.The code editor, Python, and other tools set up on your computer to help you write code are collectively referred to as your development environment. You may skip this chapter if you already have a code editor (such as VS Code, Sublime Text, or Atom) and Python 3.x installed.What You’ll Install

    • Visual Studio Code (VS Code) – a free, lightweight code editor

    • Python – a popular, beginner-friendly programming language

    • Python extension for VS Code – adds syntax highlighting, running code, debugging, and more

Official sites:

    • VS Code: [https://code.visualstudio.com](https://code.visualstudio.com) 

    • Python: [https://www.python.org](https://www.python.org) 

**Installing Visual Studio Code**
---------------------------------

### **Windows**

Open your browser and go to:

[https://code.visualstudio.com](https://code.visualstudio.com) 

    1. Click Download for Windows.

    2. Run the downloaded file (VSCodeUserSetup-x64.exe).

    3. In the installer:

        ◦ Accept the license agreement

        ◦ Keep default options

        ◦ Check:

            ▪ “Add to PATH”

            ▪ “Open with Code” (optional but useful)

    4. Click Install, then Finish.  VS Code is now installed.

5\. Open VS Code from the Start Menu.

### **macOS**

Open your browser and go to:

[https://code.visualstudio.com](https://code.visualstudio.com) 

    1. Click Download for macOS.

    2. Open the downloaded .zip file.

    3. Drag Visual Studio Code.app into the Applications folder.

    4. Open Applications ➜ Visual Studio Code.

    5. If macOS warns about security, click Open.

VS Code is now installed.

### **Ubuntu Linux**

    1. Open your browser and go to:

[https://code.visualstudio.com](https://code.visualstudio.com) 

    2. Set your web browser to download to your download folder.

    3. Click Download for Linux ➜ .deb. 

    4. Open the Terminal and Install VS Code (Ubuntu)

        1. Open the Terminal

            1. Click the Show Applications button (usually at the bottom-left).

            2. Type Terminal.

            3. Click Terminal to open it.

            4. A window with text will appear. This is called the Terminal.

        2. Go to the Downloads Folder

            1. When you downloaded VS Code, it was saved in your Downloads folder.

            2. Click inside the Terminal window.

            3. Type this exactly cd Downloads as in the screenshot below and Press Enter. on your keyboard

**Install VS Code**

    1. Now type this command sudo apt install ./code\_\*.deb as seen in the screen below and Press Enter on your keyboard

    2. You may be asked for your password.

        ◦ When typing the password, nothing will appear on the screen (this is normal).

        ◦ Type your password and press Enter.

What this command does

    • sudo  - allows a user to temporarily run commands with administrator (root) privileges, such as installing software

    • apt install -  installs a program or software

    • code\_\*.deb - the VS Code installer file you downloaded

If you see the question :

Do you want to continue? \[Y/n\]

    • Type Y and press Enter.

    • Once it finishes:

    • VS Code is installed

Open the Application from the Applications Menu

    1. Click Show Applications (the grid of dots, usually at the bottom-left of the screen).

    2. A list of programs will appear.

    3. Look for the application you just installed (for example, Visual Studio Code).

    4. Click its name or icon to open it.

**Installing Python**
---------------------

### **Windows**

Open your browser and go to:

[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) 

    • Download Python 3 (latest version).

    • Run the installer.

    • IMPORTANT: Check “Add Python to PATH”.

    • Click Install Now.

    • Verify installation:

Open Command Prompt and Check Python (Windows)

            1. Click the Start button (bottom-left of your screen).

            2. Type Command Prompt.

            3. Click Command Prompt when it appears.

    A black window will open. This is called the Command Prompt(CMD).

            1. Click inside the black window.

            2. Type this exactly the script below in the command prompt

            3. Press the Enter key on your keyboard.

You should see something like Python 3.x.x.

### **macOS**

Open your browser and go to:

[https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/) 

    • Download the macOS installer (.pkg).

    • Open the file and follow the installation steps.

    • Open Terminal and verify:

**Note**: macOS includes an older Python by default to use python3.

You should see something like Python 3.x.x.

### **Ubuntu Linux**

Python usually comes preinstalled. To make sure it’s up to date:

    1. Open Terminal.

    2. Type the command sudo apt update && sudo apt install -y python3 in the terminal as seen in the screenshot below

    3. Verify installation

Type the command python3 –version in the terminal as seen in the screenshot below.  (Note it is two hyphens before the version)

You should see something like Python 3.x.x

### **Understanding the Python Version Number**

If Python is installed correctly, you will see text like:   Python 3.x.x  from running or executing the command python –version,

The x.x part represents the exact version number of Python installed on your computer.

What each part means

    • 3 ➜ the major version

        ◦ Python 3 is the modern and recommended version.

    • x ➜  the minor version

        ◦ This changes when new features are added.

    • x ➜  the patch version

        ◦ This changes when bugs or security issues are fixed.

**Example:**

If you see:Python 3.12.3 as shown in the screenshot above

That means:

    • 3 ➜  Python 3 (correct and recommended)

    • 12 ➜  minor version

    • 3 ➜  small bug-fix update

Why this matters and why you don’t need to worry

    • Any Python 3.x.x version is perfectly fine for beginners.

    • Tutorials and examples work the same across Python 3 versions.

    • Seeing 3.x.x just means: Python is installed and working

 In short: the numbers may differ, but if it starts with Python 3, you’re good to go.

If you see an error message instead, Python may not be installed or was not added correctly, this can be fixed by reinstalling Python and making sure “Add Python to PATH” is checked during installation.

**Installing the Code Runner Extension in VS Code**
---------------------------------------------------

Open VS Code.

    • Click the Extensions icon (left sidebar) or press:

    • Windows/Linux: Ctrl + Shift + X

    • macOS: Cmd + Shift + X

    • Search for Code Runner.

    • Install the extension published by Microsoft.

    • Restart VS Code if prompted.

Selecting the Python Interpreter

    1. Open VS Code.

    2. Press:

        ◦ Windows/Linux: Ctrl + Shift + P

        ◦ macOS: Cmd + Shift + P

    3. Type Python: Select Interpreter.

    4. Choose the Python version you installed (Python 3.x).

**Hello World ! - Test Your Setup**
-----------------------------------

    1. Launch Visual Studio Code from your computer

        1. Create a folder for your project

        ◦ Click File ➜ Open Folder…

        ◦ Create/select a folder like:

            ▪ PythonScripts

        ◦ Click Select Folder / Open

        ◦ This makes VS Code treat it as a project workspace.

    2. Create the file hello\_world.py

        ◦ In the left sidebar (Explorer), click New File (paper icon) or right-click inside the folder ➜ New File

        ◦ Type the filename:

            ▪ hello\_world.py

        3. Write the code

        ◦ Click inside the editor and type:

        ◦ print("Hello, World!")

        ◦ Then save:

            ▪ File ➜ Save or press:

                • Windows/Linux: Ctrl + S

                • macOS: Cmd + S

         4. Select your Python interpreter

            ▪ Look at the bottom-right (or bottom bar) for Python Interpreter (it may show something like Python 3.x)

            ▪ Click it ➜ choose your installed Python (example: Python 3.12.x)

If you don’t see it:

            ▪ Press Ctrl + Shift + P (Cmd + Shift + P on Mac)

            ▪ Search: Python: Select Interpreter

            ▪ Pick the correct one

### **Run using the VS Code Terminal**

**Steps**

1.  Open your  hello\_world.py file in VS Code.
    
2.  Open the terminal:
    
    *   **Windows/Linux:** \`Ctrl + \`\`
        
    *   **macOS:** \`Cmd + \`\`
        
3.  Make sure you’re in the file’s directory.
    
4.  Type the command below in the terminal:
    

python [hello\_world.](http://hello-world.js)py

    Or on macOS

python3 [hello\_world.](http://hello-world.js)py

5 .  Press Enter

**Run with the VS Code Debugger**

**Steps**

1.  Open the hello\_world.py file.
    
2.  Click **Run Without Debugging** (top menu bar) or **Ctrl + F5.**
    
3.  Choose **Python Debugger**.
    

If you see "Hello, World!" printed on the vs code terminal, it means your first program worked.

This small success is an important first step in learning how to program in Python.

**What does** "**Hello, World!**"**; mean in programming?**

In programming, "Hello, World!" is a traditional first example used when learning a new programming language.

It is usually the simplest program possible, designed to do just one thing:

display a message on the screen or terminal.

When beginners see "Hello, World!" appear as output, it confirms three important things:

    1. The programming language is installed correctly

    2. The code was written correctly

    3. The program ran successfully

Because it is simple and familiar, "Hello, World!" helps new learners focus on how programs work, without being distracted by complex logic.

**Why do programmers use it?**

Programmers use "Hello, World!" because it:

    • Is easy to understand

    • Requires very little code

    • Provides immediate feedback

    • Builds confidence for beginners

Once this first program works, learners can move on to more advanced concepts knowing their setup is correct.

Before proceeding, please ensure that you have completed the following steps:

*   You have installed **Python** and **Visual Studio Code (VS Code)**, and configured the Python interpreter within VS Code.
    
*   Your hello\_world.py script runs successfully without any errors
    
*   You can launch VS Code, create a new folder, and create a Python file with the correct .py extension
    
*   You are able to run Python code using **any of the two methods**
    
*   All Python source code files are named using the .py file extension
    
*   You may henceforth copy and paste, or manually type, the source code into a file, ensuring proper indentation using four (4) spaces. Execute the file to observe the output.
    
*   Make it a consistent practice to write the code from this book examples directly into the file, run it, and review the results. Regular practice is essential for building proficiency and achieving mastery.
    

**Troubleshooting**
-------------------

When a programmer encounters an error, the most important thing to remember is that **you are not alone**. Programming has been around for many years, and **most errors have already been encountered and solved by other programmers**. Troubleshooting is a skill used by **both beginners and experienced programmers**.

**1\. Stack Overflow**

**Stack Overflow** is one of the most popular places where programmers ask and answer questions.

*   Search your error message exactly as it appears
    
*   Read answers written by experienced programmers
    
*   Try the suggested solutions step by step
    

Many Python errors already have **multiple solutions** on Stack Overflow.

**2\. Google Search**

Using **Google** is often the fastest way to understand an error.

*   Copy and paste the error message
    
*   Add words like _Python_ or _beginner_
    
*   Read blog posts, documentation, and tutorials
    

 Often, the first few results already explain the issue clearly.

**3\. ChatGPT**

**ChatGPT** can help explain errors in simple terms.

*   Paste your code and error message
    
*   Ask for a beginner-friendly explanation
    
*   Try the suggested fixes and test them yourself
    

ChatGPT is especially helpful when you don’t understand the error message.

**How to Use These Sources Effectively**

Troubleshooting usually involves:

1.  **Finding the error** using Stack Overflow, Google, or ChatGPT
    
2.  **Reading the explanations**
    
3.  **Trying out the solutions**
    
4.  **Testing your code again**
    

**Sometimes the first solution won’t work and that’s okay. Try another one.**

**Troubleshooting Is for Everyone**

Troubleshooting is not just for beginners. Even **experienced programmers troubleshoot every day**.

No matter your skill level:

*   Errors will happen
    
*   Debugging is normal
    
*   Learning how to fix issues makes you a better programmer
    

**When** "**Hello, World!**" **Doesn’t Work**

If your simple **Hello, World** program does not work, the problem may be:

*   Incorrect Python installation or setup
    
*   Typographical errors (typos)
    
*   Missing parentheses or quotation marks
    
*   Incorrect indentation
    
*   Case-sensitive mistakes (Print instead of print)
    
*   Running the file in the wrong environment
    

**Example:**

Print("Hello, World")

**Fix:**

print("Hello, world")

Python is **case-sensitive**, so small mistakes matter.

**Why Troubleshooting Is Important**

It is very important to:

*   **Troubleshoot and fix errors before moving forward**
    
*   Make sure your setup works correctly
    
*   Understand why something failed
    

Skipping errors can cause **bigger problems later** and make learning more confusing.

**Final Thought**

Troubleshooting is not a sign of failure. It is a sign that you are **actively learning and improving**.

Every programmer beginner or expert learns by:

*   Making mistakes
    
*   Researching solutions
    
*   Testing fixes
    
*   Growing through experience
    

**Embracing Unfamiliar Terms on Your Programming Journey**
----------------------------------------------------------

When learning a new programming language, it’s normal to encounter unfamiliar keywords or terms used in explanations that don’t immediately make sense. Often, programming concepts depend on other ideas that are introduced later, which can make early chapters feel confusing or overwhelming.

The key is to keep going. If a word or keyword doesn’t make sense at the moment, do a quick search to understand its basic meaning, then continue learning. As you progress, those same terms will be explained in more detail, and their purpose will become clearer through repeated use and examples.

For instance, words like _import_, _function_, or _variable_ may seem meaningless if you’ve never programmed before. However, by briefly looking them up and continuing forward, you’ll eventually encounter full explanations that tie everything together. This cycle, confusion, curiosity, clarification, is a natural part of learning any programming language. With time and experience, what once felt unfamiliar will become second nature.


------------------

Where to Buy the Book


1. [Amazon](https://example.com)
2. [Barnes & Noble](https://example.com)
3. [Apple Books](https://example.com)
4. [Google Play Books](https://example.com)
5. [Kobo](https://example.com)
6. [Publisher Website](https://example.com)
7. [IndieBound](https://example.com)
8. [Bookshop.org](https://example.com)
9. [Audible (Audiobook)](https://example.com)
10. [Local Retailer / Other](https://example.com)


![Book Cover](./assets/learn_python_cover.png)

---

About the Book

 This book explores **Python Programming** and is designed for **beginners**.
 It focuses on:

*   Setting up development environment
*   Python Syntax Fundamentals
*   Variables
*   Data Types
*   Working with Strings
*   Numbers & Maths
*   Conditional Statements & Loops
*   Functions
*   Data Structures
*   Mastering classes

This repository source code is intended to **complement the book**, not replace it.


About This Repository

This repository contains **source code, examples, and supporting materials** referenced throughout the book.

What you'll find here:

*  Chapter-based folders that mirror the book structure
*  Runnable examples and experiments
*  Supplementary notes, fixes, and updates
*  References and external resources

Each folder or file is labeled to match the corresponding chapter or section in the book.


Getting Started (for Code)

```bash
# Clone the repository
git clone https://github.com/coderealm/learn_python_beginner_level.git

# Navigate into the project
cd your-repo
```

Additional setup instructions may be found in chapter-specific folders.


How the Code Maps to the Book

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


 If code changes or improvements occur after publication, they will be documented here.

---


License

The **source code** in this repository is licensed under the **MIT License**

The **book content** is © 2026 **D.K. Julius**. All rights reserved.


Author

**D.K. Julius**


Support

If you find this book helpful:

*  Star this repository
*  Leave a review where you purchased the book
*  Share it with others who might benefit

Thank you for reading!
