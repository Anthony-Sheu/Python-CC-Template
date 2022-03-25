def luhn(s): return sum([int(i) if not ind%2 else sum([int(j) for j in str(int(i)*2)]) for ind, i in enumerate(s[::-1])]) % 10
