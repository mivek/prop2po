import click


@click.command()
@click.argument('source', type=click.File('rt'))
@click.argument('destination', type=click.File('wt'))
@click.option('-l', '--language', type=click.STRING, help='The translation language')
@click.option('-p', '--project', type=click.STRING, help='The name of the project')
@click.option('-e', '--encoding', type=click.STRING, help='The encoding wanted')
def to_po(source, destination, encoding, language, project):
    """Converts a property file to a Gettext PO file.

    SOURCE is the path of the property file to convert.

    DESTINATION is the path of the Gettext PO file to create
    """

    header = """msgid ""
msgstr ""
"MIME-Version: 1.0"
"Content-Type: text/plain; charset={encoding}"
"Content-Transfer-Encoding: 8bit"
"X-Generator: prop2po"
"Project-Id-Version: {project}"
"Language: {language}"\n"""
    lines = source.readlines()
    destination.write(header.format(
        language=language,
        project=project,
        encoding=encoding
    ))
    for line in lines:
        if not line.isspace():
            parts = line.split('=')
            destination.write('#:\n' + 'msgid "' + parts[0] + '"\n' + 'msgstr "' + parts[1][:-1] + '"\n\n')
