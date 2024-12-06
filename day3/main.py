import os
import re
from functools import reduce
from operator import mul

def remove_between_do_dont(data):
    return re.sub(r'don\'t\(\).*?do\(\)', " ", data.replace('\n', ''))

def return_every_regex_equal_to(regex:str, data:str): 
    return re.findall(regex, data, flags=0)

def evaluate_command(command):
    match command:
        case command if re.match(r'mul', command):
            return re.findall(r'\d{1,3}', command, flags=0)

def solution1(data):
    return sum([reduce(mul, map(int, evaluate_command(mull_comand))) for mull_comand in return_every_regex_equal_to(r'mul\(\d{1,3},\d{1,3}\)', data)])
    
def solution2(data):
    return sum([reduce(mul, map(int, evaluate_command(mull_comand))) for mull_comand in return_every_regex_equal_to(r'mul\(\d{1,3},\d{1,3}\)', remove_between_do_dont(data))])
    
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
    main()
        