#!/usr/bin/env python3
import time
from collections import Counter
import random

# Historical multiplier data placeholder
historical_multipliers = [round(random.uniform(1.0, 5.0), 2) for _ in range(100)]

def round_multipliers(data, decimals=1):
    """Round multipliers to a specific decimal place for frequency analysis."""
    return [round(m, decimals) for m in data]

def analyze_multipliers(data):
    """Count frequency of rounded multipliers and return most common ones."""
    rounded_data = round_multipliers(data)
    counter = Counter(rounded_data)
    most_common = counter.most_common(5)  # Get top 5 frequent multipliers
    return most_common

def generate_signal(most_common):
    """
    Generate betting signal based on frequency of multipliers.
    This does NOT predict exact outcome but suggests possible bets.
    """
    for multiplier, freq in most_common:
        if multiplier >= 2.0 and freq >= 3:
            return f"Signal: Bet now! Likely multiplier: {multiplier}x appeared {freq} times."
    return "Signal: Hold off betting, no strong pattern detected."

def main():
    print("Starting Aviator signal generator in Termux...")
    while True:
        # Ideally pull live multipliers here, for demo adding random multiplier
        new_multiplier = round(random.uniform(1.0, 5.0), 2)
        historical_multipliers.append(new_multiplier)
        if len(historical_multipliers) > 200:
            historical_multipliers.pop(0)  # Keep data size manageable

        common_multipliers = analyze_multipliers(historical_multipliers)
        print("Top multipliers and their frequencies:")
        for mul, freq in common_multipliers:
            print(f"{mul}x - {freq} times")

        signal = generate_signal(common_multipliers)
        print(signal)
        print("-" * 50)

        time.sleep(60)  # Run update every 60 seconds

if __name__ == "__main__":
    main()