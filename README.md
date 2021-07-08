# Keras  - MAML

## Part 1. Introduction
This is an experimental code base

The biggest difference between MAML and pre-training weights：Pre-training weights minimize only for original task loss. MAML can minimize all task loss with a few steps of training.


## Part 2. Quick  Start

1. Pull repository.

```shell
git clone https://github.com/verages/MAML.git
```

2. You need to install some dependency package.

```shell
cd MAML
pip installl -r requirements.txt
```

3. Download the *Omiglot* dataset and maml weights.

```shell

```

4. Run **evaluate.py**, you'll see the difference between MAML and random initialization weights.

```shell
python evaluate.py
```

## Part 3. Train your own dataset
1. You should set same parameters in **config.py**. 

```python
n_way = "number of classes"
k_shot = "number of support set"
q_query = "number of query set"
```

2. Start training.

```shell
python train.py
```

3. Running tensorboard to monitor the training process.

```shell
tensorboard --logdir=./summary
```

![tensorboard.png](https://i.loli.net/2021/04/30/KYx2FG3cpdrjSzu.png)

## Part 4. Paper and other implement

- [Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks](https://arxiv.org/pdf/1703.03400.pdf)
- [cbfinn/*maml*](https://github.com/cbfinn/maml)
- [dragen1860/*MAML*-Pytorch](https://github.com/dragen1860/MAML-Pytorch)
