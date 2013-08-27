# 1. open the file
def main():
    file = open('pythoncode.txt', 'r')
    file_remove = open('pythoncode_remove.txt', 'w+')
    
# 2. remove the line number
    for line in file:
        print(line)
        if line[1]== ' ': # for line number is less than 10
            file_remove.write(line[2:])
        elif line[1] == '\n': # for lines with only line number
            continue
        elif line[2]== ' ': # for line number is more than 10
            file_remove.write(line[3:])
    
#lineNremove()
# 3. save and close the file
    file.close()
    file_remove.close()
# def lineNRemove():
    
main()