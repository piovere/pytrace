from pytrace.ray import Ray
from pytrace.vec import Point3, Vec3

import pytest

@pytest.fixture
def setup():
    o = Point3(0, 0, 0)
    d = Vec3(1, 1, -1)
    return (o, d)

def test_ray_moves_forward(setup):
    r = Ray(*setup)
    assert r.at(1.) == Point3(1., 1., -1.)
    assert r.at(0.5) == Point3(0.5, 0.5, -0.5)
