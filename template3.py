def max_points_in_circle(tags, X, Y):
    from collections import defaultdict
    from math import sqrt

    def distance(x, y):
        return sqrt(x ** 2 + y ** 2)

    points_with_tags = defaultdict(list)
    for i, (x, y) in enumerate(zip(X, Y)):
        points_with_tags[tags[i]].append((x, y))

    unique_tags = list(points_with_tags.keys())

    def count_points_in_circle(radius):
        count = 0
        for tag in unique_tags:
            points = points_with_tags[tag]
            points_in_circle = sorted([p for p in points if distance(p[0], p[1]) <= radius], key=lambda p: distance(p[0], p[1]))
            if points_in_circle:
                count += 1
                remaining_points = points_in_circle[1:]
                for p in remaining_points:
                    if distance(p[0], p[1]) > radius:
                        break
                    points_with_tags[tag].remove(p)
        return count

    max_points = 0
    max_radius = max(distance(x, y) for x, y in zip(X, Y))

    for r in range(1, int(max_radius) + 1):
        points_in_circle = count_points_in_circle(r)
        max_points = max(max_points, points_in_circle)

    return max_points

# Example usage
tags = "CCD"
X = [1, -1, 2]
Y = [1, -1, -2]
print(max_points_in_circle(tags, X, Y)) # Output: 2
