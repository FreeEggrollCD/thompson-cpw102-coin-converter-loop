# Coin Converter Loop

---

## Overview

In this assignment, you will modify an existing Python program so that it uses a loop to repeat a task.

One common use of loops in real-world programming is allowing a user to repeat an operation multiple times. In this assignment, you will focus on making an existing program repeatable.

---

## Learning Goals

By completing this assignment, you will:

- Practice using loops in Python  
- Improve your ability to modify existing code  
- Reinforce user input, calculations, and output formatting  

---

## Getting Started

This repository includes:

- `coin_converter.py` → Starter code -- **this is the code you will modify** 
- `example_code/` → A similar completed example to help guide you  

---

## Your Task

The program already contains code that converts coins (quarters, dimes, nickels, pennies) into total cents. 

Your task is to modify the program so that it repeats the conversion as many times as the user wants.  

---

## Program Requirements


### Add a Loop

Modify the program so that:

- The program runs the coin conversion  
- Then asks the user if they want to convert more coins  
- If the user enters `y` or `Y`, the program repeats  
- If the user enters anything else (like `n`), the program stops  


---

### Current Behavior

Your program should continue to do the following until the user wants to quit:

- Prompt the user for:
  - Number of quarters  
  - Number of dimes  
  - Number of nickels  
  - Number of pennies  
- Calculate the total value in cents  
- Display the result clearly  

---

### Example Program Behavior

Your program should behave like this:

```
We will convert coins to cents.  
How many quarters? 2  
How many dimes? 3  
How many nickels? 4  
How many pennies? 5  
2 quarters 3 dimes 4 nickels 5 pennies is 105 cents  

Do you want to convert more coins? (Enter y for yes): y  

We will convert coins to cents.  
How many quarters? 5  
How many dimes? 6  
How many nickels? 7  
How many pennies? 2  
5 quarters 6 dimes 7 nickels 2 pennies is 222 cents  

Do you want to convert more coins? (Enter y for yes): n  
```

---

## Tips

- Use a while loop to repeat the program  
- Keep your code readable:
  - Use clear variable names  
  - Add blank lines where appropriate  
- Test your program multiple times  

---

## Extra Credit (10 points)

At the end of your program, add a second feature:

Create a loop that:

1. Repeatedly asks the user to enter a number  
2. Stops when the user enters a negative number  
3. Displays the sum of all non-negative numbers entered  

### Example:

```
Now we will add up some integers  
Input numbers, one at a time, entering a negative integer to stop the process.  

Input an integer: 1  
Input an integer: 2  
Input an integer: 3  
Input an integer: 5  
Input an integer: -9  
The total is 11  
```


---

## Submission

Follow the instructions in GITHUB_SETUP.md

