# Driver program for students to try the default test cases
from SOL.ProjectXX_Solution import Heap, getStats, heapSort
TEST_CASE = "\nTest Case {}:"


def test_case_1():
    print(TEST_CASE.format(1))
    test1 = Heap()
    for i in range(30, -4, -3):
        test1.insert(i)
    print(test1)

def test_case_2():
    print(TEST_CASE.format(2))
    test2 = Heap()
    for i in range(-50, 5, 6):
        test2.insert(i)
    print(test2)
    for i in range(7):
        test2.remove_min()
    print(test2)
    test2.remove(4)
    test2.remove(-50)
    print(test2)

def test_case_3():
    print(TEST_CASE.format(3))
    info = getStats([7,43,45,62,48,2,25,5,64,68])
    assert(info[0] == 2)
    assert (info[1] == 68)
    assert(info[2] == (369/10))
    assert(info[3] == 43)
    assert(info[4] != 0)
    print("Should have no output.")

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
