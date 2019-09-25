import time
ans=0


print("\nWELCOME TO THE IEEE TECHNOPOLY QUESTIONNAIRE")
print("\n\nHere, you can win 5000 IEEE bucks by answering 10 very simple questions.\nEach question is worth Rs450 and each minute is worth Rs100.\nAs every minute passes you lose Rs100 from your total.\n\n")
print("The first question appears in 15 seconds..\n\n")
time.sleep(15)


start = time.time()


print("Which of the following data structures falls under the category of a 'dictionary'?")
print("\n1.Tree")
print("\n2.Hash")
print("\n3.Linked list")
print("\n4.Hash table")
print("\nPlease enter your answer in single digit")
x=input()
if x == "4":
	ans=ans+1

print("\n\nWhich of the following is a legal identifier in assembly language?")
print("\n1.10percent")
print("\n2.A1a2a3...a247a248")
print("\n3.Eflags")
print("\n4.july_2012")
print("\nPlease enter your answer in single digit")
x=input()
if x == "4":
	ans=ans+1

print("\n\nI run in and out of town all day and night but I never get tired. What am I? (singular noun please)")
x=input()
if x == "road" or x=="ROAD":
	ans=ans+1

print("Doing good, But time is ticking\n")
time.sleep(1)
print("Tick..\n")
time.sleep(1)
print("Tock..\n")
time.sleep(1)
print("Tick..\n")
time.sleep(1)

print("\n\nWhich of the following operators has the highest precedence?")
print("\n1.*")
print("\n2.&&")
print("\n3.!")
print("\n4.!=")
print("\nPlease enter your answer in single digit")
x=input()
if x == "3":
	ans=ans+1

print("\n\nBefore a Cascading Style Sheet is useful, you need to include one into your HTML page. What HTML tag can you use to apply CSS rules to a document?")
print("\n1.Bootstrap")
print("\n2.Animation")
print("\n3.Style")
print("\n4.Function")
print("\nPlease enter your answer in single digit")
x=input()
if x == "3":
	ans=ans+1

print("\n\nThe date() function returns a formatted date or time. date('Y') would return which of following?")
print("\n1.2019")
print("\n2.September")
print("\n3.27")
print("\n4.27 Septenber 2019")
print("\nPlease enter your answer in single digit")
x=input()
if x == "1":
	ans=ans+1

print("\n\nWhich is not a function of a Manufacturing Execution System?")
print("\n1.Know how to make a product.")
print("\n2.Plan when to make the product")
print("\n3.Register how and when the product was made")
print("\n4.Send an invoice for the product.")
print("\nPlease enter your answer in single digit")
x=input()
if x == "4":
	ans=ans+1

print("Doing good, But time is ticking\n")
time.sleep(1)
print("Tick..\n")
time.sleep(1)
print("Tock..\n")
time.sleep(1)
print("Tick..\n")
time.sleep(1)

print("\n\nThe more you have of it, the less you see. What is it? (Abstract noun Please)")
x=input()
if x == "darkness" or x == "DARKNESS":
	ans=ans+1

print("\n\nHow many letters are in alphabet?")
x=input()
if x == "11":
	ans=ans+1

print("\n\nWhat is the first change that selection sort would make to this sequence to put it into ascending order: 4 3 2 1")
print("\n1. 1 2 3 4")
print("\n2. 3 4 2 1")
print("\n3.1 3 2 4")
print("\n4. 1 4 3 2")
print("\nPlease enter your answer in single digit")
x=input()
if x == "1":
	ans=ans+1



end = time.time()
timetaken = end-start
print("\n\nYou have reached the end of the questionare in ",int(timetaken/60)," minutes")
time.sleep(5)
cash= 5000+(ans*450)
timecash= (10-(int(timetaken/30)))*50
cash = cash+timecash
print("You bagged",cash," IEEE bucks. Time to work put your ideas to the test! :) \n\n")
print("\n\nPlease call a volunteer/Coordinator to Note down your cash. IEEE wishes you an awesome Techopedia!")