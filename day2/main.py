import os

def is_safe(move_set):
    return move_set <= {1,2,3} or move_set <= {-1,-2,-3}

def solution1(data):
    matrix = [[ int(i) for i in line.split()] for line in data.split('\n')]
    num_of_safe = 0
    for line in matrix:
        move_set = set([x-y for x,y in zip(line, line[1:])])
        num_of_safe += is_safe(move_set)
    return num_of_safe
            
def solution2(data):
    def try_line_combinations(line):
        for idx, _ in enumerate(line):
            new_line = line[:idx] + line[idx+1:]
            move_set = set([x-y for x,y in zip(new_line, new_line[1:])])
            if is_safe(move_set):
                return True
        return False
    
    matrix = [[ int(i) for i in line.split()] for line in data.split('\n')]
    num_of_safe = 0
    for line in matrix:
        num_of_safe += try_line_combinations(line)
    return num_of_safe

def main():
    files = os.listdir(os.path.dirname(__file__)) 
    solutions_data = []
    for file in files:
        if file.endswith('.aoc'):
            data = open(os.path.join(os.path.dirname(__file__) ,file)).read()
            solutions_data += 'task1_'+file, solution1(data)
            solutions_data += 'task2_'+file, solution2(data)
            
    return solutions_data
    
if __name__ == '__main__':
    print(main())