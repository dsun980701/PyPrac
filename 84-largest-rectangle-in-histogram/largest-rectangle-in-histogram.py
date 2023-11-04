class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Use monotonically increasing stack.
        '''
        stack, result = [], 0
        for height in heights + [-1]:
            step = 0
            while stack and stack[-1][1] >= height:
                width, h = stack.pop()
                step += width
                result = max(result, step* h)
            stack.append((step + 1, height))
        return result
        '''

        result, stack = 0, [] #Tuple(height,index)
        for height in heights + [-1]:
            step = 0
            while stack and stack[-1][0] >= height:
                h, w = stack.pop()
                step += w
                result = max(result, h * step)
            stack.append((height, step + 1))
        return result






















