# Copyright 2019 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Tools for building neural networks."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_probability.python.experimental.nn import initializers
from tensorflow_probability.python.experimental.nn import util
from tensorflow_probability.python.experimental.nn.affine_layers import Affine
from tensorflow_probability.python.experimental.nn.affine_layers import AffineVariationalFlipout
from tensorflow_probability.python.experimental.nn.affine_layers import AffineVariationalReparameterization
from tensorflow_probability.python.experimental.nn.affine_layers import AffineVariationalReparameterizationLocal
from tensorflow_probability.python.experimental.nn.convolutional_layers import Convolution
from tensorflow_probability.python.experimental.nn.convolutional_layers import ConvolutionVariationalFlipout
from tensorflow_probability.python.experimental.nn.convolutional_layers import ConvolutionVariationalReparameterization
from tensorflow_probability.python.experimental.nn.convolutional_transpose_layers import ConvolutionTranspose
from tensorflow_probability.python.experimental.nn.convolutional_transpose_layers import ConvolutionTransposeVariationalFlipout
from tensorflow_probability.python.experimental.nn.convolutional_transpose_layers import ConvolutionTransposeVariationalReparameterization
from tensorflow_probability.python.experimental.nn.layers import Lambda
from tensorflow_probability.python.experimental.nn.layers import Layer
from tensorflow_probability.python.experimental.nn.layers import Sequential
from tensorflow_probability.python.experimental.nn.variational_base import VariationalLayer
from tensorflow_probability.python.internal import all_util


_allowed_symbols = [
    'Affine',
    'AffineVariationalFlipout',
    'AffineVariationalReparameterization',
    'AffineVariationalReparameterizationLocal',
    'Convolution',
    'ConvolutionTranspose',
    'ConvolutionTransposeVariationalFlipout',
    'ConvolutionTransposeVariationalReparameterization',
    'ConvolutionVariationalFlipout',
    'ConvolutionVariationalReparameterization',
    'Lambda',
    'Layer',
    'Sequential',
    'VariationalLayer',
    'initializers',
    'util',
]


all_util.remove_undocumented(__name__, _allowed_symbols)
