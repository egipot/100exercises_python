#46 Letter Extractor
#Write a script that extracts letters from the 26 text files that we created in the previous exercise and then put those letters in a python list and print out the list.

#egi solution
import string
letter_list = []
for letter in string.ascii_lowercase:
    with open(letter + '.txt', 'r') as f:
        #letter_list.append(f) --> wrong as it prints:
        #[<_io.TextIOWrapper name='a.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='b.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='c.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='d.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='e.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='f.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='g.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='h.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='i.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='j.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='k.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='l.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='m.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='n.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='o.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='p.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='q.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='r.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='s.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='t.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='u.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='v.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='w.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='x.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='y.txt' mode='r' encoding='UTF-8'>, <_io.TextIOWrapper name='z.txt' mode='r' encoding='UTF-8'>]
        letter_list.append(letter) #this is the correct answer

print(letter_list)


#ardit answer
import glob

letters_ardit = []
file_list = glob.glob('44_letters_ardit/*.txt')

for filename in file_list:
    with open(filename, 'r') as file:
        letters_ardit.append(file.read().strip('\n'))

print(letters_ardit)
#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']