from pytrace.vec import Vec3
import pytest

@pytest.fixture
def setup():
    u = Vec3(4, 5, 6)
    v = Vec3(1., 2., 3.)
    w = Vec3(-1., 4., 5.)

    return u, v, w

def test_vec_addition(setup):
    u, v, w = setup

    assert v + w == Vec3(0., 6., 8.)
    assert u + w == Vec3(3., 9., 11.)

def test_scalar_mult(setup):
    u, v, _ = setup

    assert 3 * u == Vec3(12, 15, 18)
    assert v * 3 == Vec3(3., 6., 9.)
