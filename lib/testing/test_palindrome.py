import pytest
from lib.palindrome import longest_palindromic_substring


@pytest.mark.parametrize(
    "s, expected_options",
    [
        ("babad", {"bab", "aba"}),     # example with 2 valid answers
        ("cbbd", {"bb"}),              # standard even-length case
        ("a", {"a"}),                  # single character
        ("ac", {"a", "c"}),            # no palindrome longer than 1
        ("racecar", {"racecar"}),      # whole string palindrome
    ],
)
def test_examples_from_instructions(s, expected_options):
    result = longest_palindromic_substring(s)
    assert result in expected_options


def test_all_same_character():
    result = longest_palindromic_substring("aaaa")
    assert result == "aaaa"


def test_no_palindrome_longer_than_one():
    result = longest_palindromic_substring("abcd")
    assert len(result) == 1
    assert result in set("abcd")


def test_palindrome_in_the_middle():
    result = longest_palindromic_substring("xyzracecarzzz")
    assert result == "zracecarz"


def test_even_length_palindrome():
    result = longest_palindromic_substring("abccba")
    assert result == "abccba"
