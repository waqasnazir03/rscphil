import click
import rscphil.lib.openstack as osc

@click.command(name="test")
def test():
    click.echo("This is test")

@click.option("--target-project", "-t", required=True, help="Target project id. Source rc file before running this command")
@click.option("--instance_id", "-v", required=True, help="Instance id of instance to be migrated")
@click.command(name="interproject-instance-migrate")
def interproject_instance_migrate(target_project, instance_id):
    """ Migrates openstack instance from one project to another"""
    osc.migrate_instance_inter_project(target_project, instance_id)

def get_openstack_group():
    """ Return the OpenStack click group """

    @click.group(name="openstack")
    def openstack_group():
        """ Deploy and manage OpenStack """

    openstack_group.add_command(test)
    openstack_group.add_command(interproject_instance_migrate)
    return openstack_group
