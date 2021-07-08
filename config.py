# -*- coding: utf-8 -*-
# @Brief: 配置文件

train_data_path = "./Omniglot/images_background/"
test_data_path = "./Omniglot/images_evaluation/"
summary_path = "./summary"

batch_size = 4
val_batch_size = 20
epochs = 10
inner_lr = 0.02
outer_lr = 0.0001

n_way = 5
k_shot = 1
q_query = 1

input_shape = (28, 28, 1)
