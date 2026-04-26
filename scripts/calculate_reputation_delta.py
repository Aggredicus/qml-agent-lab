"""
Calculate suggested reputation delta based on reviewer score and outcome.

This script does NOT modify any repository state.
It prints a recommendation for human or agent reviewers.
"""

def calculate_delta(score, accepted):
    if score <= 3:
        return 0 if accepted else -2
    elif score <= 6:
        return 1 if accepted else -1
    elif score <= 8:
        return 2 if accepted else 0
    else:
        return 3 if accepted else 0


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--score", type=int, required=True)
    parser.add_argument("--accepted", action="store_true")
    parser.add_argument("--rejected", action="store_true")

    args = parser.parse_args()

    accepted = args.accepted and not args.rejected

    delta = calculate_delta(args.score, accepted)

    print("Suggested Reputation Delta:", delta)
