def work_on_strings(a,b):
    ans_a = [i.swapcase() if (b.count(i) + b.count(i.swapcase())) % 2 else i for i in a]
    ans_b = [i.swapcase() if (a.count(i) + a.count(i.swapcase())) % 2 else i for i in b]
    return ''.join(ans_a) + ''.join(ans_b)