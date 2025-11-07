import os
import sys

# Read the HTML file
with open('index.html', 'r') as f:
    content = f.read()

# Replace the tokens
content = content.replace("const GITHUB_TOKEN = '';", f"const GITHUB_TOKEN = '{os.environ['GIST_TOKEN']}';")
content = content.replace("const ADMIN_PASSWORD = 'your-secure-password';", f"const ADMIN_PASSWORD = '{os.environ['ADMIN_PASS']}';")
content = content.replace("const DISCORD_WEBHOOK = '';", f"const DISCORD_WEBHOOK = '{os.environ['WEBHOOK_URL']}';")

# Write back
with open('index.html', 'w') as f:
    f.write(content)

print("✅ Secrets injected successfully!")
