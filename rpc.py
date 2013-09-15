#coding:utf-8

# 9622 ▖
# 9623 ▗
## 9624 ▘
## 9625 ▙
## 9626 ▚
## 9627 ▛
## 9628 ▜
## 9629 ▝
## 9630 ▞
## 9631 ▟
## 9632 ■

## 9600 ▀
## 9601 ▁
## 9602 ▂
## 9603 ▃
## 9604 ▄
## 9605 ▅
## 9606 ▆
## 9607 ▇
## 9608 █
## 9609 ▉
## 9610 ▊
## 9611 ▋
## 9612 ▌
## 9613 ▍
## 9614 ▎
## 9615 ▏
## 9616 ▐
## 9617 ░
## 9618 ▒
## 9619 ▓


import random


def chstring(startchar=0,endchar=10000, n=826):
    print startchar, endchar, endchar-startchar+1 
    strchar=''
    for i in xrange(n):
        strchar += unichr(random.randrange(startchar,endchar+1))
    strchar += '\n'
    return strchar

print chstring(9482,9584)
print chstring(5121,5191)
print chstring(9622,9632)
print chstring(9601,9615)
print chstring(9617,9619)
print chstring(9398,9450) # Ⓐ 
print chstring(9776,9783) # ☴ 
print chstring(9833,9836) # 9833 ♩ 9834 ♪ 9835 ♫ 9836 ♬
print chstring(8866,8879) # 8866 ⊢ 8867 ⊣
print chstring(9585,9587) #9585 ╱ 9586 ╲ 9587 ╳
print chstring(9280,9284) #9280 ⑀ 9281 ⑁ 9282 ⑂ 9283 ⑃ 9284
print chstring(9116,9134) #⎛ 9116 ⎜ 9117 ⎝ 9118 ⎞ 9119 ⎟ 9120 ⎠ 9121 ⎡ 9122 ⎢ 9123 ⎣ 9124 ⎤ 9125 ⎥ 9126 ⎦ 9127 ⎧ 9128 ⎨ 9129 ⎩ 9130 ⎪ 9131 ⎫ 9132 ⎬ 9133 ⎭ 9134 ⎮
print chstring(10240,10495) #brail_ABC
print chstring(8704,8959) #math_ops
print chstring(59367,59379) #psevdogr
