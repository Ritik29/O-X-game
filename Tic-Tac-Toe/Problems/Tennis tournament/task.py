n = int(input())
result = [input() for _ in range(n)]
winners = [x.replace(' win', '') for x in result if x.endswith('win')]
print(winners)
print(len(winners))