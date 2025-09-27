import click


@click.command()
@click.option("--text", help="输入文字")
def ajianbest6(text):
    """装饰器传递参数"""
    if text:
        print(text)
    else:
        print("hello world")


if __name__ == "__main__":
    ajianbest6()
