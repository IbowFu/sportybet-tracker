import datetime
import csv
import os

def main():
    today = datetime.date.today().isoformat()
    filename = f"correct_scores_{today}.csv"
    filepath = os.path.join(os.getcwd(), filename)

    # بيانات وهمية كمثال
    data = [
        ["Match", "Correct Score", "Odds"],
        ["Team A vs Team B", "1-0", "6.5"],
        ["Team C vs Team D", "2-2", "12.0"]
    ]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print(f"Data saved to {filename}")

if __name__ == "__main__":
    main()
