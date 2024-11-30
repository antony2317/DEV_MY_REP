def palindrop(s):
    s_lower = s.lower()
    return s_lower == s_lower[::-1]
print(list(filter(palindrop,['анна', 'перо', 'заказ', 'кабак', 'ведро'])))

