def edit(filename):
    orig = open(filename + '.txt', 'r')
    edited = open(filename + '.tex', 'w')
    original = orig.readlines()
    orig.close()
    original[0] = '\chap{' + original[0] + '}'
    for line in original:
        line = line.replace(' – ', '~---~')
        words = line.split(' ')
        line = ''
        for word in words:
            line += word
            line += ' ' if len(word) > 2 and not word.isdigit() else '~'
        line = line.replace('. ', '.\n')
        line += '\n'
        edited.write(line)


if __name__ == '__main__':
    edit('content/' + str(input()))
