# Driver program for students to try the default test cases
from ProjectXX_Solution import HashTable

TEST_CASE = "\nTest Case {}:"


def test_case_1():
    print(TEST_CASE.format(1))
    test1 = HashTable()
    test1.insert("key1", "val1")
    test1.insert("abc", 123)
    test1.insert("g99K3fEPQt", 99.99)
    print("Size:", test1.get_size())
    print("Capacity:",  test1.get_capacity())
    print("Load factor:",  test1.load_factor())
    print("Test is_empty():", test1.is_empty())


def test_case_2():
    print(TEST_CASE.format(2))
    test2 = HashTable()
    test2.insert("key2", "val2")
    test2.insert("Python", 3.6)
    test2.insert("VzPK5VX6OM", "5pw7y8PKKy")
    test2.insert("RSPGL73xrS", "lIOOjGhYxz")
    test2.insert("HV9mIbGYYC", "4bIGNRs5x0")
    test2.insert("EmZmY6xnDa", "DY7eBFJMqi")
    test2.insert("CEXQ5hpHYZ", "qp7DvNxJsu")
    test2.insert("rtPdbWRo2G", "aGJDHxue2A")
    test2.insert("TQAG4FNDD1", "BkZ6J9yPkH")
    test2.remove("RSPGL73xrS")
    test2.remove("CEXQ5hpHYZ")
    test2.remove("TQAG4FNDD1")
    test2.remove("key2")
    test2.remove("aGJDHxue2A")
    test2.remove("key2")
    test2.remove("HV9mIbGYYC")
    print("Size:", test2.get_size())
    print("Capacity:", test2.get_capacity())


def test_case_3():
    print(TEST_CASE.format(3))
    test3 = HashTable()
    test3.insert("key3", "val3")
    test3.insert("Onsay", 331)
    test3.insert("mEcT6XS9he", "jhIoQWB1Ql")
    test3.insert("kQWdx82AbJ", "eCbXQlBomT")
    assert(test3.string_verify("Onsay", 331) == True)
    assert(test3.string_verify("Onsay", 232) == False)
    assert(test3.string_verify("eCbXQlBomT", "kQWdx82AbJ") == False)
    assert(test3.string_verify("mEcT6XS9he", "jhIoQWB1Ql") == True)
    print("All assert statements have passed.")


def test_case_4():
    print(TEST_CASE.format(4))
    table1 = HashTable(3)
    table1.insert("clementine", 1)
    table1.insert("quince", 2)
    table1.insert("durian", 3)
    table1.insert("banana", 4)
    table1.insert("mango", 5)
    print("Load Factor: " + str(table1.load_factor()) + " Size: " + str(table1.get_size()) )

    table1.insert("orange", 6)
    print("Load Factor: " + str(table1.load_factor()) + " Size: " + str(table1.get_size()) )

    table1.insert("pineapple", 7)
    print("Load Factor: " + str(table1.load_factor()) + " Size: " + str(table1.get_size()) )

    table1.remove("banana")
    table1.remove("quince")
    print("Load Factor: " + str(table1.load_factor()) + " Size: " + str(table1.get_size()) )

    table1.insert("apple", 8)
    print("Load Factor: " + str(table1.load_factor()) + " Size: " + str(table1.get_size()) )


def print_variables(hash_table):
    print("Capacity: " + str(hash_table.get_capacity()) + " Size: " +
          str(hash_table.get_size()) + " Load Factor: " + str(hash_table.load_factor()))

def test_case_5():
    print(TEST_CASE.format(5))
    htable = HashTable(1)
    print_variables(htable)

    htable.insert("dog", 1)
    print_variables(htable)

    htable.insert("cat", 2)
    print_variables(htable)

    htable.insert("lion", 3)
    htable.insert("bear", 4)
    htable.insert("bird", 5)
    htable.insert("horse", "6")
    htable.insert("pig", 7)
    htable.insert("wolf", 8)
    htable.insert("tiger", 9)
    htable.insert("deer", 10)
    print_variables(htable)

    htable.remove("bird")
    htable.remove("pig")
    print_variables(htable)

    htable.remove("horse")
    htable.remove("tiger")
    print_variables(htable)

    assert(htable.string_verify("horse", "6") == False)
    assert(htable.string_verify("pig", 7) == False)

def test_case_6():
    print(TEST_CASE.format(6))
    key = ""
    test6 = HashTable()
    file = open("input6.txt", 'r')
    for line in file:
        if key != "":
            key = line
        else:
            test6.insert(key, line)
            key = ""

    print("Size:", test6.get_size())
    print("Capacity:",  test6.get_capacity())
    print("Load factor:",  test6.load_factor())
    print("Test is_empty():", test6.is_empty())


def main():
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()


main()
