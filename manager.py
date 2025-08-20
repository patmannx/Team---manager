# manager.py
import subprocess
import time

# List of agents (Python scripts) to manage
AGENTS = [
    "strategy1.py",
    "strategy2.py",
    "strategy3.py"
]

def run_agent(agent):
    """Run a single agent script in a subprocess."""
    print(f"Starting {agent}...")
    return subprocess.Popen(["python", agent])

def main():
    processes = []

    # Start all agents
    for agent in AGENTS:
        try:
            proc = run_agent(agent)
            processes.append(proc)
        except Exception as e:
            print(f"Error starting {agent
