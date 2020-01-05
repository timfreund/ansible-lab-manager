from setuptools import setup

setup(name='ansible-lab-manager',
      version='0.1',
      description='Ansible Lab Manager',
      url='https://github.com/timfreund/ansible-lab-manager',
      author='Tim Freund',
      author_email='tim@freunds.net',
      install_requires=[
          'ansible',
          'click',
          'jinja2',
      ],
      license='MIT',
      packages=['alm'],
      entry_points = {
          'console_scripts': [
              'ansible-lab-manager=alm.cli:ansible_lab_manager',
          ],
      },
      zip_safe=False)
