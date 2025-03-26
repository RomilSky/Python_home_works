import pytest
from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()


def test_capitalize_normal(string_utils):
    assert string_utils.capitalize("skypro") == "Skypro"

def test_capitalize_empty(string_utils):
    assert string_utils.capitalize("") == ""

def test_capitalize_whitespace(string_utils):
    assert string_utils.capitalize(" ") == " "

def test_capitalize_numbers(string_utils):
    assert string_utils.capitalize("123") == "123"


def test_trim_normal(string_utils):
    assert string_utils.trim("   skypro") == "skypro"

def test_trim_no_spaces(string_utils):
    assert string_utils.trim("skypro") == "skypro"

def test_trim_only_spaces(string_utils):
    assert string_utils.trim("   ") == ""

def test_trim_empty(string_utils):
    assert string_utils.trim("") == ""

def test_contains_true(string_utils):
    assert string_utils.contains("SkyPro", "S") is True

def test_contains_false(string_utils):
    assert string_utils.contains("SkyPro", "U") is False

def test_contains_empty_string(string_utils):
    assert string_utils.contains("", "S") is False

def test_contains_empty_symbol(string_utils):
    assert string_utils.contains("SkyPro", "") is True


def test_delete_symbol_exists(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_symbol_not_exists(string_utils):
    assert string_utils.delete_symbol("SkyPro", "X") == "SkyPro"

def test_delete_symbol_multiple_occurrences(string_utils):
    assert string_utils.delete_symbol("aabba", "a") == "bb"

def test_delete_symbol_empty_string(string_utils):
    assert string_utils.delete_symbol("", "a") == ""

def test_delete_symbol_empty_symbol(string_utils):
    assert string_utils.delete_symbol("SkyPro", "") == "SkyPro"
