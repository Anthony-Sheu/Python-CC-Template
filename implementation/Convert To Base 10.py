def b10(base, num): return sum([int(num[i])*pow(base, len(num)-1-i) for i in range(len(num))])  # num must be provided as a string
