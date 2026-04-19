# HephaestusForge

Code repository for the paper entitled 
"HephaestusForge: Optimal Microservice Deployment across
the Compute Continuum via Reinforcement Learning", submitted to Elsevier FGCS.

## Overview

HephaestusForge is a reinforcement learning-based system for optimizing microservice deployment across distributed computing environments. It uses advanced RL algorithms (DQN and PPO) with Deep Sets architecture to efficiently schedule workloads across multi-cluster Kubernetes environments.

## Features

- 🤖 **Deep Reinforcement Learning**: DQN and PPO agents with Deep Sets architecture for permutation-invariant learning
- ☸️ **Multi-Cluster Scheduling**: Simulates Karmada-based Kubernetes multi-cluster scheduling
- 📊 **Interactive Dashboard**: Streamlit-based web interface for visualization and control
- 📈 **Performance Analytics**: Built-in tools for convergence analysis, accuracy computation, and comparison plots
- 🔄 **Multiple Baselines**: Compare against traditional scheduling algorithms

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd HephaestusForge-main
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Interface

Launch the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 🚀 Deploy Publicly (For Placements/Showcase)

Want to share this with recruiters or showcase in interviews? Deploy it for free!

### Option 1: Streamlit Community Cloud (Recommended - FREE)

**Perfect for placements! One-click deployment, free hosting.**

1. Push your code to GitHub (public repository)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app" and select your repository
5. Set main file path: `app.py`
6. Click "Deploy"!

**Result**: Get a public URL like `https://your-app.streamlit.app` that anyone can access!

### Option 2: Hugging Face Spaces (FREE)

1. Create account at [huggingface.co/spaces](https://huggingface.co/spaces)
2. Create new Space → Select "Streamlit"
3. Upload your files or connect GitHub
4. Auto-deploys with public URL

### Option 3: Railway.app (FREE tier available)

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

### Option 4: Render.com (FREE)

1. Connect your GitHub repo at [render.com](https://render.com)
2. Create new "Web Service"
3. Build command: `pip install -r requirements.txt`
4. Start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

### 💡 Tips for Placements

- **Add live demo link** to your resume
- **Share during interviews** - let recruiters interact with it
- **Include in GitHub README** - showcase on your profile
- **Record demo video** - for quick presentations
- **Monitor usage** - shows real user engagement

### Running Experiments

#### Train RL Agents
```bash
# Run in gym-multi-k8s directory
cd gym-multi-k8s
python run.py
```

#### Run Baseline Comparisons
```bash
cd gym-multi-k8s
python run_baselines.py
```

#### Evaluate Trained Models
```bash
cd gym-multi-k8s
python evaluation.py
```

### Visualization Scripts

- **Plot Convergence**: `python plot_convergence.py`
- **Plot Accuracy**: `python plot_accuracy.py`
- **Plot Comparison**: `python plot_comparison.py`
- **Generate Summary**: `python final_summary.py`

## Project Structure

```
HephaestusForge-main/
├── app.py                      # Main Streamlit web application
├── requirements.txt            # Python dependencies
├── gym-multi-k8s/             # Core RL environment
│   ├── envs/                  # Custom gym environments
│   │   ├── karmada_scheduling_env.py  # Karmada scheduling environment
│   │   ├── fog_env.py         # Fog computing environment
│   │   ├── dqn_deepset.py     # DQN with Deep Sets
│   │   ├── ppo_deepset.py     # PPO with Deep Sets
│   │   └── utils.py           # Utility functions
│   ├── run.py                 # Training script
│   ├── run_baselines.py       # Baseline algorithms
│   ├── evaluation.py          # Model evaluation
│   ├── results/               # Training results
│   └── runs/                  # TensorBoard logs
├── check_dqn.py               # DQN model verification
├── check_ppo.py               # PPO model verification
├── compute_accuracy.py        # Accuracy computation
├── plot_convergence.py        # Convergence visualization
├── plot_accuracy.py           # Accuracy plots
├── plot_comparison.py         # Algorithm comparison
└── runs/                      # TensorBoard event files

```

## Key Components

### Reinforcement Learning Agents

1. **Deep Q-Network (DQN)**: Value-based RL with experience replay and target networks
2. **Proximal Policy Optimization (PPO)**: Policy gradient method with clipped objective
3. **Deep Sets**: Permutation-invariant architecture for handling variable-length cluster sets

### Environments

- **Karmada Scheduling Environment**: Multi-cluster Kubernetes scheduling simulation
- **Fog Computing Environment**: Edge-to-cloud resource allocation

### Scheduling Policies

- Spread: Distribute replicas evenly across clusters
- Binpack: Consolidate replicas to minimize cluster usage
- Custom RL policies: Learned optimal placement strategies

## Monitoring and Logs

- **TensorBoard**: View training metrics and convergence
```bash
tensorboard --logdir=runs
```

- **CSV Logs**: Training and evaluation results stored in `gym-multi-k8s/` directory

## Results

Experimental results comparing RL agents against baseline algorithms are stored in:
- `gym-multi-k8s/results/` - Detailed evaluation metrics
- `*.csv` files - Training logs with various configurations

## Citation

If you use this code in your research please cite:

```
HephaestusForge: Optimal Microservice Deployment across
the Compute Continuum via Reinforcement Learning
Submitted to Elsevier Future Generation Computer Systems (FGCS)
```

## License

[Add your license information here]

## Contact

[Add contact information here]

## 🎯 For Recruiters & Interviewers

This project demonstrates:
- **Machine Learning**: Deep Reinforcement Learning (DQN, PPO)
- **Cloud Computing**: Kubernetes multi-cluster scheduling
- **Web Development**: Interactive Streamlit dashboard
- **System Design**: Distributed resource management
- **Research**: Based on academic paper submitted to Elsevier FGCS

**Live Demo**: [Add your deployed URL here]

## Acknowledgments

This work is part of research on intelligent resource management for distributed computing systems.
