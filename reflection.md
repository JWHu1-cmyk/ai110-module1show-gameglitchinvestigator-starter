# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least three concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
```
1
I kept seeing the message `📈 Go HIGHER!`
even though I am inputting number larger then 100.

I kept seeing the message '📉 Go LOWER!'
even though I am inputting number smaller then 0.

2
I have made 5 attempts.
but the Developer Debug Info console says I have made 6 Attempts.

3
Easy:
Range: 1 to 20
Attempts allowed: 6
Normal:
Range: 1 to 100
Attempts allowed: 8
Hard:
Range: 1 to 50
Attempts allowed: 5
// the `Range`, `Attempts allowed` attributes seem to have been assigned to diffculty level arbitrarily.

4
// fixed
once you enter the first letter.
the program would reject the first letter.
but once you enter a subsequent letter.
the program would accept the first letter.
that's not suppose to happen could you search the repo and find out what logic is broken thanks.
```

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
```
- I used Claude Code.

- For Bug #4, I described to Claude Code (in agent mode) that the first guess was being rejected but subsequent guesses were accepted. Claude suggested the issue was in the `secret` variable assignment around line 158 of `app.py`, where an `attempts % 2 == 0` conditional was converting `secret` to a string on even attempts but leaving it as an int on odd attempts — causing a type mismatch in `check_guess`. I verified this was correct by reading the original code and confirming the flip-flopping behavior, then removing the conditional so `secret` is always used directly from `session_state`. After the fix, every guess was evaluated consistently regardless of attempt number.

- For Bug #1, I told Claude Code that I kept seeing "Go HIGHER" even when guessing above 100 and "Go LOWER" when guessing below 0. Claude correctly identified that the hint messages in `check_guess` were swapped — when `guess > secret` the code returned "Go HIGHER" instead of "Go LOWER" and vice versa. However, Claude's initial description was slightly misleading because it framed it as the "emojis and text are backwards," which made it sound like the emojis were wrong too. In reality, the emojis were already paired with the correct direction (📈 with HIGHER, 📉 with LOWER) — the real issue was just that the wrong message was returned for each branch. I verified the fix by running the app and confirming that guessing above the secret now says "Go LOWER" and guessing below says "Go HIGHER."
```
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
```
- I decided a bug was fixed by first manually testing the app in Streamlit — for Bug #4, I made multiple guesses in a row and confirmed that every guess was evaluated correctly on the first attempt, not just on alternating ones. I also checked the git diff to make sure my change only removed the broken conditional and didn't introduce anything new.

- I had Claude Code generate a pytest case in `tests/test_game_logic.py` called `test_bug4_secret_type_consistency`. The test calls `check_guess(50, 50)` (int secret) and `check_guess(50, "50")` (str secret) and asserts both return `"Win"`. This showed me that `check_guess` can handle both types, but the real fix was ensuring the caller never passes a string in the first place.

- Yes, Claude Code wrote the test for me after I asked it to target the specific bug. It helped me understand that the core issue was a type mismatch between `int` and `str`, and the test was designed to catch that exact scenario if the bug ever gets reintroduced.
```
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

```
- Every time you interact with a Streamlit app — clicking a button, typing in a text box — the entire Python script reruns from top to bottom. That means any regular variable you define gets reset to its initial value on every interaction. To keep data around between reruns (like a secret number or an attempt counter), you have to store it in `st.session_state`, which is a dictionary that persists across reruns for the duration of the user's session. Think of it like a save file for your app: without it, the app has amnesia every time you click something.
```

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

```
- One habit I want to keep is describing the exact symptoms of a bug to the AI rather than guessing at the cause myself. When I told Claude Code what I was seeing ("the first guess gets rejected but the second one works"), it pinpointed the root cause faster than I would have by reading the code alone. Pairing that with checking the git diff after each fix helped me stay confident that only the intended change was made.

- Next time, I would double-check the AI's explanation more carefully before accepting it. For Bug #1, Claude's description was slightly misleading about the emojis being wrong when really it was just the message mapping. Going forward, I want to read the actual code diff myself instead of relying solely on the AI's summary of what changed.

- This project showed me that AI-generated code can look perfectly reasonable at first glance but still contain subtle logic bugs — like swapped messages or off-by-one errors — that only surface when you actually run the app. It reinforced that AI is a powerful drafting tool, but you still need to test and verify everything it produces.
```
