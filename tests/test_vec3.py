from pytrace.vec import Vec3, Color
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

def test_len(setup):
    u, v, w = setup
    
    assert u.length() == 77**.5
    assert v.length() == 14**0.5
    assert w.length() == (1+16+25)**0.5

def test_subtraction(setup):
    u, v, w = setup
    
    assert u - v == Vec3(3., 3., 3.)
    assert u - w == Vec3(5., 1., 1.)

def test_list_access(setup):
    u, _, _ = setup
    assert u[0] == 4
    assert u[1] == 5
    assert u[2] == 6

def test_tuple_access(setup):
    u, _, _ = setup
    assert u.tuple == (4, 5, 6)

def test_scalar_div(setup):
    u, v, w = setup
    
    assert u / 2 == Vec3(2., 2.5, 3.)
    assert v / 2 == Vec3(0.5, 1., 1.5)
    assert w / 2 == Vec3(-0.5, 2., 2.5)

def test_unit_vector(setup):
    u, v, w = setup
    assert u.unit_vector() == Vec3(0.4558423058385518, 0.5698028822981898, 0.6837634587578276)
    assert v.unit_vector() == Vec3(*[0.2672612419124244, 0.5345224838248488, 0.8017837257372732])
    assert w.unit_vector() == Vec3(*[-0.1543033499620919, 0.6172133998483676, 0.7715167498104596])

def test_dot_product(setup):
    u, v, w = setup
    
    assert u.dot(v) == 32.
    assert v.dot(w) == -1. + 8. + 15.

def test_repr(setup):
    u, v, w = setup
    assert repr(u) == "Vec3(4, 5, 6)"
    assert repr(v) == "Vec3(1.0, 2.0, 3.0)"
    assert repr(w) == "Vec3(-1.0, 4.0, 5.0)"
    
    x = eval(repr(u)) == Vec3(4, 5, 6)
    
def test_str(setup):
    u, _, _ = setup
    
    assert f"{u}" == "4 5 6"

def test_can_sum_list(setup):
    u, v, w = setup
    assert sum([u, v, w]) == Vec3(4., 11., 14.)

def test_cant_mul_by_str(setup):
    u, _, _ = setup
    with pytest.raises(TypeError):
        u * "Weee!"

def test_color_contains_bound_values():
    c = Color(45, 23, 8)
    assert f"{c}" == "225 115 40"
