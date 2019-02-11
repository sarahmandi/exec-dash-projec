# monthly_sales.py

# TODO: import some modules and/or packages here
import csv
import os
import itertools
from operator import itemgetter
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

##Option C: display list of files to user
path = "/Users/sarahmandi1/Desktop/exec-dash-project/data"
dirs = os.listdir(path)

files = []

for file in dirs:
    if file == ".DS_Store":
        pass
    else:
        print(file)
        files.append(file)

#print(files)
    
#Prompt user to input their selection

#user_input = input("Please select a file: ")

#print(files)
while True:
    
    user_input = input("Please select a file: ")
    if user_input in files:
        break 
    else:
        print("Sorry, that didn't work. Double check the file name!")
        continue



##following is from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/csv_solution_further.py
CSV_FILENAME = user_input
csv_filepath = os.path.join("data", CSV_FILENAME)
rows = []

with open(csv_filepath, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for od in reader:
        rows.append(dict(od)) # ideally we would transform all the prices from strings to floats here

sales_prices = [float(row["sales price"]) for row in rows] # list comprehension for mapping purposes!
total_sales = sum(sales_prices)

#breakpoint()

product_sales = []

sorted_rows = sorted(rows, key=itemgetter("product"))
rows_by_product = itertools.groupby(sorted_rows, key=itemgetter("product")) #> <itertools.groupby object at 0x10339dc50>

for product, product_rows in rows_by_product:
    monthly_sales = sum([float(row["sales price"]) for row in product_rows]) # list comprehension for mapping purposes!
    product_sales.append({"name": product, "monthly_sales": monthly_sales})

sorted_product_sales = sorted(product_sales, key=itemgetter("monthly_sales"), reverse=True)
top_sellers = sorted_product_sales[0:7] 
#print(top_sellers)

month = "MARCH" # TODO: get from file name or date values
year = 2018 # TODO: get from file name or date values

#
# INFO OUTPUTS
#

def to_usd(my_price):
  return f"${my_price:,.2f}"

print("-------------------------")
print(f"SALES REPORT!")
print("-------------------------")
print(f"MONTH: {month} {year}")
print(f"TOTAL SALES: {to_usd(total_sales)}")

print("-------------------------")
print("TOP SELLING PRODUCTS:")

top_seller_names = []
top_seller_sales = []

counter = 0
for top_seller in top_sellers:
    counter = counter + 1
    product_name = top_seller["name"]
    sales_usd = to_usd(top_seller["monthly_sales"])
    sales = top_seller["monthly_sales"]
    print(f"  {counter}. {product_name} ({sales_usd})")
    top_seller_names.append(product_name)
    top_seller_sales.append(sales)

#print(top_seller_names)
#print(top_seller_sales)
####

print("-----------------------")
print("VISUALIZING THE DATA...")


objects = top_seller_names
y_pos = np.arange(len(objects))
performance = top_seller_sales
 
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Sales (USD)')
plt.title('Top-Selling Products (' + month + " " + str(year) +")")
 
plt.show()