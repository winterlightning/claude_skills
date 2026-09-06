#!/usr/bin/env python3
"""Manage the repository's icon profile JSON through a local browser app.

Run without arguments to open the manager. --validate PATH checks a candidate
configuration without writing anything. The server only binds to loopback;
saves require its session token and the revision returned by the latest read.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
import os
from pathlib import Path
import secrets
import tempfile
import threading
from urllib.parse import unquote, urlsplit
import webbrowser


ROOT = Path(__file__).resolve().parent.parent
MAX_BODY_BYTES = 1024 * 1024
UNCHECKED = object()


class RevisionConflict(ValueError):
    """The source changed after the client loaded it."""


def validated_configuration(source: object) -> dict:
    # Lazy imports let --help and the server entry point report invalid local
    # configurations normally instead of exposing an import-time traceback.
    from icon_profiles import validate_profile_source
    return validate_profile_source(source)


def configuration_assets(source: dict, root: Path) -> dict[Path, str]:
    from generate_profile_assets import profile_asset_contents
    return profile_asset_contents(source, root=root)


def configuration_envelope(source: dict, revision: str) -> dict:
    from icon_profiles import resolve_profiles
    return {"configuration": source, "revision": revision,
            "resolvedProfiles": resolve_profiles(source)}


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


class ProfileStore:
    """A bounded JSON-and-generated-mirrors transaction, never an icon editor."""

    def __init__(self, root: Path = ROOT):
        self.root = root.resolve()
        self.configuration_path = self.root / "core/icon_profiles.json"
        self.lock = threading.RLock()

    def checked_path(self, path: Path) -> Path:
        path = Path(os.path.abspath(path))
        if not path.is_relative_to(self.root) or path == self.root:
            raise ValueError("Profile save target must stay inside this repository")
        for item in (path, *path.parents):
            if item == self.root:
                break
            if item.is_symlink():
                raise ValueError(f"Profile files and directories must not be symlinks: {item.relative_to(self.root)}")
        if path.exists() and not path.is_file():
            raise ValueError(f"Profile file target is not a regular file: {path.relative_to(self.root)}")
        return path

    def _source(self) -> tuple[dict, bytes]:
        content = self.checked_path(self.configuration_path).read_bytes()
        try:
            source = json.loads(content)
        except (ValueError, UnicodeError) as error:
            raise ValueError(f"Cannot parse core/icon_profiles.json: {error}") from error
        return validated_configuration(source), content

    def read(self) -> dict:
        with self.lock:
            source, content = self._source()
            return configuration_envelope(source, digest(content))

    def atomic_write(self, path: Path, content: bytes, *, expected: bytes | None | object = UNCHECKED) -> None:
        path = self.checked_path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        staged = None
        try:
            with tempfile.NamedTemporaryFile(prefix=".profile-save-", dir=path.parent, delete=False) as output:
                staged = Path(output.name)
                output.write(content)
                output.flush()
                os.fsync(output.fileno())
            if path.exists():
                os.chmod(staged, path.stat().st_mode & 0o777)
            self.checked_path(path)
            # Check again after staging/fsync, immediately before replacement.
            # The advisory transaction lock covers other manager instances;
            # this also catches ordinary edits made by an external editor.
            if expected is not UNCHECKED and (path.read_bytes() if path.exists() else None) != expected:
                raise RevisionConflict(f"{path.relative_to(self.root)} changed while its replacement was staged. Reload before saving.")
            os.replace(staged, path)
        finally:
            if staged is not None and staged.exists():
                staged.unlink()

    def save(self, configuration: object, revision: str) -> dict:
        if not isinstance(revision, str) or len(revision) != 64:
            raise RevisionConflict("Load the current configuration before saving")
        source = validated_configuration(configuration)
        # Resolve and render all generated files before touching the source.
        assets = configuration_assets(source, self.root)
        targets = {self.configuration_path: json_bytes(source),
                   **{path: content.encode("utf-8") for path, content in assets.items()}}
        for path in targets:
            self.checked_path(path)
        with self.lock:
            # An advisory lock also serializes saves from two manager instances.
            import fcntl
            lock_path = self.checked_path(self.root / "work/.profile-manager.lock")
            lock_path.parent.mkdir(parents=True, exist_ok=True)
            with lock_path.open("a+b") as lock_file:
                fcntl.flock(lock_file, fcntl.LOCK_EX)
                return self._save_locked(source, revision, targets)

    def _save_locked(self, source: dict, revision: str, targets: dict[Path, bytes]) -> dict:
        _, current = self._source()
        if digest(current) != revision:
            raise RevisionConflict("The profile JSON changed since you loaded it. Reload before saving; your draft has not been written.")
        previous = {path: path.read_bytes() if path.exists() else None for path in targets}
        changed = {path: content for path, content in targets.items() if previous[path] != content}
        if not changed:
            return {**configuration_envelope(source, revision), "savedPaths": [], "backupDirectory": None}

        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ") + "-" + secrets.token_hex(3)
        backup = self.root / "work/profile-config-backups" / stamp
        backup_manifest = []
        for path, content in changed.items():
            relative = str(path.relative_to(self.root))
            old = previous[path]
            if old is not None:
                self.atomic_write(backup / relative, old)
            backup_manifest.append({"path": relative, "existed": old is not None,
                                    "sha256": digest(old) if old is not None else None})
        self.atomic_write(backup / "manifest.json", json_bytes({"previousRevision": revision, "files": backup_manifest}))

        written = []
        try:
            if digest(self.configuration_path.read_bytes()) != revision:
                raise RevisionConflict("The profile JSON changed during save preparation. Reload before saving.")
            for path, content in changed.items():
                self.checked_path(path)
                if (path.read_bytes() if path.exists() else None) != previous[path]:
                    raise RevisionConflict(f"{path.relative_to(self.root)} changed during save preparation. Reload before saving.")
                self.atomic_write(path, content, expected=previous[path])
                written.append(path)
            # Do not report a successful revision if an external editor changed
            # an earlier file while the remaining mirrors were being written.
            for path, content in targets.items():
                self.checked_path(path)
                if not path.exists() or path.read_bytes() != content:
                    raise RevisionConflict(f"{path.relative_to(self.root)} changed during the save. Reload before saving again.")
        except Exception as error:
            rollback_errors = []
            for path in reversed(written):
                try:
                    self.checked_path(path)
                    if not path.exists() or path.read_bytes() != changed[path]:
                        raise ValueError("file was changed by another editor; its new contents were preserved")
                    if previous[path] is None:
                        path.unlink()
                    else:
                        self.atomic_write(path, previous[path], expected=changed[path])
                except Exception as rollback_error:
                    rollback_errors.append(f"{path.relative_to(self.root)}: {rollback_error}")
            if rollback_errors:
                raise OSError(f"Save failed: {error}. Restore from {backup}; rollback could not restore: {'; '.join(rollback_errors)}") from error
            raise
        return {**configuration_envelope(source, digest(targets[self.configuration_path])),
                "savedPaths": [str(path.relative_to(self.root)) for path in changed],
                "backupDirectory": str(backup.relative_to(self.root))}


def make_server(store: ProfileStore, port: int = 8765, token: str | None = None) -> ThreadingHTTPServer:
    session_token = token or secrets.token_urlsafe(32)

    class Handler(BaseHTTPRequestHandler):
        server_version = "IconProfileManager/1"

        def log_message(self, format, *args):
            # Avoid logging the bearer token carried by the initial launch URL.
            pass

        def respond(self, status: int, content: bytes, content_type: str) -> None:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("Referrer-Policy", "no-referrer")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'")
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(content)

        def json_response(self, status: int, value: object) -> None:
            self.respond(status, json_bytes(value), "application/json; charset=utf-8")

        def trusted_request(self, api: bool = False) -> bool:
            hosts = {f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}
            host = self.headers.get("Host", "")
            origin = self.headers.get("Origin")
            if host not in hosts or (origin is not None and origin != f"http://{host}"):
                self.json_response(403, {"error": "Only same-origin loopback requests are accepted"})
                return False
            if api and not secrets.compare_digest(self.headers.get("X-Profile-Token", "").encode("utf-8"), session_token.encode("utf-8")):
                self.json_response(403, {"error": "Open the manager using the session URL printed by its launcher"})
                return False
            return True

        def do_GET(self):
            path = unquote(urlsplit(self.path).path)
            if not self.trusted_request(api=path == "/api/profiles"):
                return
            try:
                if path == "/api/profiles":
                    self.json_response(200, store.read())
                    return
                if path == "/":
                    target = store.root / "frontend/profiles.html"
                elif path.startswith(("/js/", "/css/")):
                    target = store.root / "frontend" / path.lstrip("/")
                    if not target.resolve().is_relative_to(store.root / "frontend"):
                        raise FileNotFoundError
                elif path.startswith("/docs/"):
                    target = store.root / path.lstrip("/")
                    if target.suffix != ".md" or not target.resolve().is_relative_to(store.root / "docs"):
                        raise FileNotFoundError
                else:
                    raise FileNotFoundError
                store.checked_path(target)
                content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
                if target.suffix in {".js", ".css", ".html", ".md"}:
                    content_type += "; charset=utf-8"
                self.respond(200, target.read_bytes(), content_type)
            except FileNotFoundError:
                self.json_response(404, {"error": "Not found"})
            except (ValueError, OSError) as error:
                self.json_response(400, {"error": str(error)})

        def do_PUT(self):
            if urlsplit(self.path).path != "/api/profiles":
                self.json_response(404, {"error": "Not found"})
                return
            if not self.trusted_request(api=True):
                return
            if self.headers.get_content_type() != "application/json":
                self.json_response(415, {"error": "Send application/json"})
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if length < 1 or length > MAX_BODY_BYTES or self.headers.get("Transfer-Encoding"):
                    raise ValueError("Send a JSON request between 1 byte and 1 MB with Content-Length")
                payload = json.loads(self.rfile.read(length))
                if not isinstance(payload, dict) or set(payload) != {"configuration", "revision"}:
                    raise ValueError("Expected configuration and revision fields")
                self.json_response(200, store.save(payload["configuration"], payload["revision"]))
            except RevisionConflict as error:
                self.json_response(409, {"error": str(error)})
            except (ValueError, UnicodeError) as error:
                self.json_response(400, {"error": str(error)})
            except OSError as error:
                self.json_response(500, {"error": f"Profile save failed; no icon files were changed. {error}"})

        def do_OPTIONS(self):
            self.json_response(403, {"error": "Cross-origin requests are not supported"})

    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.daemon_threads = True
    server.session_token = session_token
    return server


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765, help="loopback HTTP port (default: 8765)")
    parser.add_argument("--no-open", action="store_true", help="print the URL without launching a browser")
    parser.add_argument("--validate", type=Path, metavar="PATH", help="validate candidate profile JSON without writing files")
    args = parser.parse_args()
    if not 0 <= args.port <= 65535:
        parser.error("--port must be between 0 and 65535 (0 chooses a free port)")
    try:
        if args.validate:
            source = validated_configuration(json.loads(args.validate.read_text(encoding="utf-8")))
            print(f"Valid profile configuration: {len(source['profiles'])} types; default {source['defaultIconType']}")
            return 0
        store = ProfileStore()
        store.read()
        server = make_server(store, args.port)
        url = f"http://127.0.0.1:{server.server_port}/?token={server.session_token}"
        print(f"Icon Profile Manager: {url}", flush=True)
        print("Edits save to core/icon_profiles.json and generated mirrors. Ctrl-C stops the server.", flush=True)
        if not args.no_open:
            webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.server_close()
        return 0
    except (ValueError, OSError) as error:
        parser.exit(1, f"Profile manager error: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
