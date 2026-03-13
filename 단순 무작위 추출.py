import seaborn as sns

# 데이터 로드 (모집단 가정)
tips = sns.load_dataset('tips')

# 전체에서 무작위로 30개 추출
simple_random_sample = tips.sample(n=30, random_state=42)

print("--- 단순 무작위 추출 결과 ---")
print(simple_random_sample.head())

#모든 추출 범위가 표본으로 선택될 확률이 동일하게 설계됨
#예시로는 제비뽑기나 로또 번호등 운에 맡겨 뽑는것
#방법이 단순하며,객관적이고,계산이 편함