import time

ans=0
print("\nWELCOME TO THE IEEE TECHNOPOLY QUESTIONNAIRE")
print("\n\nHere, you can win 5000 IEEE bucks by answering 10 very simple questions.\nEach question is worth Rs250 and each minute is worth Rs250.\nAs every minute passes you lose Rs250 from your total.\n\n")
print("The first question appears in 15 seconds..\n\n")
time.sleep(15)
start = time.time()


print("To begin with, why was BASIC called BASIC? ( It was one of the first programming languages )")
print("\n1.It had an easy syntax")
print("\n2.It had an easy programmable logic")
print("\n3.It was written in assembly lanugage")
print("\n4.It was an acronym")
print("\nPlease enter your answer in single digit")
x=input()
if x == "4":
	ans=ans+1

print("\n\nwhat does CSS actually stand for? _______ Style Sheets ( It is used in web designing )")
print("\n1.Cascading")
print("\n2.Constitutionalism")
print("\n3.Crypto")
print("\n4.Counterproductive")
print("\nPlease enter your answer in single digit")
x=input()
if x == "1":
	ans=ans+1

print("\n\nWhat can travel around the world while staying in a corner? ( Please type the answer in all caps, singular nown )")
x=input()
if x == "STAMP":
	ans=ans+1

print("Doing good but time is ticking... Tick.. Tock.. Tick..\n\n")
time.sleep(4)

print("\n\nOfficially, what does Perl stand for? ( It is a lesser used programming language )")
print("\n1.Practical Extraction and Reporting Language")
print("\n2.Nothing LOL")
print("\nPlease enter your answer in single digit")
x=input()
if x == "2":
	ans=ans+1

print("\n\nWhat is the shortcut to make text bold? ( No hint, don't look here please )")
print("\n1.Ctrl+F")
print("\n2.Ctrl+A")
print("\n3.Ctrl+B")
print("\n4.Ctrl+G")
print("\nPlease enter your answer in single digit")
x=input()
if x == "3":
	ans=ans+1

print("\n\nWhat icon is represented by the letter 'A' with a line under it? ( No hint, don't look here please )")
print("\n1.Font colour")
print("\n2.Font Size")
print("\n3.Font style")
print("\n4.Font attributes")
print("\nPlease enter your answer in single digit")
x=input()
if x == "1":
	ans=ans+1

print("\n\nWhich icon is represented by only two pieces of paper with writing? ( No hint, don't look here please )")
print("\n1.Cut")
print("\n2.Copy")
print("\n3.Paste")
print("\nPlease enter your answer in single digit")
x=input()
if x == "2":
	ans=ans+1

print("Doing good but time is still ticking... Tick.. Tock.. Tick..\n\n")
time.sleep(4)

print("\n\nWhat word is spelled wrong in all the dictionaries? ( Please type the answer in all caps, singular word )")
x=input()
if x == "WRONG":
	ans=ans+1

print("\n\nA sphere has three, a circle has two, and a point has zero. What is it? ( Please type the answer in all caps, plural noun )")
x=input()
if x == "DIMENSIONS":
	ans=ans+1

print("\n\nWhat icon is represented by a magnifying glass over a blank piece of paper? ( No hint, don't look here please )")
print("\n1.Print")
print("\n2.Find and Replace")
print("\n3.Print Preview")
print("\nPlease enter your answer in single digit")
x=input()
if x == "3":
	ans=ans+1



end = time.time()
timetaken = end-start
print("\n\nYou have reached the end of the questionare in ",int(timetaken/60)," minutes")
time.sleep(5)
cash= 5000+(ans*250)
timecash= (10-(int(timetaken/60)))*250
cash = cash+timecash
print("You bagged",cash," IEEE bucks. Time to work put your ideas to the test! :) \n\n")
print("\nPlease call a volunteer/Coordinator to Note down your cash. IEEE wishes you an awesome Techopedia!")