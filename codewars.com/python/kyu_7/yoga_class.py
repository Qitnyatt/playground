# https://www.codewars.com/kata/yoga-class/train/python


def yoga(classroom, poses):
    total_poses = 0

    for pose in poses:
        for row in classroom:
            sum_row = sum(row)
            for person in row:
                if sum_row + person >= pose:
                    total_poses += 1

    return total_poses
