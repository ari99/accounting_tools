import pandas as pd

# When you add a receipt into waves and also import the transactions from your checking account
# your will have duplicate transactions that need to be merged. This script will help
# you find the transactions to merge. I've found findMergers2.py to be more useful than this script.


df = pd.read_csv("accounting.csv", sep=",")
df2 = pd.read_csv("accounting.csv", sep=",")
duplicateIndexes = []


def getRowVals(row):
    return row['Transaction Date'], row["Amount (One column)"], row["Account Name"]


# amounts are the same at different locations
def sameAmountsDifIndexes(amount, amount2, index, index2):
    if amount2 == amount and index2 != index and amount > 0 and \
            index2 not in duplicateIndexes and \
            index + 1 != index2 and \
            index2 + 1 != index:
        return True
    else:
        return False

# For every row, look at every row for a duplicate.
# n^2 algo; will not optimize
# https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

for index, row in df.iterrows():
    date, amount, accountName =getRowVals(row)
    numDups = 0

    if accountName == "BUSINESS CHECKING" or accountName=="Uncategorized Expense":
        for index2, row2 in df2.iterrows():
            date2, amount2, accountName2 = getRowVals(row2)

            if sameAmountsDifIndexes(amount, amount2, index, index2):
                '''
                if numDups ==0:
                    duplicateIndexes.append(index)

                duplicateIndexes.append(index2)
                numDups +=1'''

                print(" found duplicate amounts %s and %s with dates %s and %s with indexes %s and %s" %
                      (amount, amount2, date, date2, index, index2))

            elif index % 100 == 0: # output progress periodicly
                #print (" index %s " % index)
                #print(" %s %s" % (amount, amount2))
                pass