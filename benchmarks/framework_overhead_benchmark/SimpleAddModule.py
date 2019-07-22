from __future__ import absolute_import, division, print_function, unicode_literals
import torch
from utils import NUM_PT_LOOP_ITERS

def add_tensors_loop(x, y):
    z = torch.add(x, y)
    for i in range(NUM_PT_LOOP_ITERS):
        z = torch.add(z, x)
    return z

class SimpleAddModule(torch.nn.Module):
    def __init__(self, add_op):
        super(SimpleAddModule, self).__init__()
        self.add_op = add_op

    def forward(self, x, y):
        return self.add_op(x, y)
