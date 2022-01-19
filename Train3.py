#3)A train moving at 50 km/hr crosses a bridge in 45 seconds.The length of train is 150 meters. Find the length of the bridge.
Speed_of_Train = int(input('Enter the speed of train: '))
Time = int(input('Enter the time :'))
Length_of_Train = int(input('Enter the length of train: '))
Speed = Speed_of_Train * (5/18)
Length_of_Bridge = Speed * Time - Length_of_Train
print('The Length of bridge is :' , Length_of_Bridge)



