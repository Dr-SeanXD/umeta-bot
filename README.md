# UMETA Discord Bot

A feature-rich and modular Discord bot designed for community collaboration, system testing, and dynamic engagement in the UMETA environment. Built with scalability and customization in mind, this bot supports a variety of admin tools, interactive buttons, and permission-based commands.

## 🌟 Features

- 🎯 Role-based command restrictions (team, mod, official, boss)
- 🧾 UCoin query system (Chinese & English buttons)
- 🍕 Interactive pizza voting system with CSV tracking
- 💰 Official Points management with in-server logging
- 🔗 Invite link access control with time limits
- 🔍 On-demand UCoin and point queries with persistent data tracking

## 📦 Tech Stack

- Python 3
- `discord.py` with app commands
- `pandas` for CSV manipulation
- `apscheduler` for background tasks

## 🛡️ Permissions & Checks

Commands are validated based on the user's role (`mod`, `official`, `team`, `boss`) to ensure proper access control. Invite links are monitored and revoked if misused.

## 📂 File Structure

- `main.py`: Main bot logic and command definitions
- `Officials data.csv`: Tracks official points
- `UCoin Query.csv`: Tracks UCoin balances
- `Pizza Day.csv`: Tracks voting results
- `Loop Message.csv`: Used for dynamic button message tracking

## 🛠️ Setup

1. Clone this repository.
2. Set your bot token and password in `main.py`.
3. Run the bot using:

```bash
python main.py
```

## ✨ Credits

Developed and maintained by contributors of the UMETA project.  
Originally initiated for internal use, now evolving toward open collaboration.

---

**No secrets. No silence. Just code and contribution.**
# umeta-bot
