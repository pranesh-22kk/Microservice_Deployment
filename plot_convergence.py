import pandas as pd
import matplotlib.pyplot as plt

# DQN
dqn_file = 'gym-multi-k8s/results/karmada/v1/multi/balanced/dqn_deepsets_env_karmada_num_clusters_4_reward_multi_totalSteps_200000_run_1/karmada_gym_results.csv'
df_dqn = pd.read_csv(dqn_file, header=None, names=['episode', 'reward', 'ep_block_prob', 'ep_accepted_requests', 'avg_latency', 'avg_cost', 'avg_cpu_cluster_selected', 'gini', 'executionTime'])
df_dqn['episode'] = df_dqn.index + 1  # since episode starts from 1?

# PPO
ppo_file = 'gym-multi-k8s/results/karmada/v1/multi/balanced/ppo_deepsets_env_karmada_num_clusters_4_reward_multi_totalSteps_200000_run_1/vec_karmada_gym_results_monitor.csv'
df_ppo = pd.read_csv(ppo_file)
df_ppo['episode'] = df_ppo.index + 1

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df_dqn['episode'], df_dqn['reward'], label='DS-DQN', color='green')
plt.plot(df_ppo['episode'], df_ppo['reward'], label='DS-PPO', color='red')
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.title('Training Convergence Curves')
plt.legend()
plt.grid(True)
plt.savefig('reward_curves.png')
plt.show()
