class Solution:
    # @return: The same instance of this class every time
    instance = None
    @classmethod
    def getInstance(cls):
        # write your code here
        if cls.instance is None:
            cls.instance = Solution()
        return cls.instance
