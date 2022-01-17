from typing import Container, ContextManager
import pytest
import os
from simpCity import init_game, save_game, main
from io import BytesIO


def test_saving_game_creates_a_save_file(tmp_path):
    # Arrange
    game_board = [['', '', '', ''], ['', '', '', ''],
                  ['', '', '', ''], ['', '', '', ''], ]
    building_pool = {"HSE": 8, "FAC": 8, "SHP": 8, "HWY": 8, "BCH": 8}
    temp_file = str(tmp_path) + "/pickle.save"

    # Act
    save_game(game_board, building_pool, temp_file)

    # Assert
    assert os.path.exists(tmp_path)


def test_init_game_creates_game_board_and_pool():
    # Act
    game_board, building_pool = init_game()

    # Assert
    assert game_board == [['', '', '', ''], ['', '', '', ''],
                          ['', '', '', ''], ['', '', '', ''], ]
    assert building_pool == {"HSE": 8, "FAC": 8, "SHP": 8, "HWY": 8, "BCH": 8}

