import itertools

n = int(input())
lis = [x for x in range(n)] # 0からn-1までのリスト

permutations_lis = itertools.permutations(lis)# 全ての場合のリストを生成
# 以下出力
for one_case in permutations_lis:
  for num in one_case:
    print(num, end=" ")
  print("")
