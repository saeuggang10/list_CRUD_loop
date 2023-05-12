#!/usr/bin/env python
# coding: utf-8

# In[1]:


name =[]
age=[]
area=[]

while 1:
    print('='*15)
    print('데이터 : ', name, age, area)
    print('='*15)
    print('1. 데이터 생성하기 \n2. 데이터 수정하기 \n3. 데이터 삭제하기 \n4. 데이터 검색하기 \n※ 검색 종료시 q를 입력해 주세요')
    print('='*15)
    ty=input('아래 중 하나를 선택해 주세요(번호 입력) : ')
    print('='*15)
    
    #1. 데이터 생성하기
    if ty=="1":
        print('1. 데이터 생성하기')
        print('='*15)
        nick = input('이름 : ')
        old = input('나이 : ')
        local = input('지역 : ')
        
        name.append(nick)
        age.append(old)
        area.append(local)
        
    #2. 데이터 수정하기
    elif ty=='2':
        print('2. 데이터 수정하기')
        print('='*15)
        print('1. 이름 \n2. 나이 \n3. 지역')
        fix = input('수정할 사항을 선택해 주세요 : ')
        for val in [name, age, area]:
            if fix in val:
                temp2 = input('수정 후 : ')
                i = val.index(fix)
                val[i]=temp2
            else:
                print('변경사항이 없습니다')
                
    #3. 데이터 삭제하기
    elif ty =='3':
        print('3. 데이터 삭제하기')
        print('='*15)
        dele = input('삭제할 데이터의 이름을 입력해 주세요 : ')
        if dele in name:
            j = name.index(dele)
            del name[j]
            del age[j]
            del area[j]
        else:
            print('데이터가 존재하지 않습니다.')
        
    #4. 데이터 검색하기
    elif ty=='4':
        print('4. 데이터 검색하기')
        print('='*15)
        inp = input('찾고자하는 데이터의 이름을 입력해 주세요 : ')
        if inp in name:
            k = name.index(inp)
            print('이름 : {0:^5} | 나이 : {1:^5} | 지역 : {2:^5}'
              .format(name[k], age[k], area[k]))
        else:
            print('데이터가 존재하지 않습니다.')
    
    #프로그램 종료
    elif ty=='q':
        print('종료합니다')
        break
        
    else:
        print('잘못 입력하셨습니다')
        
    print("\n")
    print("-"*15)
    print("\n")

