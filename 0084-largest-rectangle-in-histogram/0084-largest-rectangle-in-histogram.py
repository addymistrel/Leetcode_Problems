class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        length = len(heights)

        for i in range(length):
            while stack and heights[i] < heights[stack[-1]]:
                bar = stack.pop()
                pse = stack[-1] if stack else -1
                nse = i
                area = max(area, heights[bar] * (nse - pse - 1))
            stack.append(i)

        while stack:
            bar = stack.pop()
            pse = stack[-1] if stack else -1
            nse = length
            area = max(area, heights[bar] * (nse - pse - 1))

        return area