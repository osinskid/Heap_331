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
    print(TEST_CASE.format(4))
    info = getStats(["eijnw","nmlsn","fstyl","eseic","jpgyz","nnwql","qtjzc","jabfw","tothe","sdftu","puhoq","oaomn","zhbdl","qtjzc","ldwqm","wzwic","kyivp","bnzbh","uwmzf",])
    assert(info[0] == "bnzbh")
    assert (info[1] == "zhbdl")
    # assert(info[2] == (w/10))
    # assert(info[3] == 43)
    assert(info[4] != "qtjzc")
    print("Mean:    ", info[2])
    print("Median:    ", info[3])

def test_case_5():
    print(TEST_CASE.format(5))
    random.seed(2018)
    test6 = random.sample(range(0, 100), 24)
    print("Original: " + str(test6))
    sorted_list = heapSort(test6)
    print("Sorted: " + str(sorted_list))
    assert (sorted_list == [2, 3, 4, 5, 8, 15, 16, 30, 38, 51, 55, 58, 64, 67, 68, 70, 77, 80, 81, 85, 87, 90, 94, 99])

def test_case_6():
    print(TEST_CASE.format(6))

def main():
    # test_case_1()
    # test_case_2()
    # test_case_3()
    # test_case_4()
    test_case_5()
    # test_case_6()

main()
