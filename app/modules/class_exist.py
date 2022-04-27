def check_class(class_number):

    grade = int(class_number / 100)
    
    # 如果首位數不在1~3之間或後兩位不在1~24之間 回傳false
    if grade < 1 or grade > 3 or class_number - grade * 100 < 1 or class_number - grade * 100 > 24:
        return False
    return True