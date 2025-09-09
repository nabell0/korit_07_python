class Student():
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades={}

    def add_grade(self, subject, score):
        self.grades[subject] = score

    def get_average_grade(self):
        return sum(self.grades.values()) / len(self.grades)

    def show_info(self):
        print(f'학생 이름: {self.name}')
        print(f'평균 성적: {self.get_average_grade()}')

student1 = Student('김일',123)
student1.add_grade('subject1',90)
student1.add_grade('subject2',90)
student1.add_grade('subject3',90)
student1.show_info()

'''
사용자로부터 여러 개의 숫자를 입력 받아 리스트에 저장한 후, 해당 리스트에 포함된 숫자들 중 양수, 음수, 0의 개수를 각각 세어 출력하는 프로그램을 작성하시오.

지시사항:

1. 몇 개의 숫자를 입력할지 사용자로부터 입력 받으시오.
2. 입력받은 숫자들을 저장할 빈 리스트(numbers)를 생성하시오.

3. 양수, 음수, 0의 개수를 저장할 변수 3개를 0으로 초기화하시오.

4. for 반복문을 사용하여 입력 받은 횟수만큼 숫자들을 입력 받아 numbers 리스트에 추가하고, 동시에 각 숫자를 판별하여 해당 변수의 값을 1씩 증가 시키시오.

최종적으로 각 변수에 저장된 개수를 출력하시오.

실행 예:

몇 개의 숫자를 입력하시겠습니까? >>> 5

1번째 숫자를 입력하시오 >>> 10

2번째 숫자를 입력하시오 >>> -5

3번째 숫자를 입력하시오 >>> 0

4번째 숫자를 입력하시오 >>> 20

5번째 숫자를 입력하시오 >>> -15

양수: 2개

음수: 2개

0: 1개
'''