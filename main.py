from strategy.RSIStrategy import *
import sys

app = QApplication(sys.argv)

# rsi_strategy = RSIStrategy()
# rsi_strategy.start()

kiwoom = Kiwoom()

result = kiwoom.get_code_list_by_price()

print("jinhwan : ", result)

app.exec_()

