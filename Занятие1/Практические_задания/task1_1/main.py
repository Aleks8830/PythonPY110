def get_distance_f1(point: tuple) -> int:
    return (point[0] ** 2 + point[1] ** 2) ** 0.5


def task_f2(points: list) -> list:
    #map(get_distance, points)
    #return [get_distance(point) for point in points]  # TODO записать через map
    return list(map(get_distance_f1, points))

if __name__ == "__main__":
    pts = [
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    print(task_f2(pts))
