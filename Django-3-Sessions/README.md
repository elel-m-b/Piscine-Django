# Training Python-Django - 3 Sessions — "Life Pro Tips"

This is a **single, merged Django project** that implements **all 7
exercises** of the "Training Python-Django - 3 Sessions" subject together,
as one working website. Every feature from Exercise 00 through Exercise 06
is active at the same time.

If you're new to Django, don't worry — this README explains everything step
by step, from installing Python to understanding what each feature does and
how to test it.

---

## 📁 Project structure

```
ex/
├── manage.py             → the command-line tool you use to run Django
├── requirements.txt       → the exact Python packages needed
├── lpt_site/               → project-wide settings, URLs
│   ├── settings.py           → RANDOM_NAMES, AUTH_USER_MODEL, apps, etc.
│   ├── urls.py
│   └── ...
├── accounts/                → custom user app (username + reputation)
│   ├── models.py               → the custom User model
│   ├── signals.py               → automatic reputation & permission logic
│   └── admin.py
├── tips/                    → the main "tips" app
│   ├── models.py               → the Tip model (content, author, date, votes)
│   ├── views.py                 → home, register, login, logout, vote, delete
│   ├── forms.py                  → RegistrationForm, LoginForm, TipForm
│   ├── urls.py
│   ├── context_processors.py      → the 42-second anonymous name logic
│   └── admin.py
└── templates/                → all HTML pages (Bootstrap 5 styled)
```

This is exactly the same code as the final, most advanced stage of the
project — every exercise's functionality is present and working together in
this one `ex/` folder, with no separate sub-folders to juggle.

---

## ✅ Prerequisites

You only need three things installed on your computer:

1. **Python 3** (3.10 or newer recommended). Check with:
   ```bash
   python3 --version
   ```
2. **pip** (Python's package installer, usually bundled with Python).
3. A terminal / command prompt.

### About the versions used

* **Django 5.2** — the current **LTS (Long Term Support)** version, as
  required by the subject.
* **django-bootstrap5** — a small helper library that renders Bootstrap 5
  styling around Django forms so pages look clean without writing HTML for
  every field by hand.

Both are pinned in `requirements.txt` so your results match this README.

---

## 🚀 How to run the project

```bash
cd ex

# 1. Create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create the database tables
python3 manage.py migrate

# 4. (Optional but recommended) create an admin account
python3 manage.py createsuperuser

# 5. Run the server
python3 manage.py runserver
```

Then open your browser at **http://127.0.0.1:8000/**.
The admin site is at **http://127.0.0.1:8000/admin/**.

Stop the server anytime with `Ctrl + C`.

> ⚠️ **Important:** this project uses a **custom user model**
> (`AUTH_USER_MODEL`). That setting must be in place *before* the very first
> `migrate` — which it already is here. If you ever copy this project and
> change the user model afterwards, you'll need to reset the database and
> migrations, since Django can't swap the user model on an existing
> database.

---

## 📖 What each exercise added (and how to test it here)

Since everything is merged, here's a guide to trying out each piece of
functionality inside this single project.

### Exercise 00 — Anonymous sessions
Visit the homepage while logged out. The `<nav>` bar greets you with
`Hello <RandomName>!`, using one of 10 names defined in `RANDOM_NAMES`
(`lpt_site/settings.py`). This name is tied to your browser session and
stays the same for **42 seconds** (`ANONYMOUS_NAME_VALIDITY`), then
automatically changes on your next page load. Refresh a few times quickly
to see it stay put, then wait 42+ seconds and refresh again to see it
change.

### Exercise 01 — User creation
Click **Register** in the nav bar to create an account (username, password,
password confirmation — with full validation), or **Log in** if you already
have one. Once logged in, the nav bar shows your username instead of the
random name, and a **Log out** link appears. Logged-in users are redirected
away if they try to visit `/register/` or `/login/` directly.

### Exercise 02 — Our Tips!
While logged in, you'll see a form on the homepage to post a new tip
(saved with your username and the current date/time automatically).
Logged-out visitors see the list of tips but no posting form.

### Exercise 03 — Votes
Every tip has ▲ upvote and ▼ downvote buttons plus a Delete button
(logged-in users only). Click a vote button again to cancel your vote;
switching from ▲ to ▼ (or vice versa) replaces your vote rather than
stacking both. Counts are always accurate because votes are tracked as
actual user relationships, not simple counters.

### Exercise 04 — Built-in permissions
By default, only a tip's own author can delete it. Go to `/admin/`
(log in as your superuser), open a test user, and add the
**"tips | tip | Can delete tip"** permission under **User permissions**.
That user can now delete *any* tip, and the Delete button appears
everywhere for them.

### Exercise 05 — Custom permission
Same idea, but for downvoting: only a tip's author can downvote their own
tip by default. In `/admin/`, grant a user **"tips | tip | Can downvote
tip"** to unlock the ▼ button on everyone else's tips too.

### Exercise 06 — Reputation system
This is the exercise that ties everything together, and it's fully
automatic — no admin work needed:
* Every upvote your tips receive gives you **+5 reputation**.
* Every downvote gives you **−2 reputation**.
* Deleting a tip removes the influence of its votes on your reputation.
* At **15 reputation**, you automatically gain the downvote permission
  (Exercise 05).
* At **30 reputation**, you automatically gain the delete permission
  (Exercise 04).
* If your reputation drops back below a threshold, that permission is
  automatically revoked.

Your reputation is shown in brackets everywhere your username appears,
e.g. `Hello alice (23)!`

**To test it:** register a few accounts (e.g. `author`, `voter1`,
`voter2`, `voter3`). Log in as `author` and post a tip. Then log in as
each voter (private/incognito windows work well) and upvote it. After 3
upvotes, `author` reaches 15 reputation — log back in as `author` and
confirm the downvote button now appears on other users' tips. Get 3 more
upvotes on a second tip (30 total reputation) and confirm the delete
button unlocks too. Delete that tip and watch the reputation — and
permissions — automatically drop back down.

---

## 💡 Tips & common mistakes to avoid

* **Never** create users with `User.objects.create()` — always use
  `User.objects.create_user()`, which properly hashes the password.
* Votes use `ManyToManyField`s (`upvoters`, `downvoters`) instead of simple
  counters — this guarantees the count is always accurate and makes
  toggling/switching a vote trivial and bug-free.
* Permission checks always happen **in the view**, not just by hiding a
  button in the template — a hidden button alone wouldn't stop someone from
  calling the URL directly.
* `has_perm()` results are cached per Python object during a single
  request/session — a non-issue in normal browsing (each page load gets a
  fresh user object), but worth knowing if you ever test permission changes
  inside a single Django shell session.
* If you edit `models.py`, remember to run
  `python3 manage.py makemigrations` followed by `python3 manage.py migrate`
  again before your changes take effect in the database.

---

## ❓ Troubleshooting

| Problem | Likely cause / fix |
|---|---|
| `python3: command not found` | Try `python` instead, or install Python 3. |
| `ModuleNotFoundError: No module named 'django'` | Activate your virtual environment and run `pip install -r requirements.txt`. |
| Page styling looks broken / no Bootstrap | Make sure you're online — `django-bootstrap5` loads Bootstrap's CSS/JS from a CDN. |
| `django.db.utils.OperationalError: no such table` | Run `python3 manage.py migrate`. |
| Model changes don't show up | Run `python3 manage.py makemigrations` then `python3 manage.py migrate`. |
| A feature seems locked when it shouldn't be | Check the user's reputation and permissions in `/admin/`; a normal browser refresh always reflects the current state. |

Happy hacking, and good luck with your Django training! 🐍
