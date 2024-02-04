import csv
def output_log(data, filename='log.csv'):
    with open(filename, "w+") as my_csv:
        for row in data:
            my_csv.write(f"{row[0]},{row[1]}\n")




