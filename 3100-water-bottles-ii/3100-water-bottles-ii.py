class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            empty -= numExchange
            numExchange += 1

            total += 1
            empty += 1

        return total

            