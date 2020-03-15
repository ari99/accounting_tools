import pandas as pd
df = pd.read_csv("accounting.csv", sep=",")

# When you add a receipt into waves and also import the transactions from your checking account
# your will have duplicate transactions that need to be merged. This script will help
# you find the transactions to merge.


def printDf(amountDf):
    print("____________________________________________________")
    print("____________New Amount______________")
    print("____________________________________________________")

    for index, row in amountDf.iterrows():
        date = row['Transaction Date']
        amount = row["Amount (One column)"]
        accountName = row["Account Name"]
        print("index : %s  date : %s amount : %s " % (index, date, amount))





foundAmounts = []
foundAmountDfs = []

# loop through all amounts and create a df containing all occurances of that amount
# append the newly created df to foundAmountDfs
for index, row in df.iterrows():

    date = row['Transaction Date']
    amount = row["Amount (One column)"]
    accountName = row["Account Name"]  #i think if you limit it to the account group 'expense' in will be easier

    if amount > 0 and amount not in foundAmounts:
        foundAmounts.append(amount)
        sameAmountDf = df.loc[df['Amount (One column)'] == amount]
        foundAmountDfs.append(sameAmountDf)

# loop through the df's for each amount found and see if there
# are more than one occurances
for amountDf in foundAmountDfs:
    numRows = amountDf.shape[0]
    if numRows > 1:
        printDf(amountDf)





