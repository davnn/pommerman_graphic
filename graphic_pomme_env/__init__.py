import os
from pommerman import REGISTRY
from pommerman import constants, characters
import gym
import sys
from .graphic_pomme_env import PommeGraphic
from gym.envs.registration import register

from .graphic_pomme_env import STD_GRID_SIZE

# scaled approximately
BOARD_SIZE_OVO_COMPACT = 6
NUM_RIGID_OVO_COMPACT = 8
NUM_WOOD_OVO_COMPACT = 10
NUM_ITEMS_OVO_COMPACT = 5

# scaled approximately
BOARD_SIZE_OVO_NANO = 5
NUM_RIGID_OVO_NANO = 4
NUM_WOOD_OVO_NANO = 6
NUM_ITEMS_OVO_NANO = 3


def custom_conf():
    """Start up a FFA config with the default settings. (Graphic version)"""
    env = PommeGraphic
    game_type = constants.GameType.FFA
    env_entry_point = 'graphic_pomme_env.graphic_pomme_env:PommeGraphic'
    env_id = 'GraphicPommeFFAFast-v0'
    env_kwargs = {
        'sprite_size': STD_GRID_SIZE,
        'game_type': game_type,
        'board_size': constants.BOARD_SIZE,
        'num_rigid': constants.NUM_RIGID,
        'num_wood': constants.NUM_WOOD,
        'num_items': constants.NUM_ITEMS,
        'max_steps': constants.MAX_STEPS,
        'render_fps': 1000,
        'env': env_entry_point,
    }
    agent = characters.Bomber
    return locals()

def custom_one_vs_one_env():
    """Start up an OneVsOne config with the default settings."""
    env = PommeGraphic
    game_type = constants.GameType.OneVsOne
    env_entry_point = 'graphic_pomme_env.graphic_pomme_env:PommeGraphic'
    env_id = 'GraphicOneVsOne-v0'
    env_kwargs = {
        'sprite_size': STD_GRID_SIZE,
        'game_type': game_type,
        'board_size': constants.BOARD_SIZE_ONE_VS_ONE,
        'num_rigid': constants.NUM_RIGID_ONE_VS_ONE,
        'num_wood': constants.NUM_WOOD_ONE_VS_ONE,
        'num_items': constants.NUM_ITEMS_ONE_VS_ONE,
        'max_steps': constants.MAX_STEPS,
        'render_fps': constants.RENDER_FPS,
        'env': env_entry_point,
    }
    agent = characters.Bomber
    return locals()


def custom_ovo_compact():
    """Start up an OneVsOne config with the default settings."""
    env = PommeGraphic
    game_type = constants.GameType.OneVsOne
    env_entry_point = 'graphic_pomme_env.graphic_pomme_env:PommeGraphic'
    env_id = 'GraphicOVOCompact-v0'
    env_kwargs = {
        'sprite_size': STD_GRID_SIZE,
        'game_type': game_type,
        'board_size': BOARD_SIZE_OVO_COMPACT,
        'num_rigid': NUM_RIGID_OVO_COMPACT,
        'num_wood': NUM_WOOD_OVO_COMPACT,
        'num_items': NUM_ITEMS_OVO_COMPACT,
        'max_steps': constants.MAX_STEPS,
        'render_fps': constants.RENDER_FPS,
        'env': env_entry_point,
    }
    agent = characters.Bomber
    return locals()


def custom_ovo_nano():
    """Start up an OneVsOne config with the default settings."""
    env = PommeGraphic
    game_type = constants.GameType.OneVsOne
    env_entry_point = 'graphic_pomme_env.graphic_pomme_env:PommeGraphic'
    env_id = 'GraphicOVONano-v0'
    env_kwargs = {
        'sprite_size': STD_GRID_SIZE,
        'game_type': game_type,
        'board_size': BOARD_SIZE_OVO_NANO,
        'num_rigid': NUM_RIGID_OVO_NANO,
        'num_wood': NUM_WOOD_OVO_NANO,
        'num_items': NUM_ITEMS_OVO_NANO,
        'max_steps': constants.MAX_STEPS,
        'render_fps': constants.RENDER_FPS,
        'env': env_entry_point,
    }
    agent = characters.Bomber
    return locals()

if __name__ == '__main__':
    raise Exception('Is a library')
else:
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    for config in [custom_conf(), custom_one_vs_one_env(), custom_ovo_compact(), custom_ovo_nano()]:
        REGISTRY.append(config['env_id'])
        register(
            id=config['env_id'],
            entry_point=config['env_entry_point'],
            kwargs=config['env_kwargs']
        )
        # print("{} env is registered.".format(config['env_id']))
