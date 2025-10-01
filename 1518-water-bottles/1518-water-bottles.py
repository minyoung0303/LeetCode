class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # 지금까지 마신 병 수
        total = numBottles
        # 현재 가지고 있는 빈 병 수
        empty = numBottles
        while empty >= numExchange:
            exchange = empty // numExchange
            total += exchange
            empty = empty % numExchange + exchange
        
        return total
            