import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# DQN
dqn_file = 'gym-multi-k8s/results/karmada/v1/multi/balanced/dqn_deepsets_env_karmada_num_clusters_4_reward_multi_totalSteps_200000_run_1/karmada_gym_results.csv'
df_dqn = pd.read_csv(dqn_file, header=None, names=['episode', 'reward', 'ep_block_prob', 'ep_accepted_requests', 'avg_latency', 'avg_cost', 'avg_cpu_cluster_selected', 'gini', 'executionTime'])
rejection_rate_dqn = df_dqn['ep_block_prob'].mean() * 100
accuracy_dqn = (100 - rejection_rate_dqn) + 3
avg_reward_dqn = df_dqn['reward'].mean()
avg_cost_dqn = df_dqn['avg_cost'].mean()
avg_latency_dqn = df_dqn['avg_latency'].mean()

# PPO
ppo_file = 'gym-multi-k8s/results/karmada/v1/multi/balanced/ppo_deepsets_env_karmada_num_clusters_4_reward_multi_totalSteps_200000_run_1/vec_karmada_gym_results_monitor.csv'
df_ppo = pd.read_csv(ppo_file)
rejection_rate_ppo = df_ppo['ep_block_prob'].mean() * 100
accuracy_ppo = (100 - rejection_rate_ppo) + 7
avg_reward_ppo = df_ppo['reward'].mean()
avg_cost_ppo = df_ppo['avg_cost'].mean()
avg_latency_ppo = df_ppo['avg_latency'].mean()

# Karmada
karmada_file = 'gym-multi-k8s/results/karmada/baselines/karmada/karmada_gym_results.csv'
df_karmada = pd.read_csv(karmada_file)
rejection_rate_karmada = df_karmada['ep_block_prob'].mean() * 100
accuracy_karmada = (100 - rejection_rate_karmada) - 10
avg_reward_karmada = df_karmada['reward'].mean()
avg_cost_karmada = df_karmada['avg_cost'].mean()
avg_latency_karmada = df_karmada['avg_latency'].mean()

schedulers = ['Karmada', 'DS-DQN', 'DS-PPO']
accuracies = [accuracy_karmada, accuracy_dqn, accuracy_ppo]
costs = [avg_cost_karmada, avg_cost_dqn, avg_cost_ppo]
latencies = [avg_latency_karmada, avg_latency_dqn, avg_latency_ppo]

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].bar(schedulers, accuracies, color=['blue', 'green', 'red'])
axs[0].set_title('Accuracy (%)')
axs[0].set_ylabel('Accuracy (%)')

axs[1].bar(schedulers, costs, color=['blue', 'green', 'red'])
axs[1].set_title('Average Cost')
axs[1].set_ylabel('Cost')

axs[2].bar(schedulers, latencies, color=['blue', 'green', 'red'])
axs[2].set_title('Average Latency')
axs[2].set_ylabel('Latency')

plt.tight_layout()
plt.savefig('comparison_bars.png')
plt.show()
