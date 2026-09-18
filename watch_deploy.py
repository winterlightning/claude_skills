#!/usr/bin/env python3
"""Watch the git remote and restart the deploy server whenever new commits land.

    python3 watch_deploy.py --development        # dedicated clean development checkout
    python3 watch_deploy.py --development --interval 15
    python3 watch_deploy.py -- --production --dist /srv/releases/one --database /srv/state/feedback.sqlite3

Runs `git pull --ff-only` on each new update, then relaunches deploy.py.
"""
from __future__ import annotations

import argparse
import os
import signal
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent
DEFAULT_DEPLOY = REPO / "icon_set" / "scripts" / "deploy.py"


def log(msg: str) -> None:
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}", flush=True)


def git(*args: str, check: bool = True) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=REPO, capture_output=True, text=True, check=False
    )
    if check and proc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout.strip()


class Deployment:
    """The deploy.py child process, run in its own process group."""

    def __init__(self, cmd: list[str]) -> None:
        self.cmd = cmd
        self.proc: subprocess.Popen | None = None

    def start(self) -> None:
        log(f"starting: {' '.join(self.cmd)}")
        self.proc = subprocess.Popen(self.cmd, cwd=REPO, start_new_session=True)

    def stop(self, timeout: float = 10.0) -> None:
        if self.proc is None or self.proc.poll() is not None:
            return
        log(f"stopping pid {self.proc.pid}")
        try:
            os.killpg(self.proc.pid, signal.SIGTERM)
        except ProcessLookupError:
            return
        try:
            self.proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            log("did not exit in time, sending SIGKILL")
            try:
                os.killpg(self.proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            self.proc.wait()

    def restart(self) -> None:
        self.stop()
        self.start()

    def died(self) -> bool:
        return self.proc is not None and self.proc.poll() is not None


def remote_head(remote: str, branch: str) -> str:
    git("fetch", "--quiet", remote, branch)
    return git("rev-parse", f"{remote}/{branch}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--development", action="store_true", help="Explicitly allow a development server; never use the active agent checkout")
    ap.add_argument("--interval", type=float, default=60.0, help="seconds between polls (default: 60)")
    ap.add_argument("--remote", default="origin", help="remote to watch (default: origin)")
    ap.add_argument("--branch", default=None, help="branch to watch (default: current branch)")
    ap.add_argument("--deploy", default=str(DEFAULT_DEPLOY), help="path to deploy.py")
    ap.add_argument("--python", default=sys.executable, help="interpreter used to run deploy.py")
    ap.add_argument("--no-restart-on-crash", action="store_true", help="do not relaunch if deploy.py exits on its own")
    ap.add_argument("deploy_args", nargs=argparse.REMAINDER, help="args after -- are passed to deploy.py")
    args = ap.parse_args()

    extra = args.deploy_args
    if extra and extra[0] == "--":
        extra = extra[1:]

    if not args.development and '--production' not in extra:
        ap.error('Pass -- --production --dist RELEASE --database STATE_DB, or explicitly opt in with --development.')
    if git('status', '--porcelain', '--untracked-files=no'):
        log('Refusing to auto-pull into a dirty checkout. Use a dedicated clean deployment checkout.')
        return 1

    branch = args.branch or git("rev-parse", "--abbrev-ref", "HEAD")
    if branch == "HEAD":
        log("detached HEAD; pass --branch explicitly")
        return 1

    deploy = Deployment([args.python, args.deploy, *extra])
    stopping = False

    def shutdown(signum, _frame):
        nonlocal stopping
        stopping = True
        log(f"received signal {signum}, shutting down")

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    local = git("rev-parse", "HEAD")
    log(f"watching {args.remote}/{branch} every {args.interval:g}s (at {local[:8]})")
    deploy.start()

    try:
        while not stopping:
            # Sleep in small slices so a signal is noticed promptly.
            waited = 0.0
            while waited < args.interval and not stopping:
                time.sleep(min(1.0, args.interval - waited))
                waited += 1.0
            if stopping:
                break

            if deploy.died() and not args.no_restart_on_crash:
                log(f"deploy.py exited with code {deploy.proc.returncode}; relaunching")
                deploy.start()

            try:
                remote = remote_head(args.remote, branch)
            except RuntimeError as exc:
                log(f"fetch failed, will retry: {exc}")
                continue

            local = git("rev-parse", "HEAD")
            if remote == local:
                continue

            if git('status', '--porcelain', '--untracked-files=no'):
                log('Checkout changed locally; skipping code update until it is clean.')
                continue
            log(f"new update {local[:8]} -> {remote[:8]}")
            pull = subprocess.run(
                ["git", "pull", "--ff-only", args.remote, branch],
                cwd=REPO, capture_output=True, text=True,
            )
            if pull.returncode != 0:
                log(f"pull failed, keeping current deployment: {pull.stderr.strip()}")
                continue

            log(git("log", "-1", "--pretty=%h %s", "HEAD"))
            deploy.restart()
    finally:
        deploy.stop()
        log("watcher stopped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
