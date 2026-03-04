import os
import requests
import subprocess

def get_all_repos(username, token=None):
    repos = []
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    headers = {"Accept": "application/vnd.github.v3+json"}
    auth = None

    if token:
        auth = (username, token)

    # Loop through all pages
    while url:
        response = requests.get(url, headers=headers, auth=auth)
        if response.status_code != 200:
            raise Exception(f"Error fetching repos: {response.status_code} {response.text}")

        repos.extend(response.json())

        # Link header for pagination
        links = response.links
        url = links.get('next', {}).get('url') if links else None

    return repos

def clone_repos(repos, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for repo in repos:
        clone_url = repo["clone_url"]
        name = repo["name"]
        dest = os.path.join(target_folder, name)

        if os.path.isdir(dest):
            print(f"Already exists: {name}")
            continue

        print(f"Cloning {name}...")
        subprocess.run(["git", "clone", clone_url, dest], check=True)

def main():
    username = input("GitHub username: ").strip()
    token = input("Personal Access Token (optional, press Enter to skip): ").strip() or None
    target_folder = input("Folder to clone into: ").strip()

    print("Fetching repository list ...")
    repos = get_all_repos(username, token)
    print(f"Found {len(repos)} repositories.")

    clone_repos(repos, target_folder)
    print("Done.")

if __name__ == "__main__":
    main()