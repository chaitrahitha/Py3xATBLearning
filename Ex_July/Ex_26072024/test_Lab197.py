import csv
import pandas
import pandas as pd

# pip install pandas
class Test_CRUD(object):
    def test_update_1(self):
        # Read the file
        with open('Ex_July/Ex_26072024/userdata.csv') as csvfile:
            reader= csv.reader(csvfile)
            for row in reader:
                print(row[0],row[1])

    def test_update_2(self):
        df = pd.read_csv('Ex_July/Ex_26072024/userdata.csv')
        print(df)