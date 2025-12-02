import pytest
from part01 import rotate


def test_rotate_right():
    """Test rotating right from a position"""
    assert rotate(10, 'R5') == 15
    assert rotate(50, 'R30') == 80


def test_rotate_left():
    """Test rotating left from a position"""
    assert rotate(20, 'L5') == 15
    assert rotate(50, 'L30') == 20


def test_rotate_right_with_wraparound():
    """Test rotating right with modulo 100 wraparound"""
    assert rotate(95, 'R10') == 5
    assert rotate(99, 'R1') == 0


def test_rotate_left_with_wraparound():
    """Test rotating left with modulo 100 wraparound"""
    assert rotate(5, 'L10') == 95
    assert rotate(0, 'L1') == 99


def test_rotate_zero():
    """Test rotating by zero amount"""
    assert rotate(50, 'R0') == 50
    assert rotate(50, 'L0') == 50


def test_rotate_full_circle():
    """Test rotating by exactly 100 (full circle)"""
    assert rotate(25, 'R100') == 25
    assert rotate(25, 'L100') == 25
