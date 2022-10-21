class Solution:
    def isValid(self, s):
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif stack and c == ")" and stack[-1] == "(":
                stack.pop(-1)
            elif c == "}" and stack[-1] == "{":
                stack.pop(-1)
            elif c == "]" and stack[-1] == "[":
                stack.pop(-1)
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid("(()"))

