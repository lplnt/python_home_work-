import view
import operations
import logger

def button_click():
    value_lst, kind_oper = view.get_value()
    logger.logwrite("Ввод: ", value_lst) 
    result = operations.calc(value_lst, kind_oper)
    logger.logwrite("Результат: ", result)
    view.output(result)