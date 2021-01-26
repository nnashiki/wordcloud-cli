import click
from wordcloudja.wordcloud_app import text_to_img


@click.command()
@click.option('--target', prompt='target text file path', help='target text file path')
@click.option('--out', prompt='out file path', help='out file path')
def cli(target, out):
    with open(target, 'r') as f:
        text_to_img(f.read(), out)


if __name__ == "__main__":
    cli()
