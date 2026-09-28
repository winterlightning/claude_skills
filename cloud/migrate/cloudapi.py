"""Shared helpers for the migration scripts: settings from cloud/.env and authorized requests."""
from __future__ import annotations

import json
import os
from pathlib import Path
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT / 'cloud' / '.env'


def settings() -> dict:
    """KEY=value lines of cloud/.env, overridden by the process environment."""
    values = {}
    if ENV_FILE.is_file():
        for line in ENV_FILE.read_text().splitlines():
            if '=' in line and not line.lstrip().startswith('#'):
                key, value = line.split('=', 1)
                values[key.strip()] = value.strip()
    values.update({k: v for k, v in os.environ.items() if k.startswith(('PICTOGRAPHIC_', 'CLOUDFLARE_'))})
    return values


def push_token(base_url: str) -> str:
    """The Worker's PUSH_TOKEN: the local dev one for localhost, the remote one otherwise."""
    config = settings()
    local = base_url.startswith(('http://127.0.0.1', 'http://localhost'))
    token = config.get('PICTOGRAPHIC_PUSH_TOKEN_LOCAL' if local else 'PICTOGRAPHIC_PUSH_TOKEN')
    if not token:
        raise SystemExit('error: no push token; set PICTOGRAPHIC_PUSH_TOKEN (remote) or PICTOGRAPHIC_PUSH_TOKEN_LOCAL in cloud/.env')
    return token


def request(base_url: str, method: str, path: str, *, body: bytes | None = None, content_type: str = 'application/json',
            token: str | None = None, timeout: float = 120) -> tuple[int, bytes]:
    # Cloudflare's bot filter refuses Python's default User-Agent (error 1010).
    headers = {'Content-Type': content_type, 'User-Agent': 'pictographic-migrate/1.0'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    req = urllib.request.Request(base_url.rstrip('/') + path, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as error:
        return error.code, error.read()


def post_json(base_url: str, path: str, payload, token: str | None = None) -> dict:
    status, content = request(base_url, 'POST', path, body=json.dumps(payload, ensure_ascii=False).encode('utf-8'), token=token)
    try:
        data = json.loads(content or b'{}')
    except ValueError:
        data = {'error': content[:200].decode('utf-8', 'replace')}
    if status >= 400:
        raise RuntimeError(f'POST {path} -> HTTP {status}: {data.get("error", data)}')
    return data
