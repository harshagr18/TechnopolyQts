import time
ans=0


print("\nWELCOME TO THE IEEE TECHNOPOLY QUESTIONNAIRE")
print("\n\nHere, you can win 5000 IEEE bucks by answering 10 very simple questions.\nEach question is worth Rs450 and each minute is worth Rs100.\nAs every minute passes you lose Rs100 from your total.\n\n")
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

print("\n\nWho am I? Tear one off and scratch my head what was red is black instead.")
x=input()
if x == "matchstick" or x=="MATCHSTICK":
	ans=ans+1

print("Doing good, But time is ticking\n")
time.sleep(1)
print("Tick..\n")
time.sleep(1)
print("Tock..\n")
time.sleep(1)
print("Tick..\n")
time.sleep(1)

print("\n\nA double is classified as what data type?")
print("\n1.Integer")
print("\n2.Float")
print("\n3.Character")
print("\n4.Array")
print("\nPlease enter your answer in single digit")
x=input()
if x == "2":
	ans=ans+1

print("\n\nWhich of these is NOT protected by copyright? ( No hint, don't look here please )")
print("\n1.Dance Moves")
print("\n2.Machine Learning Code")
print("\n3.Ideas")
print("\n4.Musical pieces")
print("\nPlease enter your answer in single digit")
x=input()
if x == "3":
	ans=ans+1

print("\n\nGIMP is an acronym, or a word that is formed by the first letters from several words that make up a phrase. What does GIMP do?")
print("\n1.Image editing")
print("\n2.Coding IDE")
print("\n3.3D modelling")
print("\n4.Server Side editing")
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
time.sleep(4)
print("Tick..\n")
time.sleep(1)
print("Tock..\n")
time.sleep(1)
print("Tick..\n")
time.sleep(1)

print("\n\nWhat gets shorter when you add two letters to it?")
x=input()
if x == "SHORT" or x == "short":
	ans=ans+1

print("\n\nWhat gets wetter and wetter the more it dries?( Enter Singular noun ) ")
x=input()
if x == "towels" or x == "towel":
	ans=ans+1

print("\n\nWhat does the 'Q' in QBasic stand for?")
print("\n1.Quantam")
print("\n2.Quick")
print("\n3.Quiet")
print("\n4.Quinquagenarian")
print("\nPlease enter your answer in single digit")
x=input()
if x == "2":
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
