from os.path import join

from mlcomp.utils.config import Config
from mlcomp.worker.executors.base import *
from mlcomp.contrib.split import split_frame


@Executor.register
class Split(Executor):
    __syn__ = 'split'

    def __init__(self,
                 variant: str,
                 out: str,
                 n_splits: int = 5,
                 file: str = None,
                 label: str = None
                 ):
        self.variant = variant
        self.file = file
        self.n_splits = n_splits
        self.out = out
        self.label = label

    def work(self):
        if self.variant == 'frame':
            df = split_frame(self.file,
                             n_splits=self.n_splits,
                             label=self.label)
            df.to_csv(self.out, index=False)

    @classmethod
    def _from_config(cls,
                     executor: dict,
                     config: Config,
                     additional_info: dict):
        file = join(config.data_folder, executor.get('file'))
        return cls(
            variant=executor['variant'],
            out=join(config.data_folder, 'fold.csv'),
            file=file
        )


__all__ = ['Split']