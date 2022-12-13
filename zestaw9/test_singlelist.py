import pytest
from singlelist import SingleList
from node import Node

class TestSingleList:

    @pytest.fixture(scope="class")
    def SingleListA(self):
        list = SingleList()
        list.insert_tail(Node(1, None))
        list.insert_tail(Node(2, None))
        list.insert_tail(Node(3, None))
        list.insert_tail(Node(4, None))
        list.insert_tail(Node(5, None))
        return list

    @pytest.fixture(scope="class")
    def SingleListB(self):
        list = SingleList()
        list.insert_tail(Node(6, None))
        list.insert_tail(Node(7, None))
        list.insert_tail(Node(8, None))
        list.insert_tail(Node(9, None))
        list.insert_tail(Node(10, None))
        return list

    def testRemoveTail(self, SingleListA, SingleListB):
        assert str(SingleListA.remove_tail()) == '5'
        assert str(SingleListA.tail)== '4'
        SingleListA.insert_tail(Node(5))
        assert str(SingleListB.remove_tail()) == '10'
        assert str(SingleListB.tail) == '9'
        SingleListB.insert_tail(Node(10))

    def testJoin(self, SingleListA, SingleListB):
        SingleListA.join(SingleListB)
        assert str(SingleListA.head) == '1'
        assert str(SingleListA.tail) == '10'
        assert SingleListB.is_empty() == True

        SingleListB.join(SingleListA)
        assert SingleListA.is_empty() == True
        assert str(SingleListB.head) == '1'
        assert str(SingleListB.tail) == '10'

    def testClear(self, SingleListA, SingleListB):
        assert SingleListA.is_empty() == True
        SingleListB.clear()
        assert SingleListB.is_empty() == True
