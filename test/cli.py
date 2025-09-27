import click


@click.command()
@click.option("--text", help="输入文字", default="hello world", show_default=True)
@click.option("--count", help="打印次数", type=int, default=1, show_default=True)
def ajianbest6(text, count):
    """装饰器传递参数"""

    for _ in range(count):
        print(text)


if __name__ == "__main__":
    ajianbest6()
