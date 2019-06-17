import click
import re
from mlcomp.contrib.scripts.split import file_group_kfold
import os
import pandas as pd

current_folder = os.path.dirname(__file__)


@click.group()
def main():
    pass


@main.command()
@click.argument('img_path')
@click.argument('mask_path')
@click.argument('n_splits', type=int)
@click.option('--group-regex')
def split_segment(img_path: str, mask_path: str, n_splits: int, group_regex: str = None):
    output = os.path.join(current_folder, 'fold.csv')
    get_group = None
    if group_regex:
        pattern = re.compile(group_regex)
        get_group = lambda x: pattern.match(x).group(1)

    file_group_kfold(n_splits, output, get_group=get_group,
                     image=os.listdir(img_path),
                     mask=os.listdir(mask_path)
                     )


@main.command()
@click.argument('img_path')
def split_test_img(img_path: str):
    output = os.path.join(current_folder, 'fold_test.csv')
    df = pd.DataFrame({'image': sorted(list(os.listdir(img_path))), 'fold': 0})
    df.to_csv(output, index=False)


if __name__ == '__main__':
    main()
