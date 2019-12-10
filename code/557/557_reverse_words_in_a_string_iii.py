class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list1 = s.split(" ")
        list2 = []
        for x in list1:
            list2.append(x[::-1])
        return " ".join(list2)