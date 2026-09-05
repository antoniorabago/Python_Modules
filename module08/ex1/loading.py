#!/usr/bin/env python3

from importlib.metadata import PackageNotFoundError, version
import sys


def comparison() -> bool:
    dependencies = ["pandas", "numpy", "matplotlib"]
    all_dependencies = True
    for dependency in dependencies:
        try:
            dependency_version = version(dependency)
            print(f"[OK] {dependency} ({dependency_version}) - ", end="")
            if dependency == "pandas":
                print("Data manipulation ready")
            elif dependency == "numpy":
                print("Numerical computation ready")
            elif dependency == "matplotlib":
                print("Visualization ready")
        except PackageNotFoundError:
            print(f"[ERROR] {dependency} - Not installed")
            all_dependencies = False
    return all_dependencies


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    if not comparison():
        print("\nInstall dependencies with pip:")
        print("pip install -r requirements.txt\n")
        print("Or with Poetry:")
        print("poetry install")
        sys.exit(1)

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    data = np.random.normal(0, 1, 1000)
    print("Processing 1000 data points...")
    df = pd.DataFrame({"matrix_value": data})
    print("Generating visualization...")
    plt.hist(df["matrix_value"])
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
