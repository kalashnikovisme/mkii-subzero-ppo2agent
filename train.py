import retro
from stable_baselines.common.policies import CnnLstmPolicy
from stable_baselines.common.vec_env import SubprocVecEnv, DummyVecEnv, VecFrameStack, VecNormalize
from stable_baselines import PPO2
import numpy as np
import gym
from stable_baselines.common.callbacks import CheckpointCallback
from utils import *

gamename = "MortalKombat3-Genesis"

if __name__ == "__main__":
    n_cpu = 16

    env = SubprocVecEnv([make_env] * n_cpu)
    env = VecFrameStack(env, n_stack=4)

    model = PPO2(CnnLstmPolicy, env, n_steps=128, verbose=1, tensorboard_log="./tboard_log")   
    # Use this if you want to continue training a saved model
    # model = PPO2.load("training_checkpoints/mk3-ppo2_16000_steps.zip", tensorboard_log="./tboard_log")
    # model.set_env(env)

    checkpoint_callback = CheckpointCallback(save_freq=1000, save_path='./training_checkpoints',
                                            name_prefix='mk3-ppo2')
    model.learn(total_timesteps=2000, callback=checkpoint_callback)
    model.save('mk3-ppo2')
    env.close()
