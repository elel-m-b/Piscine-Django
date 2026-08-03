from datetime import datetime

from django.conf import settings
from django.shortcuts import render, redirect

from .forms import InputForm

LOGS_FILE = settings.EX02_LOGS_FILE
TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'
SEPARATOR = ' | '


def _read_history():
    """Read every past submission from the logs file.

    Returns a list of dicts (timestamp, text), oldest first. If the file
    does not exist yet (no submission has ever been made), an empty list
    is returned -- the history simply starts empty, as required.
    """
    history = []
    if LOGS_FILE.exists():
        with open(LOGS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n')
                if not line:
                    continue
                timestamp, _, text = line.partition(SEPARATOR)
                history.append({'timestamp': timestamp, 'text': text})
    return history


def _append_entry(text):
    """Append one 'timestamp | text' line to the logs file.

    The file is created automatically the first time an entry is
    submitted, and every entry is written straight to disk so the data
    survives a development-server restart.
    """
    LOGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
    with open(LOGS_FILE, 'a', encoding='utf-8') as f:
        f.write(f'{timestamp}{SEPARATOR}{text}\n')


def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            _append_entry(form.cleaned_data['user_input'])
            # Redirect after POST (PRG pattern) so a page refresh does not
            # resubmit the form.
            return redirect('ex02-index')
    else:
        form = InputForm()

    context = {
        'page_title': 'Ex02: First Form',
        'form': form,
        'history': _read_history(),
    }
    return render(request, 'ex02/index.html', context)
