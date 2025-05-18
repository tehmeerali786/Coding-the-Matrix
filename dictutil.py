def dict2list(dct, keylist): return [dct[i] for i in keylist]

def list2dict(L, keylist): return  {j:i for i,j in zip(L, keylist)}

def listrange2dict(L): return {i:L[i] for i in range(len(L))}
