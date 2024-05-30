import pkg_resources
import sys

installed_packages = [pkg.key for pkg in pkg_resources.working_set]

for package in installed_packages:
    print(package)

print("Python version", sys.version)