import os
import yaml

# # TODO pkg_resources isn't in 18.04's default python
# # auditioning pkg_resources from setuptools
# try:
#     import importlib.resources as pkg_resources
# except ImportError:
#     # Try backported to PY<37 `importlib_resources`.
#     import importlib_resources as pkg_resources
import pkg_resources

def load_config_file(file_path):
    c = {}
    try:
        with open(file_path, "r") as config_file:
            c = yaml.full_load(config_file)
    except Exception as e:
        pass
    return c

def load_config_text(config_text):
    return yaml.full_load(config_text)

def load_environment_variables():
    c = {}
    for k, v in os.environ.items():
        if k.startswith('ALM_'):
            ck = k.replace('ALM_', '').lower()
            c[ck] = v
    return c

def merge_configs(priority1, priority2):
    c = {}
    c.update(priority2)
    c.update(priority1)
    return c

def autoload_configuration():
    defaults = load_config_text(pkg_resources.resource_string('alm', 'defaults.yml').decode('utf-8'))
    cwd = load_config_file(os.path.sep.join([os.getcwd(), ".ansible-lab-manager.yml"]))
    home = load_config_file(os.path.sep.join([os.path.expanduser("~"), ".ansible-lab-manager.yml"]))
    env = load_environment_variables()

    # TODO that's pretty ugly, perhaps merge_configs should take an arbitrary
    # number of configuration dictionaries
    c = merge_configs(home, defaults)
    c = merge_configs(cwd, c)
    c = merge_configs(env, c)

    return c
