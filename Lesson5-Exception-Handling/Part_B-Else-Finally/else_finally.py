# else: Runs ONLY is the try block succeeded
try:
    # Try something risky
    score = int(input("Enter score: "))
except ValueError:
    # Runs if it FAILED
    print("Invalid Score!")
else:
    # Runs if it SUCCEEDED
    print(f"✅ Score recorded: {score}")
    
def parse_command(message):
    """Parse a Discord command like: !ban PlayerName 7days"""
    try:
        parts = message.split()
        command = parts[0]
        target = parts[1]
        duration = parts[2]
    except IndexError:
        print("❌ Invalid command format - missing parts!")
    else:
        print("✅ Command parsed successfully")
        if command.startswith("!"):
            (f"⚡️ Executing: {command}")
        return command, target, duration
    finally: # Runs no matter what
        print("This block runs regardless.")
print(parse_command("!ban PlayerName 7day"))
print(parse_command("!ban"))
        