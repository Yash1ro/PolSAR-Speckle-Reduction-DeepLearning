from torch.utils.tensorboard import SummaryWriter
import datetime
import os


class Tensorboard:
    def __init__(self):
        # in order to prevent the situation the chart being influenced because of changes
        # so creating a new dir is a better way
        self.nowtime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.root_path = "../logs"

    def create_board(self):
        writer = SummaryWriter(os.path.join(self.root_path, self.nowtime))
        return writer
