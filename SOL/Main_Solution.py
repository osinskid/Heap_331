# Driver program for students to try the default test cases
from SOL.ProjectXX_Solution import Heap

TEST_CASE = "\nTest Case {}:"


def test_case_1():
    print(TEST_CASE.format(1))
    test1 = Heap()
    for i in range(30, -4, -3):
        test1.insert(i)
    print(test1)
    for i in range(7):
        test1.remove_min()
    print(test1)


def test_case_2():
    print(TEST_CASE.format(2))

def test_case_3():
    print(TEST_CASE.format(3))

def test_case_4():
    print(TEST_CASE.format(5))

def test_case_5():
    print(TEST_CASE.format(5))

def test_case_6():
    print(TEST_CASE.format(6))

def main():
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()

main()
