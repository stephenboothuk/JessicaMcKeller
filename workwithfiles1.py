#open a file handle
f = open("IHME_GBD_2010_MORTALITY_AGE_SPECIFIC_BY_COUNTRY_1970_2010.csv", "r")

mortality_data=[]
# iterate over the file handle
for line in f:
    # .strip() removes trailing whitespace
    line  = line.strip()
    # print(line)

    # append line read to mortality_data_list
    mortality_data.append(line)

# close the file handle
f.close()

print(mortality_data)

for datum in mortality_data:
    if datum[0] == "T":
        print(datum)
