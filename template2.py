import unittest
from collections import defaultdict
from math import sqrt


def distance(x, y):
    """
    Distance formula
    @param x:
    @param y:
    @return:
    """
    return sqrt(x ** 2 + y ** 2)

def solution(S, X, Y):
    """
    function that takes a string of length N and two arrays X, Y consisting of N integers each.
    @param S: "Strings" example "ABCD"
    @param X: [[int]] Xcord
    @param Y: [[int]] Ycord
    @return: [int]
    """
    tags = defaultdict(list)
    #  groups the points based on their tag
    for i, (x, y) in enumerate(zip(X, Y)):
        tags[S[i]].append((x, y))

    unique_tags = list(tags.keys())

    def count_points(r):
        """
        counts the number of points with distinct tags within the circle for each radius.
        @param r: radius
        @return: int
        """
        count = 0
        for tag in unique_tags:
            points = tags[tag]
            points_in_circle = [p for p in points if distance(p[0], p[1]) <= r]
            if points_in_circle:
                count += 1
        return count

    max_count = 0
    # computes the maximum radius required to include all the points in the circle
    list_radius = [distance(x, y) for x, y in zip(X, Y)]
    min_radius = [i for i, x in enumerate(list_radius) if x == min(list_radius)]
    if len(min_radius) >= 2:
        if S[min_radius[0]] == S[min_radius[1]]:
            return 0
    max_radius = max(list_radius)

    # iterates over all possible radii from 1 to the maximum radius and counts using above function
    for r in range(1, int(max_radius) + 1):
        points_in_circle = count_points(r)
        max_count = max(max_count, points_in_circle)

    return max_count

# class TestBinaryGap(unittest.TestCase):
#     def test_1(self):
#         X = [2,-1,-4,-3,3]
#         Y = [2,-2,4,1,-3]
#         S = "ABDCA"
#         self.assertEqual(solution(S, X, Y), 3)
#
#     def test_2(self):
#         X = [1, 3, 5, 2]
#         Y = [1, 2, 3, 4]
#         S = "ABCD"
#         self.assertEqual(solution(S,X,Y),3)
#
#     def test_3(self):
#         X = [1,-2,-2]
#         Y = [1,-2,2 ]
#         S = "ABB"
#         self.assertEqual(solution(S, X, Y), 1)

if __name__ == "__main__":
    tags = "CCD"
    X = [1, -1, 2]
    Y = [1, -1, -2]
    print(solution(tags, X, Y))
