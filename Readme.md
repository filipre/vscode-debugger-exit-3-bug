# Readme

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Make sure the right virtual env is selected in VS Code (default path)
# Start ▶ Service in VS Code
# Change one line in main.py and observe system exit 3
```

## Trouble Shooting

- Restarting the service itself does not solve the issue ❌
- Restarting VS Code does not solve the issue ❌
- Restarting the computer does not solve the issue ❌
- Disabeling "Uncaught Exceptions" and enabling "User Uncaught Exceptions" works ✅

## Service

```
$ curl http://127.0.0.1:8082
OK%
```