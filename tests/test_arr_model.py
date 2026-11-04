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


def test_members_needed_rejects_negative_target():
    with pytest.raises(ValueError):
        members_needed(-1, 1000)


def test_members_needed_zero_target_is_zero():
    assert members_needed(0, 1000) == 0


@pytest.mark.parametrize("members,price", [(-1, 100.0), (10, -5.0)])
def test_segment_rejects_negative_values(members, price):
    with pytest.raises(ValueError):
        Segment("bad", members, price, True)


def test_members_needed_ignores_float_noise():
    # 2.1 / 0.7 is 3.0000000000000004 in floating point; the exact answer is 3
    assert members_needed(2.1, 0.7) == 3


def test_doc07_tier_mix_blended_arr():
    tiers = [
        Segment("Operator Regional", 250, 2_500.0, True),
        Segment("Operator Dashboard", 100, 9_000.0, True),
        Segment("Operator Enterprise", 3, 60_000.0, True),
        Segment("Contractor Member", 450, 3_500.0, True),
        Segment("Contractor Dashboard", 190, 9_000.0, True),
        Segment("Contractor Enterprise", 7, 40_000.0, True),
    ]
    without_addon = arr(tiers)
    assert without_addon == 5_270_000
    with_addon = arr(tiers + [Segment("Predictive add-on", 150, 5_000.0, True)])
    assert with_addon == 6_020_000
    assert sum(s.members for s in tiers) == 1000
    assert with_addon / 1000 == 6020
