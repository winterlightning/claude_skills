"""Run one combination refresh at a time, independently of browser requests."""
import os
import json
import subprocess
import sys
import tempfile
import threading
from collections import deque
from .category_report import REPO_ROOT

_lock = threading.Lock()
_state = {'status': 'idle', 'message': ''}


def status():
    with _lock:
        return dict(_state)


def _run(plan):
    try:
        # A fresh process discovers models added since the gallery server started.
        with tempfile.TemporaryDirectory(prefix='side-combine-') as temp:
            path = os.path.join(temp, 'approved.json')
            with open(path, 'w') as output:
                json.dump(plan, output)
            with subprocess.Popen(
                [os.environ.get('PICTOGRAPHIC_COMBINE_PYTHON', sys.executable), '-u',
                 '-m', 'icon_set.scripts.refresh_combination_pairs', '--previews',
                 '--approved-plan', path],
                cwd=REPO_ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True,
            ) as process:
                recent = deque(maxlen=12)
                for line in process.stdout:
                    line = line.strip()
                    if line:
                        recent.append(line)
                    if line.startswith(('Available:', 'Prepared ', 'Published ')):
                        with _lock:
                            _state['message'] = line
                if process.wait():
                    raise RuntimeError('Refresh failed: ' + ' | '.join(recent)[-1200:])
        with _lock:
            _state['status'] = 'complete'
    except Exception as error:
        with _lock:
            _state.update(status='error', message=str(error))


def start(plan):
    with _lock:
        if _state['status'] != 'running':
            if not plan:
                raise ValueError('No side pairs have both an approved main and an approved sub.')
            _state.update(status='running', message=f'Combining {len(plan)} approved side pairs…',
                          planned_count=len(plan))
            threading.Thread(target=_run, args=(plan,), daemon=True).start()
        return dict(_state)
