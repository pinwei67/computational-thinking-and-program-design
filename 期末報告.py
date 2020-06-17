print("哈囉。我是冰冰。我是一個點餐機器人。") 
print("我喜歡冰淇淋，也喜歡巧克力豆。")
# 取得顧客名字 
name = input("您叫什麼名字？： ") 
# 打招呼 
print("您好，", name, "！很高興為您服務！")

# 從顧客取得喜好 
like = input("我不太清楚您的喜好。請問要杯裝還是手拿？ ") 
print("好的，我覺得不錯！") 
# 請顧客輸入數字 
amount = int(input("請問您要幾球呢？："))
if amount >= 4:
     print("非常好的選擇!")
elif amount >=2:   
     print("謝謝捧場")
else:    
     print("好的")
print("一共是", amount,"球。")

#口味
flavor=input("請問您喜歡什麼口味？：")
print("好的，我記住了。")

# 配料
print("我們有巧克力豆、棉花糖或是都不加，") 
food = input("您要選擇加哪一樣呢？：") 
print("好，我瞭解了！") 

# 付款
print("稍後為您製作。")
print("你已點餐完成，請至窗口結帳") 

# 道別  
print("五分中後餐點就會製作完成囉！")
point = input("有集點嗎? ")

if point == "有":
    n = 0
left = 0
while n < 15:
    
    n = n + 1
    left = 15 - n
    print("這次為第", n, "次集點", "還有",left, "點可兌換冰淇淋一球")
      
    
amount=int(input('請輸入球數'))
總金額=(amount*30)
print('總金額為',總金額)
print("謝謝您的惠顧，", name, "歡迎再次光臨！")

