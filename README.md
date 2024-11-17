# [Nelia Koontz]
## [Assignment # Lab 09]
## [Submission date: 11/17/2024]
## Worked with/sources 
* asked chat gpt to explain this code that I had written because I kept getting only cheese back: 
* def setToppings(self, *toppings):
* """set toppings method"""
* index = 0
* while len(toppings) < index:
*     for topping in toppings:
*         self.toppings.append(topping)
*         index +=1
* print(self.toppings)
* to which it replied the while loop was unneccessary, and I took it out, which fixed the problem
* except it appended as another list ["cheese" ["carrots", "fudge", "crayons"]]. I tried different * things and eventually, I moved the for loop to before calling the function, which worked OK.
* I also googled does every var in a class need to be called self, and I think I understand that 
* a little more. used the book, especially the chapter on classes. It took me a while to get the * * pizza to increment.


## Project Quirks/ Things that don't work
* This program does not check for a whole number because I didn't see in the rules that it had to
* It will calculate any number, but will change it to 10 if less than 10 and it will throw an error
* if it is not a number.
