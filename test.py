import json
import argparse

with open('package.json', 'r') as f:
    data = json.load(f)

print(data)

current_version = data['version']
major, minor, patch = data['version'].split(".")

parser = argparse.ArgumentParser(
    description="Script that adds 3 numbers from CMD"
)
# parser.add_argument('--feature', action=argparse.BooleanOptionalAction)

parser.add_argument("--server", "-s", required=True, type=str)

# parser.add_argument("--patch", "-p", required=True, type=bool)

args = parser.parse_args()

next_server_major = major
next_server_minor = minor
next_server_patch = patch

if args.server == "major":
    next_server_major = int(major) + 1
if args.server == "minor":
    print(minor)
    next_server_minor = int(minor) + 1
    print(next_server_minor)
if args.server == "patch":
    next_server_patch = int(patch) + 1


next_version = f"{next_server_major}.{next_server_minor}.{next_server_patch}"

print(f"Current Version: {current_version}")
print(f"Next Version: {next_version}")
