from repos import Found
import pandas as pd

def displayRows(df: pd.DataFrame):
    for index, row in df.iterrows():
        date = row['Transaction Date']
        amount = row["Amount (One column)"]
        accountGroup = row["Account Group"]
        accountName = row["Account Name"]

        month = row['month']
        print("date %s amounth %s accountGroup %s accountName %s month %s "
              % (date, amount, accountGroup, accountName, month))


def debugFirstRow(df: pd.DataFrame):
    for name, values in df.iteritems():
        print('{name}: "{value}"'.format(name=name, value=values[0]))

    print("=+==============================")
    for name, values in df.iteritems():
        print('{name}: "{value}"'.format(name=name, value=values[1]))

    print("=+==============================")

    for name, values in df.iteritems():
        print('{name}: "{value}"'.format(name=name, value=values[2]))


# output hint where to find the missing transaction
def outputHint(firstFound: Found, secondFound: Found):
    if ((secondFound.numAmountCurrentMonth != firstFound.numAmountCurrentMonth) and
            (secondFound.numAmountNextMonth > firstFound.numAmountNextMonth)):
        print("Look in next month in %s for the missing record " % secondFound.dfDescription)

    if ((secondFound.numAmountCurrentMonth  != firstFound.numAmountCurrentMonth) and
            (secondFound.numAmountPreviousMonth > firstFound.numAmountPreviousMonth)):
        print("Look in previous month in %s for the missing record " % secondFound.dfDescription)

    if ((secondFound.numAmountCurrentMonth != firstFound.numAmountCurrentMonth) and
            ((secondFound.numAmountPreviousMonth <= firstFound.numAmountPreviousMonth) and
             (secondFound.numAmountNextMonth <= firstFound.numAmountNextMonth))):
        print("Probably transaction not imported into %s " % secondFound.dfDescription)


def outputNumFounds(firstFound: Found, secondFound: Found):

    print("number of matches in same month %s in %s" % (
        secondFound.numAmountCurrentMonth, secondFound.dfDescription))
    print("number of matches in same month %s in %s" % (
        firstFound.numAmountCurrentMonth, firstFound.dfDescription))

    if (secondFound.numAmountPreviousMonth >= 1 or firstFound.numAmountPreviousMonth >= 1):
        print("num in previous month of %s  is %s" % (secondFound.dfDescription,
                                                      secondFound.numAmountPreviousMonth))
        print("num in previous month of %s  is %s" % (firstFound.dfDescription,
                                                      firstFound.numAmountPreviousMonth))

    if (secondFound.numAmountNextMonthDf >= 1 or firstFound.numAmountNextMonth >= 1):
        print("num found in next month of %s  is %s" % (secondFound.dfDescription,
                                                        secondFound.numAmountNextMonth))
        print("num in next month of %s  is %s" % (firstFound.dfDescription, firstFound.numAmountNextMonth))



def outputDf(dfDescription: str, df: pd.DataFrame) -> None:

    for index, row in df.iterrows():
        print("%s amount %s description %s date %s " %
              (dfDescription, row['amount'], row['description'],
               row['date']))


def outputFoundAmounts(found: Found ) -> None:
        print("--------Current month found %s" % found.dfDescription)
        outputDf(found.dfDescription, found.currentMonthFoundDf)
        print("--------Previous month found %s" % found.dfDescription)
        outputDf(found.dfDescription, found.previousMonthFoundDf)
        print("--------Next month found %s" % found.dfDescription)
        outputDf(found.dfDescription, found.nextMonthFoundDf)

# Output info about a found discrepency
def outputDiscrepency(firstDfCurrentRowAmount: float, firstDfCurrentRowDate, firstDfCurrentRowDescription: str,
                                  firstFound: Found, secondFound: Found) -> None:
    print("++++++++++++++++++++++++++++")
    print("+++++++++++DISCREPENCY FOUND+++++++++++++++++")
    print("++++++++++++++++++++++++++++")

    print("%s amount %s description %s date %s   amount not equal to amount in %s" %
          (firstFound.dfDescription,
           firstDfCurrentRowAmount, firstDfCurrentRowDescription,
           firstDfCurrentRowDate, secondFound.dfDescription))

    print("-----------")
    outputNumFounds(firstFound, secondFound)

    print("-----------")
    print("-------------Amount records found in %s" % firstFound.dfDescription)
    print("-----------")

    outputFoundAmounts(firstFound)
    print("-----------")
    print("-------------Amount records found in %s" % secondFound.dfDescription)
    print("-----------")

    outputFoundAmounts(secondFound)
    print("-----------")

    outputHint(firstFound, secondFound)

