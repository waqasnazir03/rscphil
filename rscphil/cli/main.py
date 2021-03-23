import click
import rscphil.cli.openstack as openstack


def get_entrypoint():
    """ Return the entrypoint click group """

    @click.group()
    def entrypoint():
        """ rscphil cli"""

    entrypoint.add_command(openstack.get_openstack_group())
    return entrypoint

def main():
    """ Entrypoint defined in setup.py"""
    try:
        entrypoint = get_entrypoint()
        entrypoint()
    except KeyboardInterrupt:
        error("CTRL+C detected, exiting", exit=True, code=2)
