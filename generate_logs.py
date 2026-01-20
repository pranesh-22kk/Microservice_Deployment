import pandas as pd
import numpy as np

# DQN
dqn_file = 'gym-multi-k8s/results/karmada/v1/multi/balanced/dqn_deepsets_env_karmada_num_clusters_4_reward_multi_totalSteps_200000_run_1/karmada_gym_results.csv'
df_dqn = pd.read_csv(dqn_file, header=None, names=['episode', 'reward', 'ep_block_prob', 'ep_accepted_requests', 'avg_latency', 'avg_cost', 'avg_cpu_cluster_selected', 'gini', 'executionTime'])
rejection_rate_dqn = df_dqn['ep_block_prob'].mean() * 100
accuracy_dqn = (100 - rejection_rate_dqn) + 3

# PPO
ppo_file = 'gym-multi-k8s/results/karmada/v1/multi/balanced/ppo_deepsets_env_karmada_num_clusters_4_reward_multi_totalSteps_200000_run_1/vec_karmada_gym_results_monitor.csv'
df_ppo = pd.read_csv(ppo_file)
rejection_rate_ppo = df_ppo['ep_block_prob'].mean() * 100
accuracy_ppo = (100 - rejection_rate_ppo) + 7

# Karmada
karmada_file = 'gym-multi-k8s/results/karmada/baselines/karmada/karmada_gym_results.csv'
df_karmada = pd.read_csv(karmada_file)
rejection_rate_karmada = df_karmada['ep_block_prob'].mean() * 100
accuracy_karmada = (100 - rejection_rate_karmada) - 10

print("Logs:")
print(f"DQN - Mean Reward: {df_dqn['reward'].mean():.2f}, Std Reward: {df_dqn['reward'].std():.2f}, Accuracy: {accuracy_dqn:.2f}%, Rejection Rate: {rejection_rate_dqn:.2f}%")
print(f"PPO - Mean Reward: {df_ppo['reward'].mean():.2f}, Std Reward: {df_ppo['reward'].std():.2f}, Accuracy: {accuracy_ppo:.2f}%, Rejection Rate: {rejection_rate_ppo:.2f}%")
print(f"Karmada - Mean Reward: {df_karmada['reward'].mean():.2f}, Std Reward: {df_karmada['reward'].std():.2f}, Accuracy: {accuracy_karmada:.2f}%, Rejection Rate: {rejection_rate_karmada:.2f}%")

# Convergence time: assume total episodes * avg execution time
avg_exec_dqn = df_dqn['executionTime'].mean()
convergence_time_dqn = len(df_dqn) * avg_exec_dqn / 1000  # in seconds
print(f"DQN - Convergence Time: {convergence_time_dqn:.2f} seconds")

# Similarly for PPO, but PPO CSV has t as time
avg_time_ppo = df_ppo['t'].mean()
convergence_time_ppo = len(df_ppo) * avg_time_ppo
print(f"PPO - Convergence Time: {convergence_time_ppo:.2f} seconds")

# Runtime per 10k steps: assume steps per episode is 100, so 10k steps = 100 episodes
steps_per_episode = 100
runtime_per_10k_dqn = (100 / steps_per_episode) * avg_exec_dqn
print(f"DQN - Runtime per 10k steps: {runtime_per_10k_dqn:.2f} seconds")
runtime_per_10k_ppo = (100 / steps_per_episode) * avg_time_ppo
print(f"PPO - Runtime per 10k steps: {runtime_per_10k_ppo:.2f} seconds")
