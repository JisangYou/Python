import sys
import mymodule


'''
모듈화
'''

'''
print("The command line arguments are:")
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH IS', sys.path, '\n')

if __name__ == '__main__':
    print("this program is being run by itself")
else:
    print('i am being imported from another module')



mymodule.say_hi()
print('Version',mymodule.__version__)
'''
a=5
print(dir())

'''
패키지>모듈>함수+전역변수>변수
__init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. python3.3 버전부터는 상관 없음.
'''