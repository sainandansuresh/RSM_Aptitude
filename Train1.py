#1)A train moving at speed of 90 km/hr crosses a pole in 7 seconds.Find the length of the train.
len_of_the_train = int(input('The speed of train in Km/hr: ' ))
Total_time = int(input('Enter the time in seconds: '))
Speed = len_of_the_train * (5/18)  #Speed is given in Km/hr so we will converted it into m/s.
Distance = len_of_the_train * Total_time
print(Distance)

