import sys
import pkg_resources

def check_python_setup():
    """Check Python setup and installed packages."""
    print("\n=== Python Environment Information ===")
    print(f"Python Version: {sys.version}")
    print(f"Python Location: {sys.executable}")
    
    print("\n=== Installed Packages ===")
    installed_packages = [f"{dist.key} ({dist.version})" 
                        for dist in pkg_resources.working_set]
    for package in sorted(installed_packages):
        print(package)

if __name__ == "__main__":
    check_python_setup()
