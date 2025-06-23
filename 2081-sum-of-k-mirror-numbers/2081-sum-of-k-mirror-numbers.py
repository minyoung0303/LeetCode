class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        def is_palindrome(s):
            return s == s[::-1]

        def to_base_k(num, k):
            res = ''
            while num > 0:
                res = str(num % k) + res
                num //= k
            return res or '0'
        
        def generate_palindromes():
            # 한 자리 수부터 시작
            length = 1
            while True:
                # 홀수 길이 회문
                for half in range(10 ** (length - 1), 10 ** length):
                    s = str(half)
                    yield int(s + s[-2::-1])
                # 짝수 길이 회문
                for half in range(10 ** (length - 1), 10 ** length):
                    s = str(half)
                    yield int(s + s[::-1])
                length += 1

        count = 0
        total = 0
        for num in generate_palindromes():
            if is_palindrome(to_base_k(num, k)):
                total += num
                count += 1
                if count == n:
                    return total
