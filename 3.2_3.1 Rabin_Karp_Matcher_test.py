import sys

"""
52 тест. нужно отказаться от того, что после сравнения хэшей, 
вы сравниваете паттерн с подстрокой. вы уже представили такую 
хэш функцию, у которой коллизии настолько минимальны, что тяжело 
придумать такие тесты, чтобы при совпадении хэш функций не 
совпадали паттерн с подстрокой

действительно замена посимвольной проверки на слайс помогла 
пройти 52 тест по времени. Спасибо.

Завис на 52 тесте. Просто поменял порядок проверки строки не 
от 0 к len(P), а от  len(P) к 0 зная что судя по лекции будут 
варианты подобные (T = aaaaaaab, P = aaa) ну то есть отличительный 
символ будет в конце). Прошел тест ) слава слепому тыку)

а 52й на Пайтоне помогло пройти сравнение паттерна со срезом вместо 
посимвольного сравнения в цикле.

взять :p = 2**31 - 1 и x = 257, и убрать посимвольную проверку
"""

def Rabin_Karp_Matcher(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d,m-1)%q
    p = 0
    t = 0
    result = []
    for i in range(m): # preprocessing
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(text[i]))%q
    for s in range(n-m+1): # note the +1
        if p == t: # check character by character
            result = result + [s]
            # match = True
            # for i in range(m):
            #     if pattern[i] != text[s+i]:
            #         match = False
            #         break
            # if match:
            #     result = result + [s]
        if s < n-m:
            t = (t-h*ord(text[s]))%q # remove letter s
            t = (t*d+ord(text[s+m]))%q # add letter s+m
            t = (t+q)%q # make sure that t >= 0
    return result


reader = (line.split() for line in sys.stdin)
pattern = next(reader)[0]  # Pattern
text = next(reader)[0]  # Text

q = 2**31
d = 257
f = []

if len(pattern) == 1:
    for number, char in enumerate(text):
        if char == pattern:
            f.append(number)
else:
    f = Rabin_Karp_Matcher(text, pattern, d, q)

print(*f)