import instaloader
import re

# Function to extract email and phone numbers using regex
def extract_contact_info(bio):
    # Regex for basic email and phone numbers
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
    phone_pattern = r"\+?[0-9]{1,4}?[-.\s]?(?:\(?\d{1,3}?\)?[-.\s]?)?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}"

    # Searching for email and phone numbers in the bio
    email = re.findall(email_pattern, bio)
    phone = re.findall(phone_pattern, bio)

    return email, phone

# Initialize Instaloader
L = instaloader.Instaloader()

# Login if necessary (not required for public profiles)
# L.login('your_username', 'your_password')

# Define the target Instagram profile
profile = instaloader.Profile.from_username(L.context, "azzip.tech")

# Scraping followers' info (email and phone)
for follower in profile.get_followers():
    print(f"Follower: {follower.username}")
    print(f"Bio: {follower.biography}")
    
    # Extract email and phone from bio
    emails, phones = extract_contact_info(follower.biography)
    
    if emails:
        print(f"Email(s): {', '.join(emails)}")
    if phones:
        print(f"Phone(s): {', '.join(phones)}")
    
    print(f"Profile URL: https://www.instagram.com/{follower.username}/")
    print("-" * 50)
