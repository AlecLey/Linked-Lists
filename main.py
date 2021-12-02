from UnorderedList_test import * 

def test_insert(data, pos, input):
    newlist = UnorderedList()
    for i in input:
        newlist.add(i)
    newlist.insert(data, pos)
    newlist.print_list()


def test_element_here(position, input):
    newlist = UnorderedList()
    for i in input:
        newlist.add(i)
    print(newlist.element_at(position))


def test_swap(position1, position2, input):
    newlist = UnorderedList()
    for i in input:
        newlist.add(i)
    newlist.swap(position1, position2)
    newlist.print_list()


def test_value_repeats(input):
    newlist = UnorderedList()
    for i in input:
        newlist.add(i)
    return newlist.value_repeats()

test_insert(5, -4, [1, 3, 7, 9, 12]) 
test_insert(5, 2, [1, 3, 7, 9, 12]) 
test_element_here(3, [1, 3, 7, 9, 12]) 
test_swap(3, 1, [1, 3, 7, 9, 12])   
print(test_value_repeats([1, 3, 7, 9, 12]))  
print(test_value_repeats([1, 2, 3, 4, 5, 5, 12])) 
