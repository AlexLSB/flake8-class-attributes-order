from conftest import run_validator_for_test_file


def test_always_ok_for_empty_file():
    errors = run_validator_for_test_file('errored.py')
    assert len(errors) == 2


def test_async_def_not_breaks_validator():
    assert not run_validator_for_test_file('async_def.py')
