import subprocess

def ask_permission(command):
    """
    Stops the agent and waits for your manual 'Y' or 'N'.
    """
    print(f"\n⚠️  AGENT WANTS TO RUN THIS COMMAND: \033[93m{command}\033[0m")
    user_input = input("Allow execution? (y/N): ").lower()
    
    if user_input == 'y':
        try:
            # Runs the command safely in your Linux Mint terminal
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            print("✅ Execution successful.")
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"❌ Command failed: {e.stderr}")
            return e.stderr
    else:
        print("🚫 Command blocked by user.")
        return "User denied permission for this command."

# Example: The agent tries to install a library
# ask_permission("pip install requests")
