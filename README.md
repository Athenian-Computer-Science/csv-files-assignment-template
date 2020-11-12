# Working with csv files

First, find a csv file of data you want to use. You can get data from [NOAA](https://www.ncdc.noaa.gov/data-access) or many other public agencies. You can even use an excel file from a science class - just save it as a .csv file. (Note: CSV stands for *comma-separated values*. Save the csv file in this repo.

Next, be sure to import the csv module. (It comes with python, so you don't need to download anything. Just start your program with `import csv`)

## Reading the headers
Data spreadsheets have header lines that say what each column means. (If you are using your own lab data, be sure you have headers!)
* Open the file
* Use the reader() method in the csv module to read the file and assign it to a variable: `contents = csv.reader(filename)`
* Use the next() function to return the next line of the file (in this case, the first line - which is the header). `next()` returns the line in a list. `header_row = next(contents)`
* Print the header row - partly to be sure everything is working and also to see what the columns are!

## Printing the headers and their positions
It's helpful - especially for larger data sets - to know the position (index) of each header. That makes it easier to reference a column of data without trying to count down or over in a list. Therefore, it's helpful to print out the headers with their positions. 
* Using a for loop, print the index and the column header:
```
for index, column_header in enumerate(header_row):
  print(index, column_header)
```
* The `enumerate()` function returns the index and the value of each item as you loop through a list.
* When this works, you can remove the previous print statement since this one is more useful.

# Extracting data
* Choose a column of data you want to read.
* Make an empty list to hold that data.
* Use a `for` loop to step through the file contents. 
  * Note: be sure you still have the file open!
* Pull the data from the appropriate index and assign it to a variable.
* Append that variable to your list.
```
wind_direction = []
for row in contents:
    w_dir = int(row[31])
    wind_direction.append(w_dir)

print(wind_direction)
```
Now you have a list of data that you can manipulate in any way you wish! Find the average, high and low, or whatever else makes sense. Be sure to add comments to your code so I understand what you're doing.

When you commit, but sure to commit and push your data file(s) too!




