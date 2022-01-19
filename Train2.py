#2)A train of length 200 meters crosses a man running at 10 km/hr in the same direction in 10 seconds.What is the speed of the train?
Length_of_train = int(input('The length of train in m/s: '))
Speed_of_man = int(input('Enter the speed of man: '))
Speed_of_train = Length_of_train/Speed_of_man * (18/5) #We will convert it into Km/hr
Speed = Speed_of_train + Speed_of_man
print(Speed)


