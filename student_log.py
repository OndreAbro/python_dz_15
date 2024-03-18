import argparse
from student import *


logging.basicConfig(filename='student.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    parser = argparse.ArgumentParser(description='Process student information.')
    parser.add_argument('name', help='Student name')
    parser.add_argument('csv_filename', help='CSV filename')
    args = parser.parse_args()

    try:

        # Для тестов логирования полезной информации создаются студенты
        student1 = Student(args.name, args.csv_filename)
        student2 = Student('Dick', 'subjects.csv')
        student1.add_score('math', 5)
        student2.add_test_result('history', 100)

        # Для тестов логирования ошибок поочередно раскоментировать по одной строке
        # student1.add_score('literature', 6)
        # student2.add_test_result('chemistry', 101)
        # student3 = Student('name', 'subjects.csv')

    except StudentNameError:
        pass
    except InvalidSubjectError:
        pass
    except InvalidScoreError:
        pass


if __name__ == '__main__':
    main()
