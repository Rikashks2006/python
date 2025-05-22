if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Get all unique grades sorted
    unique_scores = sorted(set(score for name, score in students))
    
    # Second lowest grade
    second_lowest = unique_scores[1]

    # Filter names with the second lowest grade
    names = [name for name, score in students if score == second_lowest]

    # Print names in alphabetical order
    for name in sorted(names):
        print(name)
