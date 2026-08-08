import requests
from pathlib import Path

USERNAME = "rathisri-a"

query = """
query userProblemsSolved($username: String!) {
  matchedUser(username: $username) {
    submitStats {
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
    headers={"Content-Type": "application/json"}
)

data = response.json()

if (
    "data" not in data
    or data["data"] is None
    or data["data"]["matchedUser"] is None
):
    raise Exception(
        f"LeetCode user '{USERNAME}' not found. Check the USERNAME in update.py."
    )

stats = data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]

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

## 🧩 Skills Distribution

| Category | Problems |
|---------|---------:|
| Easy | {easy} |
| Medium | {medium} |
| Hard | {hard} |

## 📅 Submission Heatmap

![LeetCode Heatmap]({heatmap})
"""

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")

marker = "<!--STATS-->"

if marker in text:
    text = text.replace(marker, content)
else:
    text += "\n" + content

readme.write_text(text, encoding="utf-8")
