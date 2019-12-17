#!/usr/bin/python3
def multiple_returns(sentence):
    t = []
    t.append(len(sentence))
    if len(sentence) == 0:
        t.append(None)
    else:
        t.append(sentence[0])
    return (t)
