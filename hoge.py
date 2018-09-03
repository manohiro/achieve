from decimal import Decimal
def check_sample(param):
    # リストが空の場合は0を返す
    if not param:
        return 0
    
    # 最大値と最小値を取得
    maxValue = max(param)
    minValue = min(param)
    
    # 最大値、最小値の型が浮動小数点数かチェック
    if type(maxValue) is float or type(minValue) is float:
        # 浮動小数点数の場合、Decimal型で計算
        return Decimal(str(maxValue)) - Decimal(str(minValue))
    else:
        # 整数の場合はそのまま計算
        return max(param) - min(param)        

result = check_sample([1,1.9])
print(result)

