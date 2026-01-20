import pandas as pd
df = pd.read_csv('gym-multi-k8s/results/karmada/baselines/karmada/karmada_gym_results.csv')
print("Karmada Columns:", df.columns)
print("Karmada Head:")
print(df.head())
