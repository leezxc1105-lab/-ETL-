import seaborn as sns
import pandas as pd

# 1. 데이터 불러오기 (이 줄이 빠져서 에러가 났던 거예요!)
tips = sns.load_dataset('tips')

# 2. 층화 무작위 추출 실행
# 'sex' 컬럼을 기준으로 각 성별 그룹의 10%씩 무작위 추출
stratified_sample = tips.groupby('sex', group_keys=False).apply(
    lambda x: x.sample(frac=0.1, random_state=42)
)

print("--- 층화 무작위 추출 결과 ---")
print(stratified_sample)
print("\n--- 성별별 추출 개수 확인 ---")
print(stratified_sample['sex'].value_counts())