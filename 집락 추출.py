import seaborn as sns
import random

# 1. 데이터 불러오기
tips = sns.load_dataset('tips')

# 2. 집락(Cluster) 설정: 'day'별로 그룹화
# tips 데이터의 요일 종류: ['Thur', 'Fri', 'Sat', 'Sun']
clusters = tips['day'].unique().tolist()

# 3. 집락 중 무작위로 n개 선택 (예: 요일 1개 선택)
selected_clusters = random.sample(clusters, 1)

# 4. 선택된 집락에 속한 데이터 모두 추출
cluster_sample = tips[tips['day'].isin(selected_clusters)]

print(f"✅ 선택된 집락(요일): {selected_clusters}")
print(f"✅ 추출된 표본 개수: {len(cluster_sample)}개")
print("-" * 30)
print(cluster_sample.head())
#구성원에 대한 전수 조사 (제비뽑기를 해서 그 그굷을 통째로 조사하는 것)
#시간과 비용 절약,목록 작성의 편리함
