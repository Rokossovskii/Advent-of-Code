import os

def insert_character_margin_on_data(data, margin=3):
    data = data.split('\n')
    length_of_column = len(data[0])
    top_margin = bottom_margin = '-'*(length_of_column+margin*2)
    return '\n'.join([top_margin]*margin + ['-'*margin  + line + '-'*margin for line in data] + [bottom_margin]*margin)
    
def find_string_in_data(data, string):
    pass

def search_for_string_in_all_directions(data, string):
    pass
    
def solution1(data):
    print(insert_character_margin_on_data(data))

def solution2(data):
    pass

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