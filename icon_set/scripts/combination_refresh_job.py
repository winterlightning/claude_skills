"""Run one combination refresh at a time, independently of browser requests."""
import os
import subprocess
import sys
import threading
from .category_report import REPO_ROOT

_lock = threading.Lock()
_state = {'status': 'idle', 'message': ''}


def status():
    with _lock:
        return dict(_state)


def _run():
    try:
        # A fresh process discovers models added since the gallery server started.
        with subprocess.Popen(
            [os.environ.get('PICTOGRAPHIC_COMBINE_PYTHON', sys.executable), '-u',
             '-m', 'icon_set.scripts.refresh_combination_pairs', '--previews'],
            cwd=REPO_ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True,
        ) as process:
            for line in process.stdout:
                line = line.strip()
                if line.startswith(('Available:', 'Prepared ', 'Published ')):
                    with _lock:
                        _state['message'] = line
            if process.wait():
                raise RuntimeError('Refresh failed. Check the exported SVGs and try again.')
        with _lock:
            _state['status'] = 'complete'
    except Exception as error:
        with _lock:
            _state.update(status='error', message=str(error))


def start():
    with _lock:
        if _state['status'] != 'running':
            _state.update(status='running', message='Scanning generated icons…')
            threading.Thread(target=_run, daemon=True).start()
        return dict(_state)
