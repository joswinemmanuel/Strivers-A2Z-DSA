class Solution:
    def dataTypeSize(self, str):
        # Code here
        if str == "Character":
            return 1
        elif str == "Integer" or str == "Float":
            return 4
        elif str == "Long" or str == "Double":
            return 8
        else:
            return -1
