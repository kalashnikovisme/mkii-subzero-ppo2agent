import numpy as np
import gym
import retro

class Discretizer(gym.ActionWrapper):
    """
    Wrap a gym environment and make it use discrete actions.
    based on https://github.com/openai/retro-baselines/blob/master/agents/sonic_util.py
    Args:
        buttons: ordered list of buttons, corresponding to each dimension of the MultiBinary action space
        combos: ordered list of lists of valid button combinations
    """

    def __init__(self, env, buttons, combos):
        super().__init__(env)
        assert isinstance(env.action_space, gym.spaces.MultiBinary)
        self._decode_discrete_action = []
        for combo in combos:
            arr = np.array([False] * env.action_space.n)
            for button in combo:
                arr[buttons.index(button)] = True
            self._decode_discrete_action.append(arr)

        self.action_space = gym.spaces.Discrete(len(self._decode_discrete_action))

    def action(self, act):
        return self._decode_discrete_action[act].copy()


class ShangTsungDiscretizer(Discretizer):
    def __init__(self, env):
        HP = 'X' 
        LP = 'A'
        HK = 'Z'
        LK = 'C'
        BL = 'B'
        UP = 'UP'
        DOWN = 'DOWN'
        LEFT = 'LEFT'
        RIGHT = 'RIGHT'

       super().__init__(env = env, buttons = env.unwrapped.buttons, combos = [
           [],
           [LEFT, LEFT, LEFT, LEFT ]
           # [HP], [LP], [HK], [LK], [BL], [UP], [DOWN], [LEFT], [RIGHT], # single moves
           # [UP, HK], [LEFT, UP, HK], [RIGHT, UP, HK], # jumps
           # [UP, HP], [LEFT, UP, HP], [RIGHT, UP, HP], # jumps
           # [LEFT, HP], [RIGHT, HP], [LEFT, DOWN, HP], [RIGHT, DOWN, HP],
           # # [LEFT, LP], [RIGHT, LP], [LEFT, UP, LP], [RIGHT, UP, LP], [LEFT, DOWN, LP], [RIGHT, DOWN, LP],
           # [DOWN, HP],
           # [DOWN, LP], 
           # [DOWN, LK],
           # [DOWN, BL],
           # [LEFT, LEFT, HP], [RIGHT, RIGHT, HP], # Fire Skull
           # [LEFT, LEFT, RIGHT, HP], [RIGHT, RIGHT, LEFT, HP], # Double Fire Skull
           # [LEFT, LEFT, RIGHT, RIGHT, HP], [RIGHT, RIGHT, LEFT, LEFT, HP] # Triple Fire Skull
           # [RIGHT, LEFT, LEFT, LK], [LEFT, RIGHT, RIGHT, LK], # Volcanic Eruption
           # [HP, HP, LP], [LK, HP, HP, LP], # kombos
           # [HP, HP, HP, HP], [LP, LP, LP, LP], # unfair combo
           # [LEFT, LK], [RIGHT, LK], # podnozhka :)
           # [DOWN, HP] # uppercut
         ]
       )

gamename = "MortalKombat3-Genesis"
#state = 'kabal2.state'
#state = 'Level1.ShangTsungVsLiuKang.state'

def make_env():
    env = retro.make(gamename, state = retro.State.DEFAULT)
    env = ShangTsungDiscretizer(env)
    return env

def make_env_record():
    env = retro.make(gamename, state = retro.State.DEFAULT)
    env = ShangTsungDiscretizer(env)
    return env
