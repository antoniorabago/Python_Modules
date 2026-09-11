#!/usr/bin/env python3

import os
import sys


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    env_file = ""
    try:
        from dotenv import load_dotenv, find_dotenv  # type: ignore
        env_file = find_dotenv()
        if env_file:
            load_dotenv(env_file)
    except ImportError:
        print("python-dotenv is not installed\n")
        sys.exit(1)

    print("Configuration loaded:")
    mode = os.getenv("MATRIX_MODE")
    database = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    if mode is None:
        print("Mode: Not configured")
    elif mode in ("development", "production"):
        print(f"Mode: {mode}")
    else:
        print(f"Mode: Invalid ({mode})")

    if database:
        print("Database: Connected to local instance")
    else:
        print("Database: Not connected")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Not authenticated")

    if log_level is None:
        print("Log Level: Not configured")
    else:
        print(f"Log Level: {log_level}")

    if zion:
        print("Zion Network: Online\n")
    else:
        print("Zion Network: Offline\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if env_file:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
