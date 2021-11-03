from github import Github
from access_token import token

g = Github(token)
org = g.get_organization("Devs-Clan")

class github_actions:

    def getMembers(self):
        members = list()
        for member in org.get_members():
            members.append(member)
        return members    

    def getMemberInfo(self, memberName):
        memberInfo = {}
        for member in org.get_members():
            if(member.name == memberName):
                memberInfo['user'] = member.name
                memberInfo['avatarurl'] = member.avatar_url
                memberInfo['bio'] = member.bio
                memberInfo['email'] = member.email
        return memberInfo     

    def getRepos(self):
        repos = list()
        for repo in org.get_repos():
            repos.append(repo)
        return repos    
                   