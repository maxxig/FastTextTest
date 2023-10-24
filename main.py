from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
from fasttext import train_supervised


def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))


if __name__ == "__main__":
    train_data = os.path.join(os.getenv("DATADIR", ''), 'product_description.train')
    valid_data = os.path.join(os.getenv("DATADIR", ''), 'product_description.valid')

    # train_supervised uses the same arguments and defaults as the fastText cli
    model = train_supervised(
        input=train_data, epoch=25, lr=1.0, wordNgrams=2, verbose=2, minCount=1
        #input=train_data, epoch=25, lr=1.0,  wordNgrams=2, bucket=200000, dim=100, loss='hs' #(1437216, 0.8748629294413645, 0.8748629294413645) product_description.bin
        # input=train_data, epoch=25, lr=1.0, wordNgrams = 2, bucket = 200000, dim = 150, loss = 'hs'  # (1437216, 0.8775904248213212, 0.8775904248213212)
        #input = train_data, epoch = 25, lr = 1.0, wordNgrams = 2, bucket = 200000, dim = 150#, loss = 'hs'
    )
    print_results(*model.test(valid_data))

    # model = train_supervised(
    #     input=train_data, epoch=25, lr=1.0, wordNgrams=2, verbose=2, minCount=1,
    #     loss="hs"
    # )
    # print_results(*model.test(valid_data))
    model.save_model("product_description3.bin")

    model.quantize(input=train_data, qnorm=True, retrain=True, cutoff=100000)
    print_results(*model.test(valid_data))
    model.save_model("product_description.ftz")