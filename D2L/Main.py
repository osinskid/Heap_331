# Driver program for students to try the default test cases
from D2L.ProjectXX import Heap, getStats, heapSort

TEST_CASE = "\nTest Case {}:"


def test_case_1():
    print(TEST_CASE.format(1))
    test1 = Heap()
    for i in range(30, -4, -3):
        test1.insert(i)
    print(test1)
    assert (test1.array == [-3, 3, 0, 12, 6, 15, 18, 30, 21, 24, 9, 27])
    print("Test 1 Passesd")


def test_case_2():
    print(TEST_CASE.format(2))
    test2 = Heap()
    for i in range(-50, 5, 6):
        test2.insert(i)
    print(test2)
    assert (test2.array == [-50, -44, -38, -32, -26, -20, -14, -8, -2, 4])
    for i in range(7):
        test2.remove_min()
    print(test2)
    assert (test2.array == [-8, 4, -2])
    test2.remove(4)
    test2.remove(-50)
    print(test2)
    assert (test2.array == [-8, -2])
    print("Test 2 Passed")


def test_case_3():
    print(TEST_CASE.format(3))
    info = getStats([7, 43, 45, 62, 48, 2, 25, 5, 64, 68])
    assert (info[0] == 2)
    assert (info[1] == 68)
    assert (info[2] == (369 / 10))
    assert (info[3] == 45)
    assert (info[4] != 0)
    print("Test 3 Passed.")


def main():
    test_case_1()
    test_case_2()
    test_case_3()


main()
