#5)A train of length 100 meters is moving at a speed of 70 km/hr.In what time it will cross a man who is walking at 10 km/hr in the same direction?
Length_of_Train = int(input('Enter the length of train: '))
Speed_of_Train = int(input('Enter the speed of train: '))
Speed_of_Man = int(input("Enter the speed of man: "))
Relative_speed = Speed_of_Train - Speed_of_Man
Speed = Relative_speed * (5/18)
Distance = int(input('Length of train is: '))
Time = Distance / Speed
print('Time taken to cross the man is: ', Time)
