# https://leetcode.com/problems/climbing-stairs/

class StairsClimber:
    @staticmethod
    def climb_stairs(stairs_number: int) -> int:
        if stairs_number <= 0:
            return 0
        if stairs_number <= 2:
            return stairs_number
        calculations = (1, 2)
        for i in range(3, stairs_number + 1):
            calculations = (calculations[1], sum(calculations))
        return calculations[-1]


if __name__ == '__main__':
    climber = StairsClimber()
    print(climber.climb_stairs(9))
