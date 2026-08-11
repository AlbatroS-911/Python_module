import sys
from importlib import import_module
from importlib.metadata import version


def visualialize() -> None:
    req = import_module('requests')
    plt = import_module('matplotlib.pyplot')
    response = req.get(
        "https://covid-api.com/api/reports/total?date=2020-04-07")
    if response.status_code == 200:
        data = response.json()
        metrics = data['data']
        category = ['Confirmed', 'Active', 'Recovered', 'Deaths']
        values = [metrics['confirmed'], metrics['active'],
                  metrics['recovered'], metrics['deaths']]
        colors = ['#3498db', '#f1c40f', '#2ecc71', '#e74c3c']
        plt.figure(figsize=(9, 6))
        plt.bar(category, values, color=colors,
                edgecolor='black', width=0.6)
        plt.yscale('log')
        plt.ylabel('Number of cases', fontsize=12)
        plt.xlabel('Categories', fontsize=12)
        plt.title("Covid Statistics")
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        saving_file: str = "matrix_analysis.png"
        plt.savefig(saving_file, dpi=300)
        print(f"Results saved to: {saving_file}")
    else:
        print(f"Failed to retrieve data: {response.status_code} Error")


def matrix_venv() -> None:
    if sys.base_prefix != sys.prefix:
        REQUIRED_PACKAGES: list[str] = [
            "pandas", "numpy", "requests", "matplotlib"]
        INFO: list[str] = ["Data manipulation ready",
                           "Numerical computation ready",
                           "Network access ready",
                           "Visualization ready"]
        MISSING: list[str] = []
        for pack in REQUIRED_PACKAGES:
            try:
                import_module(pack)
            except ImportError:
                MISSING += [pack]
        if MISSING:
            print(
                "There are missing dependencies: ")
            for miss in MISSING:
                print(f"[MISSING] {miss}")
            print()
            print("Install using pip3: \n"
                  "pip3 install -r requirements.txt")
            print("Install Poetry: \n"
                  "poetry install")
        else:
            try:
                print()
                print("LOADING STATUS: Loading programs...")
                print()
                print("Checking dependencies:")
                i: int = 0
                for pack in REQUIRED_PACKAGES:
                    lib = import_module(pack)
                    print(
                        f"[OK] {(lib.__name__)} ({version(pack)}) - {INFO[i]}")
                    i += 1
                print()
                print("Analyzing Matrix data...")
                print("Processing Covid data points...")
                print("Generating visualization...")
                print()
                visualialize()
                print("Analysis complete!")
            except KeyboardInterrupt:
                print("Program interrupted: Visualisation aborted!")
    else:
        print()
        print("LOADING STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("Create and activate venv, run:")
        print("python -m venv loading_venv "
              "\nsource loading_venv/bin/activate # On Unix"
              "\nloading_venv\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    matrix_venv()
