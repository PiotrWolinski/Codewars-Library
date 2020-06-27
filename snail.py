def snail(snail_map):
    size = len(snail_map[0])
    row = 0
    col = 0
    ans = []
    visited = [ [ 0 for col in range(0, size) ] for row in range(0, size)]
    while any(0 in sublist for sublist in visited):
        while col < size - 1 and not visited[row][col + 1]:
            ans.append(snail_map[row][col])
            visited[row][col] = 1
            col += 1
        while row < size - 1 and not visited[row + 1][col]:
            ans.append(snail_map[row][col])
            visited[row][col] = 1
            row += 1
        while col > 0 and not visited[row][col - 1]:
            ans.append(snail_map[row][col])
            visited[row][col] = 1
            col -= 1
        while row > 0 and not visited[row - 1][col]:
            ans.append(snail_map[row][col])
            visited[row][col] = 1
            row -= 1

        zeros = sum(sub.count(0) for sub in visited)
        if not visited[row][col] and zeros == 1:
            ans.append(snail_map[row][col])
            visited[row][col] = 1

    return ans