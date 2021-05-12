# -*- coding: utf-8 -*-
#!/usr/bin/env python2
# Before Copy This Tool look Yourself properly 
# Good Bye Bro 
import os
os.system('clear')
import sys, json, time , requests
bannar='''\033[91m
 ██████  ██████  ██    ██ ███    ██ ████████ ███████ ██████  
██      ██    ██ ██    ██ ████   ██    ██    ██      ██   ██ 
██      ██    ██ ██    ██ ██ ██  ██    ██    █████   ██████  
██      ██    ██ ██    ██ ██  ██ ██    ██    ██      ██   ██ 
 ██████  ██████   ██████  ██   ████    ██    ███████ ██   ██ 
                                                             
                             
                                    \033[93m  Version : 1.0     
         
         
          \033[0m       \033[0;37;41m Github Star Counter\033[0m                            
                                    
'''
bannar2='''\033[94m--------------------------------------------------------'''
bannar3= '''\033[94m--------------------------------------------------------'''
print bannar
print bannar2
print ''
print ' \033[96m Author   : \033[95m Dark Hunter 141'
print ''
print ' \033[96m Tool     : \033[95m Github Start Counter'
print ''
print ' \033[96m Facebook : \033[95m https://www.facebook.com/darkhunter141/'
print ''
print ' \033[96m Github   : \033[95m https://www.github.com/darkhunter141/'
print ''
print ' \033[96m Coded By : \033[95m Dark Wolf , DarkXploit'
print ''
print bannar3
print ''
print ''
github_id = raw_input('\033[91m[\033[0m✓\033[91m] \033[93mYour Github Username(ex:darkhunter141) : \033[92m')
print ''
print ''
def bal(b):
 for biva in b + '\n':
   sys.stdout.write(biva)
   sys.stdout.flush()
   time.sleep(0.02)
bal ('\033[91m[\033[0m✓\033[91m] \033[93mFinding. Please wait.......')
print ''
print ''
url = 'https://api.github.com/users/{github_id}/repos?page={page_id}'
repo_list = []
page_id = 1
while True:
    r = requests.get(url.format(github_id=github_id, page_id=page_id))
    if r.status_code != 200:
        print('\033[91mCheck your network connections')
        exit()

    repo_array = json.loads(r.content.decode('utf-8'))
    if len(repo_array) == 0:
        break

    for repo in repo_array:
        if not repo['fork']:
            repo_list.append([repo['name'], repo['stargazers_count'], repo['forks_count']])
    page_id += 1

# sort by number of stars
repo_list = sorted(repo_list, key=lambda x: x[1], reverse=True)

print('\033[96m=' * 55)
print '\033[0m'
print('\n'.join(['{: <30}★{: <10}\tfork {} '.format(*repo) for repo in repo_list]))
print ''
print('\033[96m=' * 55)
print('{: <30}★{: <10}\tfork {} '.format('\033[91m[\033[0m✓\033[91m] \033[93m Total ', sum([i[1] for i in repo_list]), sum([i[2] for i in repo_list])))
print ''

print '[√] \033[93m Good Bye ಠ‿ಠ'
