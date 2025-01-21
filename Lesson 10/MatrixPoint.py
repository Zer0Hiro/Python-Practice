def way(start_x,start_y):
    if start_x== 0 or start_y== 0:
        return 1
    return way(start_x-1,start_y) + way(start_x,start_y-1)

print(way(2,3))
