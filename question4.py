#You are given an n x n 2D matrix representing an image.
#Rotate the image by 180 degrees (anti-clockwise) but after sorting the n*n 2D array
def sort_matrix(matrix):
    flattened = [num for row in matrix for num in row]
    flattened.sort()
    
    n = len(matrix)
    sorted_matrix = [[0] * n for _ in range(n)]
    
    index = 0
    for i in range(n):
        for j in range(n):
            sorted_matrix[i][j] = flattened[index]
            index += 1

    return sorted_matrix

def rotate_180(matrix):
    return [row[::-1] for row in matrix[::-1]]

n = int(input("Enter matrix size (n x n): "))
matrix = []

print("Enter matrix elements row-wise:")
for _ in range(n):
    matrix.append(list(map(int, input().split())))

sorted_matrix = sort_matrix(matrix)
rotated_matrix = rotate_180(sorted_matrix)

print("\nSorted Matrix:")
for row in sorted_matrix:
    print(*row)

print("\nRotated Matrix:")
for row in rotated_matrix:
    print(*row)

