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


def test_bug2_attempts_initialized_to_zero():
    """
    FIX 2 regression test: The original bug initialized attempts to 1 instead
    of 0, so the debug info always showed one extra attempt. This test reads
    app.py and verifies the initial value is 0.
    """
    import ast
    import os

    app_path = os.path.join(os.path.dirname(__file__), "..", "app.py")
    with open(app_path) as f:
        source = f.read()

    tree = ast.parse(source)
    for node in ast.walk(tree):
        # Look for: st.session_state.attempts = 0
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Attribute)
            and node.targets[0].attr == "attempts"
        ):
            # The first assignment is the initialization
            assert isinstance(node.value, ast.Constant), (
                "attempts should be initialized to a constant"
            )
            assert node.value.value == 0, (
                f"attempts should be initialized to 0, got {node.value.value}"
            )
            return

    raise AssertionError("Could not find attempts initialization in app.py")
