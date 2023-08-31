from github import Github
import os
from github import Auth


def save_token(token):
    with open('token.txt', 'w') as f:
        f.write(token)


def get_repos(auth):
    g = Github(auth=auth)
    data = []
    name = []
    for repo in g.get_user().get_repos():
        data.append(repo.name)
        name.append(repo.full_name.split("/")[0])
    return data, name[0]


def select_repo(repos):
    print("Select a repository by entering its number:")
    for i, repo in enumerate(repos):
        print(f"{i+1}. {repo}")
    choice = int(input("Your choice: ")) - 1
    return repos[choice]


def clone_repo(repo, token, name):
    os.system(f'git clone https://{token}@github.com/{name}/{repo}.git')


def find_language(repo):
    languages = ['react', 'angular', 'vue', 'django',
                 'flask', 'fastapi', 'spring boot', 'dotnet']
    for language in languages:
        if language in open(f'{repo}/README.md').read():
            print(language)
            return language
    return None


def install_dependencies_andBuild(language, repo):
    if language == 'react':
        os.system(f'cd {repo} && npm install && npm run build')
    elif language == 'angular':
        os.system(f'cd {repo} && npm install && && ng build')
    elif language == 'vue':
        os.system(f'cd {repo} && npm install && npm run build')
    elif language == 'django':
        os.system(
            f'cd {repo} && pip install -r requirements.txt && python manage.py runserver ')
    elif language == 'flask':
        os.system(f'cd {repo} && pip install -r requirements.txt && falsk run')
    elif language == 'fastapi':
        os.system(
            f'cd {repo} && pip install -r requirements.txt && uvicorn main:app --reload')
    elif language == 'spring boot':
        os.system(f'cd {repo} && mvn install && mvn spring-boot:run ')
    elif language == 'dotnet':
        os.system(f'cd {repo} && dotnet restore && dotnet run')


def deploy(stage_ip):
    print(f"deployment completed {stage_ip}")
    # os.system(f'scp -r ./dist root@{stage_ip}:/var/www/html/')


def main():
    stage_ip = '127.0.0.1'
    token = "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"
    # token = input("Enter token : ")
    save_token(token)
    auth = Auth.Token(token)
    with open('token.txt', 'r') as f:
        token = f.read().strip()
    repos, name = get_repos(auth)
    repo = select_repo(repos)
    clone_repo(repo, token, name)
    language = find_language(repo)
    install_dependencies_andBuild(language, repo)
    deploy(stage_ip)


if __name__ == '__main__':
    main()
