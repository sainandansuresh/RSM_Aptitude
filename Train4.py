#4)A train is moving at 120 km/hr.The length of the train is 150 meters. How long it will take to cross a platform of length 100 meters?
Speed_of_Train = int(input('Enter the speed of train: '))
Length_of_Train = int(input('Enter the length of train: '))
Length_of_Platform = int(input('Enter the length of platform: '))
Speed = Speed_of_Train * (5/18)
Distance = Length_of_Train + Length_of_Platform
Time = Distance / Speed
print('Time taken to cross the platform is :', {Time})