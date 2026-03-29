# Automated-Social-Media-Post-Scheduler
Automated Social Media Scheduler using Python and APIs
🔐 Environment Setup

This project uses environment variables to securely store API credentials.

📁 Step 1: Create a .env file

Create a file named .env in the root directory of the project.

✏️ Step 2: Add your API keys

Copy the contents from .env.example and replace with your actual credentials:

API_KEY=your_api_key
API_SECRET=your_api_secret
ACCESS_TOKEN=your_access_token
ACCESS_SECRET=your_access_token_secret
⚠️ Important Notes
Do NOT share your .env file publicly
.env is included in .gitignore to protect your secrets
Never upload your API keys to GitHub
🔑 Where to Get API Keys

You can generate API keys from the X (Twitter) Developer Console.

🚫 Without API Keys

If API access is not available, the project includes a simulation mode to demonstrate functionality without making real API calls.

This project follows secure practices by storing sensitive credentials using environment variables.
