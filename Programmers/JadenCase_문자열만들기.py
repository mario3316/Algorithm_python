def solution(s):
    s_list = list(s)
    is_first = True

    for i in range(len(s_list)):
        if s_list[i] != ' ' and is_first:
            s_list[i] = s_list[i].upper()
            is_first = False
        elif s_list[i] != ' ' and not is_first:
            s_list[i] = s_list[i].lower()
        else:
            is_first = True

    return ''.join(s_list)
