def exercise1(tp, fp, fn):
    if type(tp) is not int:
        return print('tp must be int')
    if type(fp) is not int:
        return print('fp must be int')
    if type(fn) is not int:
        return print('fn must be int')
    if tp <= 0 or fp <= 0 or fn <= 0:
        return print('tp and fp and fn must be greater than zero')
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(f'precision is : {precision}\n'
          f'recall is : {recall}\n'
          f'f1_score is : {f1_score}')


exercise1(tp=2, fp=3, fn=4)
exercise1(tp="a", fp=3, fn=4)
exercise1(tp=2, fp="a", fn=4)
exercise1(tp=2, fp=3, fn="a")
exercise1(tp=2, fp=3, fn=0)
exercise1(tp=2.1, fp=3, fn=0)
