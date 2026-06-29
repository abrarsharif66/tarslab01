# 🗓️ Day 01 — Class Checklist & Teaching Script
### TARS Lab Academy · 45-Day Generative AI Engineer Bootcamp
**Topic:** Python Core & Environments · **Duration:** ~1 hour

Legend used below:
- 😄 = lighten the mood / joke cue
- ❓ = question to throw at the class (keep it interactive)
- 🖐️ = show of hands / quick poll
- 💻 = switch to notebook / live code

---

# PART 1 — THE CHECKLIST
*(Tick as you go. The line in brackets = what to actually cover.)*

- [ ] **1. Instructor Introduction**
  *(Who you are, what you do as an AI engineer — keep it short & warm. This part is yours.)*

- [ ] **2. Why This Course Exists**
  *(The skill gap you've seen between students and the industry; how GenAI hiring has exploded; what they'll be able to build by Day 45.)*

- [ ] **3. Get to Know the Students**
  *(Quick round of intros + poll their Python familiarity so you can calibrate the pace.)*

- [ ] **4. Agenda for Today**
  *(One-line tour of what this hour covers: setup → variables → types → operators → control flow → data structures → build.)*

- [ ] **5. What is a Programming Language?**
  *(Plain-English: how we give instructions to a computer; source code → machine.)*

- [ ] **6. High-Level vs Low-Level Languages**
  *(Spectrum from machine code/assembly → C → Python; why Python is high-level & readable.)*

- [ ] **7. Environment Setup**
  *(VS Code, Conda, UV, and virtual environments — why isolation matters.)*

- [ ] **8. Variables & Dynamic Typing**
  *(What a variable is; naming; assignment; Python infers the type.)*

- [ ] **9. Data Types**
  *(Numbers: int / float / complex · Strings · Booleans & None · type conversion.)*

- [ ] **10. Operators**
  *(Arithmetic · comparison · logical · assignment · membership & identity.)*

- [ ] **11. Conditional Statements**
  *(if / elif / else, indentation, the ternary one-liner.)*

- [ ] **12. Loops**
  *(for + range, while, break / continue.)*

- [ ] **13. Data Structures**
  *(List · list comprehension · tuple · set · dict — when to use each.)*

- [ ] **14. 🔨 Build: Data-Manipulation Exercise**
  *(Hands-on practice on student records — clean, average, dedupe, filter, group; with hints.)*

- [ ] **15. Recap & Homework**
  *(Recap the day; assign notebook completion + push to GitHub; tease Day 2.)*

---
---

# PART 2 — THE FULL SCRIPT
*(Same headings, now with talking points, jokes 😄 and questions ❓.)*

---

## 1. Instructor Introduction
> 🎤 **This part is yours — leave it natural.**

Introduce yourself, your background, and what you do day-to-day as an AI engineer. Keep it to ~2 minutes — warm, human, not a résumé reading.

😄 *Optional opener:* "Before we start — yes, the course is 45 days, and no, I will not be replaced by an AI by Day 46. We checked."

---

## 2. Why This Course Exists

**Talking points:**
- "I'm building AI systems in the real world, and I kept noticing the same thing: there's a **huge gap** between what students *know* and what the industry actually *needs*. People finish a Python course or an ML playlist… and still can't ship a working AI application."
- "Meanwhile, look at the job market — **Generative AI roles have absolutely exploded.** Companies are scrambling for engineers who can take an LLM from a cute demo to a real, reliable, secure, deployed product. The demand is far ahead of the supply of people who can actually do it."
- "That gap *is* the opportunity. This bootcamp is designed to put you on the *right* side of it — not just 'I watched some videos,' but 'I built this, here's the repo, here's it running in production.'"
- "By Day 45 you won't have notes. You'll have a **portfolio**: RAG systems, agents, a fine-tuned model, evaluation, guardrails, and a deployed capstone."

❓ **Ask the class:** "Quick one — how many of you are here because you've *tried* to build something with AI and got stuck somewhere?" 🖐️
*(This instantly tells you their starting frustration level.)*

😄 "Good news: 'getting stuck' is literally the job. The difference is, by the end of this, you'll know *how* to get unstuck."

---

## 3. Get to Know the Students

**Say:** "Since this is Day 1, before I throw any code at you, I genuinely want to know who's in the room — it helps me pitch this at the right level for *you*."

**Run a quick round** (or a poll if the group is large). Ask each / show of hands:
- 🖐️ "Your name and what you're studying / doing right now."
- 🖐️ "Have you written Python before? — (a) never, (b) a little, (c) pretty comfortable."
- 🖐️ "Have you used any AI tool beyond ChatGPT — like an API, LangChain, anything?"

> 🧠 **Why you're doing this:** you're calibrating. If most say "never," slow down on Sections 5–9. If most say "comfortable," move faster through basics and spend the saved time on the build.

😄 "Don't worry about giving the 'right' answer — there are no wrong answers here. Except saying you write code only in Microsoft Word. *That* would concern me."

---

## 4. Agenda for Today

**Say:** "Here's the plan for the next hour — nothing scary:"
1. What a programming language even is (super quick, for everyone's sake).
2. Set up our workspace — VS Code, Conda/UV, environments.
3. The Python core: **variables, data types, operators.**
4. Making decisions and repeating things: **conditionals & loops.**
5. Storing collections of data: **lists, tuples, sets, dictionaries.**
6. Then we get our hands dirty with a **real data-manipulation exercise.**

"Every concept, we'll run live in the notebook together. You code *with* me, not after me." 💻

---

## 5. What is a Programming Language?

**Talking points:**
- "A computer is incredibly fast but incredibly dumb — it only does *exactly* what it's told. A **programming language** is just the language we use to tell it what to do."
- "You write instructions (**source code**) in something humans can read; a translator turns it into something the machine understands (**0s and 1s / machine code**)."
- "Analogy: it's a recipe. You write the steps clearly; the computer is a chef who follows them literally — no improvising."

❓ **Ask:** "If I tell a human 'make me tea,' they fill in the gaps. If I tell a computer 'make me tea' with no steps — what happens?"
*(Answer you're fishing for: nothing, or an error. Computers don't assume.)*

😄 "Computers are like that one extremely literal friend. You say 'grab me a soda from the fridge if there's beer, get two' — and they bring two sodas. (Old programmer joke. You'll get it by Day 10.)"

---

## 6. High-Level vs Low-Level Languages

**Talking points — paint it as a spectrum:**

| | Low-Level | High-Level |
|---|---|---|
| Examples | Machine code, Assembly, (C is mid/low-ish) | **Python**, JavaScript, Java |
| Closeness to hardware | Very close — you manage memory yourself | Far — the language handles details for you |
| Readability | Hard for humans | Reads almost like English |
| Speed to write | Slow, error-prone | Fast |

- "**Low-level** = closer to the machine. Powerful and fast, but you sweat every detail (memory, registers). Think Assembly."
- "**High-level** = closer to *us*. The language hides the messy hardware stuff so you focus on the *idea*."
- "**Python is high-level** — that's exactly why the entire AI world runs on it. You write `name = 'TARS'` and you're done; you don't tell the computer which memory address to use."

❓ **Ask:** "Given all that — why do you think AI researchers picked Python and not something super fast like Assembly?"
*(Answer: readability + speed of experimentation + libraries matter more than squeezing raw speed. We prototype fast.)*

😄 "Writing AI in Assembly would be like commuting to work on a unicycle. Technically possible. Deeply unnecessary. Slightly concerning."

---

## 7. Environment Setup
> 💻 Switch to terminal / VS Code here.

**Talking points:**
- "**VS Code** — our editor. Install the *Python* and *Jupyter* extensions. This is where we write and run everything."
- "**Conda** — manages Python versions and heavy packages cleanly."
- "**UV** — a newer, *much* faster package manager. Same job as pip, but seconds instead of minutes."
- "**Virtual environment** — the big idea: every project gets its **own isolated box** of dependencies, so Project A's versions never break Project B."

**Live demo:**
```bash
# Conda
conda create -n genai python=3.11 -y
conda activate genai

# or UV (fast)
uv venv
source .venv/bin/activate
uv pip install numpy pandas streamlit
```

❓ **Ask:** "Why might it be a *terrible* idea to install everything into one global Python for all your projects?"
*(Answer: version clashes — upgrading a package for one project silently breaks another.)*

😄 "Virtual environments are like separate lunchboxes. You don't want your project's spicy dependency leaking into everyone else's sandwich."

---

## 8. Variables & Dynamic Typing
> 💻 Notebook from here on.

**Talking points:**
- "A **variable** is just a *name* that points to a value. `days = 45` means: the name `days` now refers to the number 45."
- "Python is **dynamically typed** — you don't declare the type, Python figures it out. And it can even change."

**Live code:**
```python
name = "TARS"        # str
days = 45            # int
days = "forty-five"  # totally legal — now it's a str
a, b = 1, 2          # multiple assignment
a, b = b, a          # swap with no temp variable 😎
```

❓ **Ask:** "If I write `x = 5` and then `x = 'hello'`, will Python complain?"
*(Answer: No — that's dynamic typing. Try it live and show it.)*

😄 "Variables are like nicknames. 'days' is a nickname for 45. And just like real nicknames, if you choose a bad one, everyone's confused later. So please — no variables named `x1`, `x2`, `xx`."

---

## 9. Data Types

### 9a. Numbers — int, float, complex
```python
count = 42         # int (unlimited size in Python!)
price = 19.99      # float
big   = 1_000_000  # underscores just for readability
z     = 2 + 3j     # complex
```
❓ **Ask:** "What do you think `7 / 2` gives — `3` or `3.5`?"
*(Answer: `3.5`. Then show `7 // 2` → `3`, floor division. Great gotcha moment.)*

😄 "Python ints have *no size limit*. You can compute a number so big it wouldn't fit on this projector. Please don't, the projector has feelings."

### 9b. Strings — text
```python
course = "GenAI Bootcamp"
course[0]        # 'G'  (indexing starts at 0!)
course[0:5]      # 'GenAI'  (slicing)
course[::-1]     # reversed
f"Day {1} of {45}"   # f-string -> 'Day 1 of 45'
```
❓ **Ask:** "Indexing starts at… 0 or 1?"
*(Answer: 0. The classic. Watch half the room hesitate.)*

😄 "Programmers count 0, 1, 2… which is why we say a course has 'Day 0.' We're not weird, we're just… zero-indexed."

> 💡 Mention: strings are **immutable** — methods like `.upper()` return a *new* string, they don't change the original.

### 9c. Booleans & None
```python
is_ready = True      # bool: True / False
result   = None      # 'no value yet'
bool(0), bool(""), bool([])   # all False (falsy)
bool(42), bool("hi")          # both True (truthy)
```
❓ **Ask:** "Is an empty string `''` True or False when treated as a boolean?"
*(Answer: False — it's 'falsy'. List the falsy gang: `0, 0.0, '', [], {}, None, False`.)*

### 9d. Type Conversion (Casting)
```python
int("10")     # 10
float("3.14") # 3.14
str(99)       # "99"
isinstance(x, int)   # preferred way to CHECK a type
```
😄 "Casting is like translating. `int('10')` works. `int('hello')`… Python will look at you, sigh, and throw a `ValueError`."

---

## 10. Operators

### 10a. Arithmetic
`+  -  *  /  //  %  **`
```python
7 + 2    # 9
7 / 2    # 3.5  (true division)
7 // 2   # 3    (floor division)
7 % 2    # 1    (remainder / modulo)
7 ** 2   # 49   (power)
```
❓ **Ask:** "How would I check if a number is **even** using one of these?"
*(Answer: `n % 2 == 0`. The modulo trick — they'll use this constantly.)*

### 10b. Comparison & Logical
```python
score >= 60 and attendance > 0.8   # both must be true
value or "default"                 # fallback if value is falsy
18 <= age < 65                     # chained comparison — very Pythonic
```
❓ **Ask:** "What's the difference between `=` and `==`?"
*(Answer: `=` assigns, `==` compares. The #1 beginner bug. Burn it in.)*

😄 "`=` is 'make it so.' `==` is 'is it so?' Mix them up and Python *will* judge you."

### 10c. Assignment, Membership & Identity
```python
total += 5            # same as total = total + 5
"a" in "cat"          # True — membership
x is None             # identity check
```
> 💡 Rule: use `==` for **values**, `is` only for **identity** (mostly `is None`).

---

## 11. Conditional Statements

**Talking points:** "This is how programs make **decisions**. And note — Python uses **indentation** (4 spaces) to group code, not curly braces."
```python
def phase_for(day):
    if day <= 3:
        return "Foundations"
    elif day <= 7:
        return "How LLMs Work"
    else:
        return "Advanced"

status = "pass" if score >= 60 else "fail"   # ternary one-liner
```
❓ **Ask:** "What happens if I get the indentation wrong in Python?"
*(Answer: it breaks — `IndentationError`. In Python, whitespace is *not* optional. Demo it live.)*

😄 "In most languages indentation is for looks. In Python, it's the *law*. Python is the strict teacher who takes marks off for messy handwriting."

---

## 12. Loops

**Talking points:** "Loops = doing something repeatedly without copy-pasting."
```python
for day in range(1, 46):       # 1 to 45
    print(day, phase_for(day))

for i, topic in enumerate(topics):   # index + value
    print(i, topic)

# while + break + continue
day = 0
while True:
    day += 1
    if day % 2 == 0:
        continue   # skip evens
    if day > 7:
        break      # stop
    print("odd study day:", day)
```
❓ **Ask:** "What's the difference between `break` and `continue`?"
*(Answer: `break` exits the whole loop; `continue` skips to the next iteration.)*

😄 "`continue` is 'skip this one, next!' `break` is 'I'm done, I'm leaving.' Basically `continue` = skipping a bad song, `break` = leaving the party."

---

## 13. Data Structures

**Frame it:** "Four ways to store *collections* of data. Picking the right one is half of clean Python."

| Structure | Ordered | Mutable | Duplicates | Looks like |
|-----------|---------|---------|------------|------------|
| **list**  | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| **tuple** | ✅ | ❌ | ✅ | `(x, y)` |
| **set**   | ❌ | ✅ | ❌ unique | `{1, 2}` |
| **dict**  | ✅ | ✅ | keys unique | `{"k": 1}` |

### 13a. Lists
```python
topics = ["setup", "vars", "loops"]
topics.append("dicts")     # add
topics[0] = "env"          # change in place
topics[1:3]                # slice
```
### 13b. List Comprehensions
```python
squares = [n**2 for n in range(10)]
evens   = [n for n in nums if n % 2 == 0]
```
❓ **Ask:** "Which reads better — a 4-line loop that builds a list, or one comprehension line?" *(Sell readability.)*

### 13c. Tuples
```python
point = (10, 20)
x, y = point        # unpacking
# point[0] = 5      # ❌ error — tuples can't change
```
😄 "A tuple is a list that went to finishing school. Sits still, behaves, never changes."

### 13d. Sets
```python
tools = {"uv", "conda", "uv"}   # -> {'uv', 'conda'}  (dupes gone)
"uv" in tools                   # fast membership test
{1,2} | {2,3}                   # union
```
❓ **Ask:** "If I have a list with thousands of duplicate emails, what's the fastest way to get the unique ones?" *(Answer: `set(emails)`.)*

### 13e. Dictionaries
```python
student = {"name": "Ada", "scores": [82, 91]}
student["name"]              # 'Ada'
student.get("email", "n/a")  # safe lookup
student["city"] = "Lagos"    # add/update
for k, v in student.items(): # iterate pairs
    print(k, v)
```
💡 "Dicts are *everywhere* in AI — JSON, API responses, configs all map straight to dictionaries."

---

## 14. 🔨 Build: Data-Manipulation Exercise
> 💻 This is the hands-on finale. Open the practice cells. Let them try first, drop hints as they get stuck.

**Setup — the messy data:**
```python
students = [
    {"name": "  Ada ",   "city": "Lagos",  "scores": [82, 91, 77]},
    {"name": "Babbage",  "city": "lagos",  "scores": [55, 60, 48]},
    {"name": "Hopper",   "city": "Abuja",  "scores": [90, 95, 88]},
    {"name": " turing ", "city": "Abuja",  "scores": [70, 65, 80]},
    {"name": "Lovelace", "city": "LAGOS",  "scores": [40, 52, 61]},
]
```

**Challenge 1 — Clean the names.** Strip spaces + capitalize → `"  ada "` becomes `"Ada"`.
> 💡 *Hint:* loop the list; use `.strip()` then `.capitalize()` (or `.title()`) on `s["name"]`.
> ✅ *Expected:* `['Ada', 'Babbage', 'Hopper', 'Turing', 'Lovelace']`

**Challenge 2 — Add an average.** Give each student an `"avg"` key = mean of `scores`, 1 decimal.
> 💡 *Hint:* `round(sum(s["scores"]) / len(s["scores"]), 1)`.

**Challenge 3 — Distinct cities.** Build a **set** of cities, normalized to title-case.
> 💡 *Hint:* `{ s["city"].title() for s in students }` — a set comprehension.
> ✅ *Expected:* `{'Lagos', 'Abuja'}`

**Challenge 4 — Top performers.** Names where `avg >= 75`, highest first.
> 💡 *Hint:* filter with a comprehension, then `sorted(..., key=..., reverse=True)`.
> ✅ *Expected:* `['Hopper', 'Ada']`

**Challenge 5 — Group by city.** Dict: city → list of names in that city.
> 💡 *Hint:* start with `by_city = {}`; use `by_city.setdefault(city, []).append(name)`.
> ✅ *Expected:* `{'Lagos': ['Ada', 'Babbage', 'Lovelace'], 'Abuja': ['Hopper', 'Turing']}`

**🌟 Stretch — Phase day-counts.** Given phase boundaries, count days per phase and confirm they sum to 45.
> 💡 *Hint:* track `prev = 0`; for each `(name, last_day)`, `count = last_day - prev`, then `prev = last_day`.
> ✅ *Expected total:* `45`

❓ **Wrap question:** "Notice we used *all four* structures — list, dict, set, comprehension — on ONE real problem. That's what real data work feels like."

😄 "Congratulations — you just did 'data cleaning,' which is officially 80% of every data/AI job. The other 20% is telling people you did data cleaning."

---

## 15. Recap & Homework

**Recap (rapid-fire, ask THEM to answer):**
- ❓ "What's the difference between `=` and `==`?"
- ❓ "Which structure removes duplicates automatically?"
- ❓ "How do you check if a number is even?"
- ❓ "What does a virtual environment give us?"

**Homework:**
- Finish any unsolved challenge cells in the notebook.
- Push the notebook to your **GitHub repo** (we'll formalize Git on Day 3).

**Tease Day 2:** "Tomorrow — **Python OOP & Advanced**: functions, classes, decorators, generators… and we build a small CLI project. It's where Python starts feeling powerful."

😄 "Same time tomorrow. Bring your laptop, your curiosity, and ideally the same enthusiasm — caffeine optional but historically effective."

---

**TARS Lab Academy — we don't watch, we ship.** 🚀
