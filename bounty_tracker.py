# bounty_tracker.py

class BountyTracker:
    def __init__(self):
        self.claims = {}

    def star_repo(self, user):
        if user not in self.claims:
            self.claims[user] = {'starred': True, 'rtc': 2}
            return "Claim successful: 2 RTC added to your wallet."
        return "Claim already made."

    def follow_repo(self, user):
        if user not in self.claims:
            self.claims[user] = {'followed': True, 'rtc': 2}
            return "Claim successful: 2 RTC added to your wallet."
        return "Claim already made."