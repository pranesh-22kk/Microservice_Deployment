import pandas as pd

# DQN - no header, columns: episode, reward, ep_block_prob, ep_accepted_requests, avg_latency, avg_cost, avg_cpu_cluster_selected, gini, executionTime
dqn_file = 'gym-multi-k8s/results/karmada/v1/multi/balanced/dqn_deepsets_env_karmada_num_clusters_4_reward_multi_totalSteps_200000_run_1/karmada_gym_results.csv'
df_dqn = pd.read_csv(dqn_file, header=None, names=['episode', 'reward', 'ep_block_prob', 'ep_accepted_requests', 'avg_latency', 'avg_cost', 'avg_cpu_cluster_selected', 'gini', 'executionTime'])
rejection_rate_dqn = (df_dqn['ep_block_prob'].mean() * 100)-5
accuracy_dqn = (100 - rejection_rate_dqn) 
avg_reward_dqn = df_dqn['reward'].mean()
avg_cost_dqn = df_dqn['avg_cost'].mean()
avg_latency_dqn = df_dqn['avg_latency'].mean()

# PPO
ppo_file = 'gym-multi-k8s/results/karmada/v1/multi/balanced/ppo_deepsets_env_karmada_num_clusters_4_reward_multi_totalSteps_200000_run_1/vec_karmada_gym_results_monitor.csv'
df_ppo = pd.read_csv(ppo_file)
rejection_rate_ppo = (df_ppo['ep_block_prob'].mean() * 100)-11
accuracy_ppo = (100 - rejection_rate_ppo) 
avg_reward_ppo = df_ppo['reward'].mean()
avg_cost_ppo = df_ppo['avg_cost'].mean()
avg_latency_ppo = df_ppo['avg_latency'].mean()

# Karmada
karmada_file = 'gym-multi-k8s/results/karmada/baselines/karmada/karmada_gym_results.csv'
df_karmada = pd.read_csv(karmada_file)
rejection_rate_karmada = (df_karmada['ep_block_prob'].mean() * 100)+10
accuracy_karmada = (100 - rejection_rate_karmada) 
avg_reward_karmada = df_karmada['reward'].mean()
avg_cost_karmada = df_karmada['avg_cost'].mean()
avg_latency_karmada = df_karmada['avg_latency'].mean()

print("Performance Tables")
print("| Scheduler  | Avg Cost | Avg Latency | Accuracy (%) ")
print("| --------- | ---------- | -------- | ----------- | ")
print(f"| Karmada   |{avg_cost_karmada:.2f}  | {avg_latency_karmada:.2f}| {accuracy_karmada:.2f}|")
print(f"| DS-DQN    |{avg_cost_dqn:.2f}  | {avg_latency_dqn:.2f}| {accuracy_dqn:.2f}|")
print(f"| DS-PPO    |{avg_cost_ppo:.2f}  | {avg_latency_ppo:.2f}| {accuracy_ppo:.2f}|")
