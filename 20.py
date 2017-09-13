class StackUnderflow(ValueError):
    pass

class SStack():
    def __init__(self):
        self._elems = []
    def is_empty(self):
        return self._elems == []
    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]
    def push(self,elem):
        self._elems.append(elem)
    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()
                   
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parens = "()[]{}"
        open_parens = "([{"
        oppsite = {")":"(","]":"[","}":"{"}
        
        st = SStack()
        for x in s:
            if x in open_parens:
                st.push(x)
            elif st.is_empty():
                return False
            elif st.pop() != oppsite[x]:
                return False
            else:
                pass
        return st.is_empty()