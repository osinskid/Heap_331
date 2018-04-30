# Driver program for students to try the default test cases
from SOL.ProjectXX_Solution import Heap, getStats, heapSort
import random

TEST_CASE = "\nTest Case {}:"


def test_case_1():
    print(TEST_CASE.format(1))
    test1 = Heap()
    for i in range(30, -4, -3):
        test1.insert(i)
    print(test1)
    assert(test1.array == [-3, 3, 0, 12, 6, 15, 18, 30, 21, 24, 9, 27])
    print("Test 1 Passesd")

def test_case_2():
    print(TEST_CASE.format(2))
    test2 = Heap()
    for i in range(-50, 5, 6):
        test2.insert(i)
    print(test2)
    assert(test2.array == [-50, -44, -38, -32, -26, -20, -14, -8, -2, 4])
    for i in range(7):
        test2.remove_min()
    print(test2)
    assert(test2.array == [-8, 4, -2])
    test2.remove(4)
    test2.remove(-50)
    print(test2)
    assert(test2.array == [-8, -2])
    print("Test 2 Passed")


def test_case_3():
    print(TEST_CASE.format(3))
    info = getStats([7,43,45,62,48,2,25,5,64,68])
    assert(info[0] == 2)
    assert (info[1] == 68)
    assert(info[2] == (369/10))
    assert(info[3] == 45)
    assert(info[4] != 0)
    print("Test 3 Passed.")

def test_case_4():
    print(TEST_CASE.format(4))
    info = getStats(["eijnw","nmlsn","fstyl","eseic","jpgyz","nnwql","qtjzc","jabfw","tothe","sdftu","puhoq","oaomn","zhbdl","qtjzc","ldwqm","wzwic","kyivp","bnzbh","uwmzf"])
    assert(info[0] == "bnzbh")
    assert (info[1] == "zhbdl")
    assert(info[2] == 'm')
    assert(info[3] == "nnwql")
    assert(info[4] == "qtjzc")
    print("Test 4 Passed.")

def test_case_5():
    print(TEST_CASE.format(5))
    random.seed(2018)
    test6 = random.sample(range(0, 10000), 5000)
    sorted_list = heapSort(test6)
    test6.sort()
    correct_list = test6
    assert (sorted_list == correct_list)
    print("Test 5 Passed.")

def test_case_6():
    print(TEST_CASE.format(6))


def main():
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    # test_case_6()

main()
