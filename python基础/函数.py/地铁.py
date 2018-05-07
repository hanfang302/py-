money = 0
distance = input('请输入距离\n')
day = 1
while day <= 2:
    count = 1
    while count <=2:
        if money <= 100: 
            if distance <=6:
                money+=3
            elif 6 < distance and distance <=12:
                money+=4
            elif 12 < distance and distance <=22:
                money+=5
            elif 22 < distance and distance <=32:
                money+=6
            elif distance > 32:
                if (distance - 32)%20 ==0:
                    money+=(6+(distance-32)/20)
                else:
                    money+=(6+(distance-32)/20+1)
        if 100<money and money <= 150:
            if distance <=6:
                money+=3*0.8
            elif 6 < distance and distance <=12:
                money+=4*0.8
            elif 12 < distance and distance <=22:
                money+=5*0.8
            elif 22 < distance and distance <=32:
                money+=6*0.8
            elif distance > 32:
                if (distance - 32)%20 ==0:
                    money+=(6+(distance-32)/20)*0.8
                else:
                    money+=(6+(distance-32)/20+1)*0.8
        if 150<money and money<=400:
            if distance <=6:
                money+=3*0.5
            elif 6 < distance and distance <=12:
                money+=4*0.5
            elif 12 < distance and distance <=22:
                money+=5*0.5
            elif 22 < distance and distance <=32:
                money+=6*0.5
            elif distance > 32:
                if (distance - 32)%20 ==0:
                    money+=(6+(distance-32)/20)*0.5
                else:
                    money+=(6+(distance-32)/20+1)*0.5
        if money > 400:
            if distance                                            
