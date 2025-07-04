class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        length=1
        for _ in operations:
            length*=2

        inc=0
        for op in reversed(operations):
            length//=2
            if k>length:
                k-=length
                if op==1:
                    inc+=1
            else:
                if op==1:
                    pass
        
        return chr((inc) %26 +ord('a'))

