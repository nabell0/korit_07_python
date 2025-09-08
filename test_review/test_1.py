
for i in range(2):
    tel = input('전화번호를 입력하시오 >>>')
    if len(tel) != 13:
        print(f'유효하지않은 전화번호 형식 입니다.')
    elif len(tel) == 13:
        print(f' 전화번호의 중간 4자리는 {tel[4:8]}입니다. ')
