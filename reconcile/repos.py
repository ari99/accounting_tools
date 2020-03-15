import pandas as pd

# Hols current, previous, next months dataframes
class MonthsOriginalDf:
    def __init__(self, currentMonth: int,
                 df: pd.DataFrame,
                 dfDescription: str):
        self.currentMonthDf = df[df['month'] == currentMonth]
        self.previousMonthDf = df[df['month'] == (currentMonth - 1)]
        self.nextMonthDf = df[df['month'] == (currentMonth + 1)]
        self.dfDescription = dfDescription

# Holds dataframes and counts for an amount we are looking for
class Found:
    def __init__(self, monthsOriginalDf: MonthsOriginalDf, amount: float):
        self.amount = amount
        self.monthsOriginalDf = monthsOriginalDf
        self.dfDescription =  self.monthsOriginalDf.dfDescription
        self.previousMonthFoundDf = self.initializeFoundDf()
        self.nextMonthFoundDf = self.initializeFoundDf()
        self.currentMonthFoundDf = self.initializeFoundDf()
        self.numAmountPreviousMonth= 0
        self.numAmountNextMonth= 0
        self.numAmountCurrentMonth = 0

    def initializeFoundDf(self):
        foundDf = pd.DataFrame({'date': [], 'amount': [], 'month': [],
                                                   'description': [], 'year': []})
        return foundDf

    def calcMonthFoundDf(self, originalMonthDf: pd.DataFrame) -> pd.DataFrame:
        monthFoundDf = self.initializeFoundDf()
        if(len(originalMonthDf) > 0):
            monthFoundDf = originalMonthDf[originalMonthDf['amount'] == self.amount]
        return monthFoundDf

    def findAmount(self) -> None:
        self.currentMonthFoundDf = self.calcMonthFoundDf(self.monthsOriginalDf.currentMonthDf)
        self.numAmountCurrentMonth = len(self.currentMonthFoundDf)
        self.previousMonthFoundDf = self.calcMonthFoundDf(self.monthsOriginalDf.previousMonthDf)
        self.numAmountPreviousMonth = len(self.previousMonthFoundDf)
        self.nextMonthFoundDf = self.calcMonthFoundDf(self.monthsOriginalDf.nextMonthDf)
        self.numAmountNextMonth = len(self.nextMonthFoundDf)
