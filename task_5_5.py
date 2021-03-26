from time import perf_counter
from sys import getsizeof

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start1 = perf_counter()
unique_src = set()
repeated_src = set()

for num in src:
    if num in repeated_src:
        continue
    if num in unique_src:
        unique_src.discard(num)
        repeated_src.add(num)
        continue
    unique_src.add(num)

src = [el for el in src[:] if el in unique_src]
print(src, '\n', perf_counter() - start1, '\n', getsizeof(src) + getsizeof(unique_src) + getsizeof(repeated_src))
