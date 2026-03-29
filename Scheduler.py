import tweepy
import os
from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# Load environment variables
load_dotenv()

def post_to_twitter():
    """Posts a fixed message to X/Twitter."""
    
    try:
        # Your message
        
        content = "Believe in yourself and keep moving forward 🚀"
        
        
        # Connect to Twitter API
        client = tweepy.Client(
            consumer_key=os.getenv("API_KEY"),
            consumer_secret=os.getenv("API_SECRET"),
            access_token=os.getenv("ACCESS_TOKEN"),
            access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
        )
        
        # Post tweet
        response = client.create_tweet(text=content)
        
        print(f"✅ Posted successfully at {datetime.now()} | Tweet ID: {response.data['id']}")

    except Exception as e:
        print("❌ Error:", e)


# --- Scheduler setup ---
scheduler = BlockingScheduler()

# 👉 CHANGE THIS TIME to future time
scheduler.add_job(
    post_to_twitter,
    trigger='date',
    run_date='2026-03-29 12:15:00' # put your confortable time zone.
)

# 👉 Optional: Run instantly for testing
# post_to_twitter()

print("⏳ Scheduler running... waiting for scheduled time...")
scheduler.start()
