import click

from alm import autoload_configuration
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from jinja2 import Environment, PackageLoader

@click.command()
@click.option('--inventory', default="./hosts")
def ansible_lab_manager(inventory):
    config = autoload_configuration()
    template_context = config.copy()

    ansible_loader = DataLoader()
    template_context['inventory'] = InventoryManager(loader=ansible_loader, sources=inventory)
    
    jinjaenv = Environment(loader=PackageLoader('alm', 'templates'))
    compose_template = jinjaenv.get_template('docker-compose.yml.j2')
    compose_rendered = compose_template.render(template_context)
    print(compose_rendered)

