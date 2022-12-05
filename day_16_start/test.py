from prettytable import from_csv 
fp = open("day_16/books.csv", "r") 
pt = from_csv(fp) 
pt.align = 'l'
print(pt)
fp.close() 