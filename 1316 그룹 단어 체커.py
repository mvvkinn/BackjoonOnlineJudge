t_case = int(input())

cnt = 0
word_in = []

last_w = ''
shown_w = []

is_group = True

for _ in range(t_case):
        word_in.append(input())

for word in word_in:
        #다른 단어 검사전 변수 초기화
        is_group = True
        shown_w = []
        
        print("\nsearching in "+word)
        
        # 각 자리 알파뱃 비교
        for ch in word:
                
                # 직전 알파뱃과 현재 알파뱃 미일치
                if last_w != ch:

                        # 전에 있던 값이 존재할때(0이 아닐때) 그룹단어 아님
                        if shown_w.count(ch) != 0:
                                print("not group word")
                                print(ch+" is shown")
                                is_group = False
                                break
                                

                        # 미존재시 직전단어 변경, 전에 있던 값에 추가
                        else:
                                print(ch+" is not in list. adding")
                                last_w = ch
                                shown_w.append(ch)
                        print("still searching "+word)

        # 그룹 단어일때 카운트 증가
        if is_group == True:
                print(word+" is group word")
                cnt+=1
        

print(cnt)
                
                        
                        
                        


