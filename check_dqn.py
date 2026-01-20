import pandas as pd
df = pd.read_csv('gym-multi-k8s/results/karmada/v1/multi/balanced/dqn_deepsets_env_karmada_num_clusters_4_reward_multi_totalSteps_200000_run_1/karmada_gym_results.csv')
print("DQN Columns:", df.columns)
print("DQN Head:")
print(df.head())
