import pandas as pd 
df = pd.read_csv('autos.csv')
print(df.head())
# code to load the csv and read it

#a. find average price of autos
print('mean of price column:',autos['price'].mean())
# mean of price column: 17295.14186548524 is the desired solution
# I worked it out on google colabs


#b.Print the list of different possible types of VehicleType found in dataset
uniqueVehicleType = autos['vehicleType'].unique()
print('unique values of vehicleType column:',uniqueVehicleType)
#Print the list of different possible types of VehicleType found in dataset

#c.Calculate and print lowest yearOfRegistration  and highest yearOfRegistration
min_yearOfRegistration = autos['yearOfRegistration'].min()
max_yearOfRegistration = autos['yearOfRegistration'].max()
print('min:',min_yearOfRegistration)
print('max:',max_yearOfRegistration)
# min: 1000
# max: 9999

#d.Find and print standard deviation of column kilometer
kilometer = autos['kilometer'].std()
print('standars deviation',kilometer)
#gives the standard deviation

#e. I could not get the graph 

#f.Find out which VehicleType  is sold minimum and maximum
vehicleType = autos['vehicleType'].min()
vehicleType = autos['vehicleType'].max()
print('min sold',vehicleType)
print('max sold',vehicleType)

#g. cound not plot the graph

#I will certainly try to figure out the falut and plot graph for question (e) and (G)
