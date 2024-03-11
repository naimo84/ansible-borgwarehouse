# Ansible Collection - rarrais.borgwarehouse

Ansible Collection for managing [BorgWarehouse](https://github.com/Ravinou/borgwarehouse).

## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.14.2**.

## Installing this collection

You can install the Cisco BorgWarehouse collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install rarrais.borgwarehouse

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: rarrais.borgwarehouse
```

## Using this collection

```yaml
---
- name: Configure repository in BorgWarehouse.
  rarrais.borgwarehouse.repository:
    url: http://borgwarehouse.lan:3000
    api_token: yet-another-secret
    alias: ansibletest
    ssh_public_key: "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIK0wmN/Cr3JXqmLW7u+g9pTh+wyqDHpSQEIQczXkVx9q ansibletest"
```

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
