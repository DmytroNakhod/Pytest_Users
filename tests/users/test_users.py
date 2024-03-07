import pytest
from src.baseclasses.response import Response
from src.schemas.user import User


def test_get_users_list(get_users):
    Response(get_users).assert_status_code(200).validate(User)


@pytest.mark.staging
@pytest.mark.production
@pytest.mark.skip('[ISSUE-23414] Issue with network connection')
def test_another():
    assert 1 == 1


@pytest.mark.production
@pytest.mark.staging
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'b', None)
])
def test_calculator(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result


@pytest.mark.staging
@pytest.mark.production
def test_another_failed_t():
    assert 1 == 2
