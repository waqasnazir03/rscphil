import click

def migrate_instance_inter_project(target_project, instance_id):
    """ Lib method to migrate VM from one openstack project to another"""
    click.echo("Instance: {} Project: {}".format(instance_id, target_project))
