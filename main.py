import argparse

import numpy as np
import torch.optim as optim

import baseline
import data_generator

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str, default='../data/eclipse')
parser.add_argument('--n_words', type=int, default=50000)
parser.add_argument('--n_chars', type=int, default=100)
parser.add_argument('--word_dim', type=int, default=128)
parser.add_argument('--char_dim', type=int, default=64)
parser.add_argument('--n_filters', type=int, default=128)
parser.add_argument('--n_prop', type=int, default=50)
parser.add_argument('--epochs', type=int, default=10)
parser.add_argument('--batch_size', type=int, default=64)
parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
                    help='learning rate (default: 0.01)')
args = parser.parse_args()


def train(epoch, net, optimizer):
  print('Epoch: {}'.format(epoch))
  net.train()
  for loop, (batch_x, batch_y) in data_generator.batch_iterator(args.data, args.batch_size):
    # optimizer.zero_grad()
    # preds = net(batch_x)
    # print(preds)
    # loss = F.cross_entropy(preds, batch_y)
    # loss.backward()
    # optimizer.step()
    loop.set_postfix(loss=np.random.rand())



def test(net):
  pass


def main():
  net = baseline.BaseNet(args)
  net.cuda()
  optimizer = optim.Adam(net.parameters(), lr=args.lr)
  for epoch in range(1, args.epochs + 1):
    train(epoch, net, optimizer)
    test(net)


if __name__ == "__main__":
  main()