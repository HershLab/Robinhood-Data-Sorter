import robin_stocks as r
from xlsxwriter import Workbook


def login ():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        login = r.login(username,password)
    except AttributeError:
        print("Incorrect login, please try running the script again.")

def historical_stock():
    ticker = input("Enter ticker: ")
    file_name = input("Please enter the file name. Include .xlsx at the end of the file name: ")

    final_list = []
    final_list = r.get_stock_historicals(ticker, interval= '5minute',span= 'week', bounds= 'regular', info = None)

    ordered_list=["time","begins_at","open_price","close_price", "high_price", "low_price", "volume", "session", "interpolated", "symbol"]

    wb= Workbook(file_name)
    ws=wb.add_worksheet("Ticker")

    first_row=0
    for header in ordered_list:
        col=ordered_list.index(header) 
        ws.write(first_row,col,header) 

    row=1
    for player in final_list:
        for _key,_value in player.items():
            col= ordered_list.index(_key)
            ws.write(row,col,_value)
        row+=1 #enter the next row
    wb.close()
    println("Done!")


def historical_options():
    print("placeholder")

login()
answererd = True
while(answererd == True):
    answer = input("What would you like to do? 1. get stock historical, 2. get options historical, 3. exit (enter corresponding number): ")
    if(answer == '1'):
        historical_stock()
    elif (answer == '2'):
        historical_options()
    elif (answer == '3'):
        answererd = False
    else:
        continue





