import pytest
from model.arr_model import Segment, arr, members_needed, required_arr


def test_required_arr_values():
    assert required_arr(300e6, 8) == 37.5e6
    assert required_arr(500e6, 5) == 100e6


@pytest.mark.parametrize("ev,mult", [(300e6, 0), (0, 5), (-1, 5), (300e6, -2)])
def test_required_arr_rejects_nonpositive(ev, mult):
    with pytest.raises(ValueError):
        required_arr(ev, mult)


def test_arr_counts_only_paying_segments():
    segs = [Segment("ROW managers", 2000, 0.0, False),
            Segment("Operators", 100, 50_000.0, True)]
    assert arr(segs) == 5_000_000.0


def test_free_segment_with_price_contributes_zero():
    assert arr([Segment("ROW managers", 2000, 99.0, False)]) == 0


def test_members_needed_rounds_up():
    assert members_needed(1_000_000, 30_000) == 34


def test_members_needed_rejects_bad_price():
    with pytest.raises(ValueError):
        members_needed(1_000_000, 0)
