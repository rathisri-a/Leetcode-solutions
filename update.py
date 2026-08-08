import requests
from pathlib import Path

USERNAME = "rathisri_a"

query = """
query getUserProfile($username: String!) {
  matchedUser(username: $username) {
    username
    submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
"""

response = requests.post(
    "https://leetcode.com/graphql",
    json={
        "query": query,
        "variables": {"username": USERNAME}
    },
    headers={
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/u/{USERNAME}/",
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30,
)

data = response.json()

if (
    "data" not in data
    or data["data"] is None
    or data["data"]["matchedUser"] is None
):
    raise Exception(f"LeetCode user '{USERNAME}' not found.\nResponse: {data}")

stats = data["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]

easy = medium = hard = total = 0

for item in stats:
    if item["difficulty"] == "Easy":
        easy = item["count"]
    elif item["difficulty"] == "Medium":
        medium = item["count"]
    elif item["difficulty"] == "Hard":
        hard = item["count"]
    elif item["difficulty"] == "All":
        total = item["count"]

heatmap = f"https://leetcard.jacoblin.cool/{USERNAME}?theme=dark&ext=heatmap"

content = f"""
## 📊 LeetCode Statistics

| Difficulty | Solved |
|-----------|-------:|
| Easy | {easy} |
| Medium | {medium} |
| Hard | {hard} |
| **Total** | **{total}** |

## 📅 Submission Heatmap

![LeetCode Heatmap]({heatmap})
"""

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")

marker = "<!--STATS-->"

if marker in text:
    start = text.index(marker)
    text = text[:start] + marker + "\n\n" + content
else:
    text += "\n\n<!--STATS-->\n\n" + content

readme.write_text(text, encoding="utf-8")
