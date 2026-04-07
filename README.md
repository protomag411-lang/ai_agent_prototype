# AI Agent Prototype

## 🛡️ Security Note & Video Submission
**Important:** The original demonstration video submitted for this project was recorded using a hardcoded API key for rapid prototyping. 

**Incident Response:**
* Following a **publicly issued security alert from GitHub**, that original key was immediately revoked and deactivated.
* This repository has been updated to use **Environment Variables (.env)** for all private credentials.
* The current code reflects the final, secure version of the prototype, which differs from the video for safety reasons.

## Setup
1. Clone the repo.
2. Create a `.env` file with your `GOOGLE_API_KEY`.
3. Run `uvicorn main:app`.
