from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_bug4_secret_type_consistency():
    """
    FIX 4 regression test: The original bug converted secret to str on even
    attempts (attempts % 2 == 0), causing check_guess to compare int vs str.
    This led to the first guess being rejected and the next one accepted.
    Verify that check_guess returns the same result regardless of secret's type.
    """
    # When secret is int (odd attempt behavior) — should be correct
    outcome_int, _ = check_guess(50, 50)
    # When secret is str (even attempt behavior — the bug) — should also be correct
    outcome_str, _ = check_guess(50, "50")

    assert outcome_int == "Win"
    assert outcome_str == "Win", (
        "check_guess should handle str secret, but the caller should never "
        "pass a str — this guards against the even/odd type-flip bug"
    )


def test_bug1_hint_messages_correct_direction():
    """
    FIX 1 regression test: The original bug had hint messages swapped —
    guessing too high said "Go HIGHER" and guessing too low said "Go LOWER".
    Verify that the hints point the player in the correct direction.
    """
    # Guessing 80 when secret is 50 — too high, should tell player to go lower
    outcome_high, message_high = check_guess(80, 50)
    assert outcome_high == "Too High"
    assert "LOWER" in message_high, (
        f"When guess is too high, hint should say LOWER, got: {message_high}"
    )

    # Guessing 20 when secret is 50 — too low, should tell player to go higher
    outcome_low, message_low = check_guess(20, 50)
    assert outcome_low == "Too Low"
    assert "HIGHER" in message_low, (
        f"When guess is too low, hint should say HIGHER, got: {message_low}"
    )
