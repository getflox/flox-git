import click
from git import Git
from flox_git.wrapper import Git as Wrapper


@click.group()
@click.pass_obj
def git(flox):
    """Git tools for flox"""
    flox.git = Wrapper(Git(flox.working_dir), flox.container.issue_tracker)


@git.command()
@click.pass_obj
@click.argument('source', default="origin/develop")
@click.argument('destination', default="origin/release")
def changelog(flox, source, destination):
    messages = flox.git.log(source, destination)
    for message in messages:
        click.echo(message)


@git.command()
def tag():
    pass


@git.command()
def tags():
    pass
