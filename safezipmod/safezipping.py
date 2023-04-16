import click, os 
import zipfile
import re
def regex_validation(_, param, value: str) -> str:
    try:
        re.compile(value)
    except:
        raise click.BadParameter("regex is invalid")
    return value
@click.group()
def zippinggroup(): ...
@zippinggroup.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False,  dir_okay=True, resolve_path=True))
@click.argument('newnamefile', type=click.Path(exists=False, file_okay=True, dir_okay=False, resolve_path=True))
@click.option('--skipsecure', required=False, is_flag=True, help="Skip unsecure files with credentials")
@click.option('--customregex', required=False, type=str, callback=regex_validation) 
def zip_folder(directory: str, newnamefile: str, skipsecure: bool, customregex: str=False)-> None:
    files = os.listdir(directory)
    if len(files) > 0:
        dangerous_files: set[str] = {r'\.env', r'^config'}
        if customregex: dangerous_files.add(customregex)
        marked_files: set[str] = set()
        safe_files: set[str] = {x for x in files}
        if not skipsecure:
            safe_files = set()
            for file in files:
                if len(tuple(filter(lambda regex: re.match(regex, file), dangerous_files))) != 0:
                    marked_files.add(file)
                else:
                    safe_files.add(file)
        if newnamefile in safe_files:
            os.remove(newnamefile)
        if len(safe_files) == 0:
            click.echo(click.style("Warning: zipfile will contain nothing", fg="yellow", bold=True))
        with zipfile.ZipFile(newnamefile, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
            os.chdir(directory)
            for file in safe_files: zipf.write(file)
        click.echo(f'Successfully created zip {newnamefile}')
        if len(marked_files) != 0:
            click.echo('The following files has not been comprimised because they are dangerous(run --skipsecure to ignore):')
            for index, file in enumerate(marked_files):
                if index != (len(marked_files) - 1):
                    click.echo(click.style(f'├──{file}', fg="red"))
                else:
                    click.echo(click.style(f'└──{file}', fg="red"))
        if len(safe_files) != 0:
            click.echo('The following files has been compromised in the zip folder:')
            for index, file in enumerate(safe_files):
                if index != (len(safe_files) - 1):
                    click.echo(click.style(f'├──{file}', fg="green"))
                else:
                    click.echo(click.style(f'└──{file}', fg="green"))
    else:
        click.echo('Directory cannot be empty', err=True)
if __name__ == '__main__':
    zippinggroup()
    
