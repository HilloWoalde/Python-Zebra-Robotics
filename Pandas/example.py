#pandas is a data management library, commmonly imported as pd
import pandas as pd

#series ~= list for pandas but you can change index (change from item1=0, item2=1... to smth else), can be made from dict with keys being indexes and values being the values
calories = [420, 380, 390]
duration = [50, 40, 45]
print(calories)
print(duration)

workouts = {"calories": calories, "duration": duration}
print(workouts)

#dataframe ~= google sheets, index is numbering, key (in dict) is Titles 
workoutSheet = pd.DataFrame(workouts, index = ["day1", "day2", "day3"])
print(workoutSheet)