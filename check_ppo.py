import pandas as pd
df = pd.read_csv('gym-multi-k8s/results/karmada/v1/multi/balanced/ppo_deepsets_env_karmada_num_clusters_4_reward_multi_totalSteps_200000_run_1/vec_karmada_gym_results_monitor.csv')
print("PPO Columns:", df.columns)
print("PPO Head:")
print(df.head())
