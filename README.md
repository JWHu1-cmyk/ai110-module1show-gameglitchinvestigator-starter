# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  - A Streamlit-based number guessing game where the player picks a difficulty, then tries to guess a randomly generated secret number within a limited number of attempts. The app gives "higher" or "lower" hints after each guess.

- [x] Detail which bugs you found.
  1. **Swapped hint messages** — `check_guess` returned "Go HIGHER" when the guess was too high and "Go LOWER" when too low, pointing the player in the wrong direction.
  2. **Off-by-one attempt counter** — `st.session_state.attempts` was initialized to `1` instead of `0`, so the Developer Debug Info always showed one extra attempt.
  3. **Scrambled difficulty settings** — The range and attempt limits for Easy, Normal, and Hard were assigned to the wrong difficulty levels.
  4. **Type-flipping secret** — On even attempts the secret was converted to a string, causing `check_guess` to compare `int` vs `str` and reject valid guesses on the first try.

- [x] Explain what fixes you applied.
  1. **Fix 1 (app.py, `check_guess`)** — Swapped the hint messages so "Too High" returns "Go LOWER" and "Too Low" returns "Go HIGHER."
  2. **Fix 2 (app.py, line 96)** — Changed `st.session_state.attempts = 1` to `= 0` so the counter starts at zero.
  3. **Fix 4 (app.py, line 158)** — Removed the `attempts % 2 == 0` conditional that converted the secret to a string on even attempts, so `secret` is always used directly from `session_state`.

## 📸 Demo

- [x] ![Screenshot](CleanShot%202026-03-15%20at%2014.37.10@2x.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
