# Copyright: (c) 2024, Rafael Arrais
# GNU General Public License v3.0+

from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.urls import Request
import json

__metaclass__ = type

class BorgWarehouseClient:
    def __init__(self, url, api_token, alias, ssh_public_key, size, alert, comment):
        self.url = url
        self.alias = alias

        self.headers = {
            'Authorization': str('Bearer ' + api_token),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        self.data = {
            'alias': alias,
            'sshPublicKey': ssh_public_key,
            'size': str(size),
            'alert': alert,
            'comment': comment,
            'lanCommand': False
        }

        self.session = Request()
        self.repository = self.get_repository()

        if self.repository is not None:
            self.exists = True
            self.id = self.repository['id']
        else:
            self.exists = False

    def get_repository(self):
        get_api_url = self.url + "/api/repo"
        r = self.session.get(get_api_url , headers=self.headers)
        
        repositories = json.loads(r.read())['repoList']

        for repo in repositories:
            if repo['alias'] == self.alias:
                return repo

        return None

    def add_repository(self):     
        add_api_url = self.url + "/api/repo/add"

        self.session.post(add_api_url, data=json.dumps(self.data), headers=self.headers)
        return True

    def edit_repository(self):
        edit_api_url = self.url + "/api/repo/id/" + str(self.id) + "/edit"
        changed = False
        
        if self.repository['sshPublicKey'] != self.data['sshPublicKey']:
            changed = True
        if int(self.repository['storageSize']) != int(self.data['size']):
            changed = True
        if int(self.repository['alert']) != int(self.data['alert']):
            changed = True
        if self.repository['comment'] != self.data['comment']:
            changed = True

        if changed == True:
            self.session.put(edit_api_url, data=json.dumps(self.data), headers=self.headers)
        
        return changed

    def delete_repo(self):
        delete_api_url = self.url + "/api/repo/id/" + str(self.id) + "/delete"
        data = {'toDelete': True}

        self.session.delete(delete_api_url, data=json.dumps(data), headers=self.headers)
        return True
