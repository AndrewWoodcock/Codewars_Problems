

# have to look at the next word as well?

def main():

    inp_string = 'hello world'
    limit = 7
    split = inp_string.strip().split()

    out_string = ''

    line_cnt = 0
    for word in split:
        if (line_cnt + len(word)) + 1 > limit:
            out_string = out_string + word + ' ' + '\n'
            line_cnt = 0
        else:
            line_cnt + len(word) + 1
            out_string = out_string + word + ' '

    print(out_string)



if __name__ == '__main__':
    main()
