# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#


import numpy as np
import utils
import params

src_id2word, src_word2id, src_embeddings = utils.read_txt_embeddings('data/wiki.%s.vec' % params.src_lang, params.n_init_ex, False) # = 5000, only read en 500 words
np.save('data/%s_%d' % (params.src_lang, params.n_init_ex), src_embeddings)
tgt_id2word, tgt_word2id, tgt_embeddings = utils.read_txt_embeddings('data/wiki.%s.vec' % params.tgt_lang, params.n_init_ex, False)# = 5000, only read es 500 words
np.save('data/%s_%d' % (params.tgt_lang, params.n_init_ex), tgt_embeddings)

src_id2word, src_word2id, src_embeddings = utils.read_txt_embeddings('data/wiki.%s.vec' % params.src_lang, params.n_ft_ex, False) # = 7500, only read en 7500 words
np.save('data/%s_%d' % (params.src_lang, params.n_ft_ex), src_embeddings)
tgt_id2word, tgt_word2id, tgt_embeddings = utils.read_txt_embeddings('data/wiki.%s.vec' % params.tgt_lang, params.n_ft_ex, False) # = 7500, only read es 7500 words
np.save('data/%s_%d' % (params.tgt_lang, params.n_ft_ex), tgt_embeddings)

src_id2word, src_word2id, src_embeddings = utils.read_txt_embeddings('data/wiki.%s.vec' % params.src_lang, 10000, False) # = 10000, only read en 7500 words
np.save('data/%s_%d' % (params.src_lang, 10000), src_embeddings)
tgt_id2word, tgt_word2id, tgt_embeddings = utils.read_txt_embeddings('data/wiki.%s.vec' % params.tgt_lang, 10000, False) # = 10000, only read es 7500 words
np.save('data/%s_%d' % (params.tgt_lang, 10000), tgt_embeddings)
