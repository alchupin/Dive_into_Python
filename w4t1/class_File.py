import tempfile
import os

class File():
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_path_split = file_path.split('/')[-1] 
        self.current = 0
        try:
            with open(self.file_path, 'r') as f:
                pass
        except FileNotFoundError:
            with open(self.file_path, 'w') as f:
                pass
    
    def get_file_path(self):
        return self.file_path    
        
        
    def write(self, new_str):
        with open(self.file_path, 'a') as f:
            f.write(new_str)
            
        
    def __add__(self, File):
        new_path = self.file_path_split + ' and ' + File.get_file_path().split('/')[-1]
        print('New path = ' + new_path)
        
        with open(self.file_path, 'r') as f1:
            data1 = f1.read()
            
            with open(File.get_file_path(), 'r') as f2:
                data2 = f2.read()
                
                with open(os.path.join(tempfile.gettempdir(), new_path), 'w') as f:
                    f.write(data1 + '\n' + data2)
                
        return self
        
    
    
    def __iter__(self):
        return self
    
    def __next__(self):
        with open(self.file_path) as f:
            data = f.readlines()
            print(self.current, len(data))
            if self.current == len(data):
                raise StopIteration()
            result = data[self.current]
            self.current += 1
            
            return result
            
    def __str__(self):
        return '{}'.format(self.file_path)


if __name__ == '__main__':
    
    
    my_file = File('file1.txt')
    for line in File('file1.txt'):
        print(line, end='')
    
    print(File('file_print.txt'))
    
'''

my_file.write('I wrote this string with method write')
new_file = File('file2.txt')

result_file = my_file + new_file

'''
        
        
        
