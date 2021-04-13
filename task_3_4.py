def keys_find(nm):
    key_ar = []
    for idx_f in nm:
        if idx_f[idx_f.find(' ')+1] not in key_ar:
            key_ar.append(idx_f[idx_f.find(' ')+1])
    ks = sorted(key_ar)
    return ks


def keys_find_fn(fn):
    key_fn_ar = []
    for idx_fn in fn:
        if idx_fn[0] not in key_fn_ar:
            key_fn_ar.append(idx_fn[0])
    ks_fns = sorted(key_fn_ar)
    return ks_fns


def thesaurus_adv(nfn):
    res_voc = {}
    keys = keys_find(nfn)
    for idx in keys:
        val = list(filter(lambda el, k=idx: el[el.find(' ') + 1].startswith(k), nfn))
        keys_fn = keys_find_fn(val)
        res_voc_fn = {}
        for idx_2 in keys_fn:
            val_fn = list(filter(lambda el, k=idx_2: el[0].startswith(k), val))
            res_voc_fn.update({idx_2: val_fn})
        res_voc.update({idx: res_voc_fn})
    return res_voc


names = ('Иван Смирнов', 'Анна Довлатова', 'Илья Сергеев', 'Петр Романов', 'Яков Перельман', 'Сергей Петрушенко')
print(thesaurus_adv(names))
