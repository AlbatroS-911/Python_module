import sys
import os
try:
    from dotenv import load_dotenv  # type: ignore
except ImportError as error:
    print(error)
    sys.exit(1)


def checking_configuration(mode: str | None, db_url: str | None,
                           api: str | None, log: str | None,
                           zion_endpt: str | None) -> None:
    print("Configuration loaded:")
    if mode not in ['development', 'production']:
        print("Mode: error matrix mode: development or production")
    else:
        print(f"Mode: {mode}")
    if db_url:
        print("Database: Connected to local instance")
    else:
        print("Database: Missing database configuration")
    if api:
        print("API Access: Authenticated")
    else:
        print("API Access: Failed to authenticate")
    if log:
        print(f"Log level: {log}")
    else:
        print("Log level: Unknown log")
    if zion_endpt:
        print("Zion network: online")
    else:
        print("Zion network: disconnected")


def checking_security(db_url: str | None, api: str | None,
                      missing_keys: list[str], override: bool) -> None:
    print("Environment security check:")
    if not db_url or not api:
        print("[KO] Secrets are possibly hardcoded")
    else:
        print("[OK] No hardcoded secrets detected")
    if missing_keys:
        print(f"[KO] Missing key in your environment: {missing_keys}")
    else:
        print("[OK] .env file properly configured")
    if not override:
        print("[OK] Default values loaded")
    else:
        print("[OK] Production overrides available")


def oracle() -> None:
    if sys.base_prefix != sys.prefix:
        print()
        print("ORACLE STATUS: Reading the Matrix...")
        print()
        required_keys = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL",
                         "ZION_ENDPOINT"]
        override = any(key in os.environ for key in required_keys)
        load_dotenv(".env", override=False)
        missing_keys: list[str] = []
        for key in required_keys:
            if key not in os.environ:
                missing_keys += [key]
        matrix_mode = os.getenv(required_keys[0])
        database_url = os.getenv(required_keys[1])
        api_key = os.getenv(required_keys[2])
        log_level = os.getenv(required_keys[3])
        zion_endpoint = os.getenv(required_keys[4])
        if not os.path.exists(".env"):
            print("No configuration file detected")
        else:
            checking_configuration(matrix_mode, database_url, api_key,
                                   log_level, zion_endpoint)
            print()
            checking_security(database_url, api_key, missing_keys, override)

            print()
            print("The Oracle sees all configurations.")
    else:
        print()
        print("ORACLE STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("Create and activate venv, run:")
        print("python -m venv oracle_venv "
              "\nsource oracle_venv/bin/activate # On Unix"
              "\noracle_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    oracle()
