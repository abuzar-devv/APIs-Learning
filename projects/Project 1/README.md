# GitHub Python Repo Lead Generator

A scenario-based project for a company selling a **developer tool for Python developers**.

### Scenario

The company wants to find potential customers among active Python projects on GitHub. Finding these repositories manually would take time, so this project automates the initial lead-generation process.

### Solution

The project uses the **GitHub Search API** to find relevant repositories and organizes them into prioritized lead lists based on their recent activity.

### Criteria

- Python repositories
- 500+ stars
- Not archived
- Activity within the last 90 days

### Lead Segments

- **Highest Priority** — activity within the last 30 days
- **2nd Priority** — activity within 31–90 days

### What I Practiced

- GitHub Search API
- API authentication
- Python `requests`
- Processing API responses
- Dates and timestamps
- Pandas and CSV files
- Basic lead segmentation
