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

# X = High Punch          Y = Block       Z = High Kick
# A = Low Punch           B = Block       C = Low Kick
# Jump Kick   :  Up + HIGH or LOW KICK
# Jump Punch  :  Up + HIGH or LOW PUNCH
# Roundhouse  :  Back + HIGH PUNCH
# Foot Sweep  :  Back + LOW PUNCH
# Uppercut    :  Down + HIGH PUNCH
# Crouch Punch:  Down + LOW PUNCH
# Crouch Kick :  Down + LOW KICK
# Turning Kick:  Jump over opponent.  When you pass the center of his body,
#                 press either KICK.  The character will turn and kick at the
#                 opponent.
# Throw       :  Forward + LOW PUNCH(Close to opponent)
# Avoid Throw :  Diagonally down away from opponent + BLOCK
# Close Move  :  Any attack button(Close to opponent)

class ShangTsungDiscretizer(Discretizer):
    def __init__(self, env):
        HP = 'X' 
        LP = 'A'
        HK = 'Z'
        LK = 'C'
        BL = 'Y'
        UP = 'UP'
        DOWN = 'DOWN'
        LEFT = 'LEFT'
        RIGHT = 'RIGHT'

        super().__init__(env=env, buttons=env.unwrapped.buttons, combos=[[],
        [HP], [LP], [HK], [LK], [BL], ['START'], [UP], [DOWN], [LEFT], [RIGHT], # single moves
        [UP, HK], [LEFT, UP, HK], [RIGHT, UP, HK], # jumps
        [UP, HP], [LEFT, UP, HP], [RIGHT, UP, HP], # jumps
        [LEFT, HP], [RIGHT, HP], [LEFT, DOWN, HP], [RIGHT, DOWN, HP],
        [LEFT, LP], [RIGHT, LP], [LEFT, UP, LP], [RIGHT, UP, LP], [LEFT, DOWN, LP], [RIGHT, DOWN, LP],
        [DOWN, HP],
        [DOWN, LP], 
        [DOWN, LK],
        [DOWN, BL],
        [LEFT, LEFT, HP], # Fire Skull
        [LEFT, LEFT, RIGHT, HP], # Double Fire Skull
        [LEFT, LEFT, RIGHT, RIGHT, HP], # Triple Fire Skull
        [RIGHT, LEFT, LEFT, LK], # Volcanic Eruption
        [HP, HP, LP], [LK, HP, HP, LP], # kombos
        [HP, HP, HP, HP] # unfair combo
        ])

gamename = "MortalKombat3-Genesis"
#state = '/home/pavel/projects/mkii-subzero-ppo2agent/Level1.ShangTsungVsLiuKang.state'
state = 'Level1.ShangTsungVsLiuKang.state'


# start from the 1st fight on very easy playing as Sub-Zero
def make_env():
    env = retro.make(gamename, state=state, obs_type=retro.Observations.IMAGE)
    env = ShangTsungDiscretizer(env)
    return env

def make_env_record():
    env = retro.make(gamename, state=state, obs_type=retro.Observations.IMAGE)
    env = ShangTsungDiscretizer(env)
    return env
