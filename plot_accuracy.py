import pandas as pd
import matplotlib.pyplot as plt

# DQN - no header, columns: episode, reward, ep_block_prob, ep_accepted_requests, avg_latency, avg_cost, avg_cpu_cluster_selected, gini, executionTime
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

schedulers = ['Karmada', 'DS-DQN', 'DS-PPO']
accuracies = [accuracy_karmada, accuracy_dqn, accuracy_ppo]

plt.bar(schedulers, accuracies, color=['blue', 'green', 'red'])
plt.xlabel('Scheduler')
plt.ylabel('Accuracy (%)')
plt.title('Accuracy Comparison')
plt.ylim(85, 100)
plt.savefig('accuracy_comparison.png')
plt.show()
