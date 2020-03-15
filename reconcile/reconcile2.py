
from dfCreator import createDfs
from repos import *
from outputs import *

'''
    The purpose of this is to reconcile accounting softwares' accounts of transactions with bank accounts records.
    For each transaction, the transaction can show in the softwares' or bank's current, previous, or next month. 
    Reconciliation is the provess of making those accounts' match, usually confirmed by checking the monthly ending 
    balances. If a transaction is missing this program provides hints where to find it (next or previous month).

'''

# compare two DataFrames for reconciliation
def compareDfs(firstDf: pd.DataFrame, secondDf: pd.DataFrame,
               firstDfDescription: str, secondDfDescription: str) -> None:
    count= 0
    for current in range(1,13):
        firstDfMonths = MonthsOriginalDf(current , firstDf, firstDfDescription)

        secondDfMonths = MonthsOriginalDf(current, secondDf, secondDfDescription)


        for firstDfIndex, firstDfRow in firstDfMonths.currentMonthDf.iterrows():
            firstDfCurrentRowAmount = firstDfRow['amount']
            firstDfCurrentRowDate = firstDfRow['date']
            firstDfCurrentRowDescription = firstDfRow['description']

            firstFound = Found(firstDfMonths, firstDfCurrentRowAmount)
            secondFound = Found(secondDfMonths, firstDfCurrentRowAmount)
            firstFound.findAmount()
            secondFound.findAmount()

            if (secondFound.numAmountCurrentMonth != firstFound.numAmountCurrentMonth):
                outputDiscrepency(firstDfCurrentRowAmount, firstDfCurrentRowDate, firstDfCurrentRowDescription,
                                  firstFound, secondFound)

                count +=1

    print("TOTAL COUNT %s" % count)

bankDf, wavesDf = createDfs()

# run both
compareDfs(bankDf, wavesDf,"BANK", "WAVES")
#compareDfs(wavesDf, bankDf, "WAVES", "BANK")




#find a specific amount
def findRow(df):
    df['amount'] = df['amount'].astype(float)
    #df = df[(df['amount'] == -227.5) & (df['amount'] >= -1500)]
    df = df[(df['amount'] == -227.5)]

    outputDf("aaaa", df)

#findRow(bankDf)