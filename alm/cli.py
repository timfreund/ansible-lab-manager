import click

from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from jinja2 import Environment, PackageLoader

@click.command()
@click.option('--inventory', default="./hosts", prompt='Ansible inventory file')
def ansible_lab_manager(inventory):
    ansible_loader = DataLoader()
    inventory = InventoryManager(loader=ansible_loader, sources=inventory)
    
    jinjaenv = Environment(loader=PackageLoader('alm', 'templates'))
    compose_template = jinjaenv.get_template('docker-compose.yml.j2')
    compose_rendered = compose_template.render(dict(inventory=inventory))
    print(compose_rendered)
    # for h in inventory.hosts:
    #     print(h)


