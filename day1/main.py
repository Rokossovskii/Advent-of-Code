import os

def solution1(data):
    return sum([abs(x-y) for x, y in zip(sorted([int(num) for idx,num in enumerate(data.split()) if idx % 2 == 0]),sorted([int(num) for idx,num in enumerate(data.split()) if idx % 2 == 1]))])
    #       ^               ^                           ^                        ^
    #    and sum | take absolute difference  | zip two sorted lists | sort even and odd numbers
    
def solution2(data):
    return sum([i for i in [int(num) for idx,num in enumerate(data.split()) if idx % 2 == 1] for j in [int(num) for idx,num in enumerate(data.split()) if idx % 2 == 0] if i == j])
    #       ^               ^                                                          ^                                                                                      ^                    
    #    and sum | place element from first list   |  iterate over odd numbers (first list) and iterate over even numbers (second list) |  check if element from first list is in second list
    #            | every time it is in second list |  
    #            | axb = a+a+a+a.... b times       |                        
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