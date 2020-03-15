import pandas as pd
import datetime

def getWavesMonth(row):
    dateStr = row['Transaction Date']
    dateObj = datetime.datetime.strptime(dateStr, '%Y-%m-%d')
    return dateObj.month


def getWavesYear(row):
    dateStr = row['Transaction Date']
    dateObj = datetime.datetime.strptime(dateStr, '%Y-%m-%d')
    return dateObj.year

def getBankMonth(row):
    dateStr  = row['date']
    dateObj = datetime.datetime.strptime(dateStr, '%m/%d/%Y')
    return dateObj.month

def getBankYear(row):
    dateStr = row['date']
    dateObj = datetime.datetime.strptime(dateStr, '%m/%d/%Y')
    return dateObj.year



def createWavesDf(wavesDf: pd.DataFrame) -> pd.DataFrame:
    #debugFirstRow(wavesDf)

    print(wavesDf['Account Group'].unique())

    #select only the columns we want
    newDf = wavesDf[['Transaction Date', 'Amount (One column)', 'Account Group',
                     'Account Name', 'Other Accounts for this Transaction', 'Transaction Description']]

    newDf = newDf[newDf['Account Name'] == 'BUSINESS CHECKING']
    print("len %s " %len(newDf))


    newDf['month'] = newDf.apply(lambda row: getWavesMonth(row), axis=1)
    newDf['year'] =  newDf.apply(lambda row: getWavesYear(row), axis=1)
    newDf = newDf[newDf['year'] == 2019]

    #displayRows(newDf)

    newDf = newDf[['Transaction Date','Amount (One column)', 'month', 'year' ,'Transaction Description' ]]
    newDf = newDf.rename(columns={'Transaction Date':'date', 'Amount (One column)':'amount',
                                  'Transaction Description':'description' })

    return newDf


def createBankDf(originalBankDf: pd.DataFrame) -> pd.DataFrame:
    bankDf = originalBankDf[['date', 'amount', 'description']]

    bankDf = bankDf.assign(month = bankDf.apply(lambda row: getBankMonth(row), axis=1))
    bankDf =  bankDf.assign( year = bankDf.apply(lambda row: getBankYear(row), axis=1))
    bankDf = bankDf[bankDf['year'] == 2019]

    return bankDf



def createDfs():
    originalWavesDf = pd.read_csv("../wavesExport/accounting.csv", sep=",")
    wavesDf = createWavesDf(originalWavesDf)

    orignalBankDf = pd.read_csv("../bankExport/Checking1.csv", sep=",")
    bankDf = createBankDf(orignalBankDf)
    return bankDf, wavesDf
