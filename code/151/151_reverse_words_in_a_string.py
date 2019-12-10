class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list1 = s.split(" ")
        list2 = [x for x in list1 if x != ""]
        list2.reverse()
        return " ".join(list2)