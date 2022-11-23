answers = ""
class money_banana:
    def chuyen_tien(tag,tag_given, money):
        
        money_in_txt = open(f'D:\\coding stuff\\discord bot\\assets\\information\\{tag}.txt')
        money_left= money_in_txt.read()
        if int(money) > int(money_left):
            answers = "Bạn không có đủ banana để chuyển !"
        elif int(money) <= 0:
            answers ="Giá trị không đúng !"
        elif not money.isdigit():
            answers ="Giá trị không đúng !"
        elif int(money) > 100000000:
            if str(tag) != '9935':
                answers = "Mỗi lần chuyển chỉ được tiêu ít hơn 100000 :banana: !"
            else:
                if str(tag_given) == '9935':
                    money_give_in_txt = open(f'D:\\coding stuff\\discord bot\\assets\\information\\{tag_given}.txt','r')
                    money_in_txt_2 = open(f'D:\\coding stuff\\discord bot\\assets\\information\\{tag}.txt','w')
                    money_given = int(money_give_in_txt.read())
                    money_give_in_txt_2 = open(f'D:\\coding stuff\\discord bot\\assets\\information\\{tag_given}.txt','w')
                    money_left_after = int(money_left) - int(money)
                    money_given = money_given + int(money)
                    answers = f"Bạn đã chuyển thành công số banana là **{int(money):,d}** :banana: !"
                    money_in_txt_2.write(str(money_left_after))
                    money_give_in_txt_2.write(str(money_given))
        else:
            money_give_in_txt = open(f'D:\\coding stuff\\discord bot\\assets\\information\\{tag_given}.txt','r')
            money_in_txt_2 = open(f'D:\\coding stuff\\discord bot\\assets\\information\\{tag}.txt','w')
            money_given = int(money_give_in_txt.read())
            money_give_in_txt_2 = open(f'D:\\coding stuff\\discord bot\\assets\\information\\{tag_given}.txt','w')
            money_left_after = int(money_left) - int(money)
            money_given = money_given + int(money)
            answers = f"Bạn đã chuyển thành công số banana là **{int(money):,d}** :banana: !"
            money_in_txt_2.write(str(money_left_after))
            money_give_in_txt_2.write(str(money_given))
        return answers
    def kiem_tra(tag):
        money_in_txt = open(f'D:\\coding stuff\\discord bot\\assets\\information\\{tag}.txt')
        money= money_in_txt.read()
        answers = f"Số banana của bạn hiện tại là **{int(money):,d}** :banana: !"
        return answers