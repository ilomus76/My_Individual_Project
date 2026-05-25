
# 파일명 ex14_module_custom.py

#module을 만드는 수업 
# 나만의 모듈 만들기 

#1 ] 별도의 파일(module_a.py)에 함수와 변수를 만들어 사용해보기 
# 그냥 단순히 이름이다..
# module_a.py 파일에 변수 함수 만드는 것이다.

#print(title) # 그냥사용하면 error 
#show() # error

# 다른 모듈(파이썬 파일)의 변수와 함수를 사용하려면.... import

import module_a
print(module_a.title) # import 로 나의 파이썬 파이썬 파일을 불러오면 됨. 
module_a.show() 

from module_a import title,show   # 함수이지만 이름만 가져오면 된다. 
print(title) # hello python module
show() #show module a


# 특정 모듈의 모든 변수와 함수를 쉽게 사용하고 싶다면...
from module_a import * # 모든 변수 함수를 불러옴.
print(title)
show()
print()

# 위의 3가지중 하나를 사용하면 된다.... 
# 모듈을 내 파일과 같은 디렉토리에 있으면 헤깔리니 디렉터리 하나를 만들어 관리하자..
# modules 라는 폴더를 하나 만들자.. 그리고 그 안에 aaa.py를 하난 만들자

import modules.aaa  # 폴더안에 파이썬 파일이 이름이 있으면 그이름. 으로 명명해야 함.
print(modules.aaa.title) 
modules.aaa.show()
print()


from modules import aaa
print(aaa.title)
aaa.show()
print()
#------------------------------------------------

#모듈을 import 한다는 것은 사실.....그 파이썬파일.py를 실행한다는 것임.

from modules import  bbb # modules라는 폴더에서 import하자..
# bbb만 import 함. 
# import만 했는데 bbb의 display()가 실행이 됨. 
# 하지만 output()함수는 실행이 안됨. 코드에 함수 호출이 안되니...

# import 시 bbb의 output 함수가 호출이 안됨.
# bbb모듈의 output()함수를 호출하고 싶다면...
bbb.output()
print()
# ---------------------------------------------------

# _(언더스코어)를 변수명에 사용하면 import*로 가져올때 제외됨... 
#  modules 폴더에 ccc.py를 만들어라...

from modules import ccc
print(ccc.title)
print(ccc._message)

from modules.ccc import * # ccc안의 모든것을 모듈명 없이 쓸수 있는 기능
print(title)    # 이것은 가능
#print(_message) # *로 import를 했기 때문에 _message를 가져오지 못함. 
#import * 일때만 제외되는 것이어서.. 직접 대상을 명시하여 import하면 사용가능.
#*로 import하면 너무많은 것을 가져오니 _로 된것을 배제하고 아래와 같이 직접 import하면 사용가능하게 함. 
from modules.ccc import _message
print(_message)  
# _언더스코어는 변수뿐 아니라 함수도 사용가능























