import argparse
from datetime import date
import re
from pathlib import Path
# title can contain spaces, caps
def filename(title, today):
    title = title.lower()
    title = title.replace(" ", "-")
    title = title.replace(",", "")
    title = title.replace(":", "")
    title = title.strip()
    title = re.sub("-+", "-", title)
    title = ''.join(e for e in title if e.isalnum() or e == "-")
    filepath = f"_news/{today}-{title}.md"
    return filepath

def news_template(today):
    return f"""---
layout: post
date: {today}
inline: true
---

<add text here>
"""

# example usage: python3 news.py "Quarterly Earnings Reach All-Time High"

def main():
    parser = argparse.ArgumentParser(description='Create news template from news title')
    parser.add_argument('title', type=str,
                        help='News title')
    parser.add_argument('--date', required=False)
    args = parser.parse_args()

    today = args.date
    if today is None:
        today = date.today()

    filepath = filename(args.title, today)
    filepath = Path(filepath)

    if filepath.exists():
        print("News file already exists at", filepath.resolve())
        return
    
    with open(filepath, "w") as f:
        print("News file created at", filepath)
        f.write(news_template(today))

if __name__ == "__main__":
    main()