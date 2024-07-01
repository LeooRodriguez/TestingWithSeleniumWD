import pytest

@pytest.fixture(params=[
    'standard_user',
    'locked_out_user',
    'problem_user',
    'performance_glitch_user',
    'visual_user',
    'error_user'
])
def username(request):
    return request.param

@pytest.fixture
def password():
    return 'secret_sauce'
