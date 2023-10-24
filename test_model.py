from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

import fasttext
from fasttext import train_supervised


model = fasttext.load_model('product_description2.bin')


r = model.test('product_description.valid')
print(r)