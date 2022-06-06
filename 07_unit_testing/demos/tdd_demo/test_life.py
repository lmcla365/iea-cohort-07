from life import Life


def test_life_init_blank_grid():
    grid = [
        [False, False],
        [False, False],]

    game = Life(grid)
    assert game.grid == grid


def test_life_init_single_cell():
    grid = [
        [True, False],
        [False, False],]

    game = Life(grid)
    assert game.grid == grid


def test_life_next_generation_empty():
    grid = [
        [False, False],
        [False, False],]

    expected = [
        [False, False],
        [False, False],]
    game = Life(grid)
    next_gen = game.next_generation()

    assert next_gen == expected


def test_life_next_generation_single_cell():
    grid = [
        [True, False],
        [False, False],]

    expected = [
        [False, False],
        [False, False],]
    game = Life(grid)
    next_gen = game.next_generation()

    assert next_gen == expected


def test_life_next_generation_all_alive():
    grid = [
        [True, True],
        [True, True],]

    expected = [
        [True, True],
        [True, True],]
    game = Life(grid)
    next_gen = game.next_generation()

    assert next_gen == expected


def test_life_next_generation_new_cell():
    grid = [
        [False, True],
        [True, True],]

    expected = [
        [True, True],
        [True, True],]
    game = Life(grid)
    next_gen = game.next_generation()

    assert next_gen == expected
