class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #top, left, down, right
        dir = [[1,0], [0,-1], [-1,0], [0,1]] 
        cur = dir[0]
        location = [0,0]
        i = 0
        instrucions = list(instructions)
        loop = 0
        while(True):
            ins = instructions[i]
            if cur == [1,0]:
                if ins == "L": cur = dir[1]
                if ins == "R": cur = dir[3]
            elif cur == [0,-1]:
                if ins == "L": cur = dir[2]
                if ins == "R": cur = dir[0]
            elif cur == [-1,0]:
                if ins == "L": cur = dir[3]
                if ins == "R": cur = dir[1]
            elif cur == [0,1]:
                if ins == "L": cur = dir[0]
                if ins == "R": cur = dir[2]
            if ins == "G":
                location[0] += cur[0]
                location[1] += cur[1]
            i += 1
            if i == len(instructions):
                i = 0
                loop += 1
            if location == [0,0]:
                return True
            if loop > 4:
                return False
s = Solution()
print(s.isRobotBounded("GLGLGGLGL"))
