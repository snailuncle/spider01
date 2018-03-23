

for i in range(6):
    print('i='+str(i))
    try:
        # store_list=[1,2,3,4,5,6,7,8]
        store_list=[]
        if len(store_list)==0:
            print("zhixing  break")
            break
        for j in range(6):
            print('j='+str(j))
    except Exception as e:
        print(e)
        break       
