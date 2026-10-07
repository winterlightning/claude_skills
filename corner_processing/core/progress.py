#!/usr/bin/env python3
"""core/progress.py — lightweight per-file progress for the pipeline stages.

Used by core/detect.py / core/toggle.py so a run.sh run shows how far along each
stage is and when it will finish.

On a TTY: an in-place bar with count, percent, elapsed and ETA plus the file
currently being processed. When output is piped/logged (no TTY): one plain
line every ~5% so logs stay readable. Everything goes to stderr — the stages'
own summaries and failure lists stay clean on stdout.
"""
import sys
import time


def _fmt(seconds):
    seconds = max(0, int(seconds))
    if seconds >= 3600:
        return f"{seconds // 3600}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}"
    return f"{seconds // 60}:{seconds % 60:02d}"


class Progress:
    """prog = Progress("roundable", len(paths)); prog.step(name) per file; prog.done()."""

    BAR = 28          # bar width (chars)
    THROTTLE = 0.1    # s — max TTY redraw rate
    LOG_EVERY = 5.0   # % — non-TTY line interval

    def __init__(self, label, total, stream=None):
        self.label = label
        self.total = total
        self.n = 0
        self.t0 = time.time()
        self.stream = stream if stream is not None else sys.stderr
        try:
            self.tty = self.stream.isatty()
        except Exception:
            self.tty = False
        self._last_draw = 0.0
        self._last_pct = 0.0
        self._width = 0

    def step(self, item=""):
        """Call once per file, when starting it (the bar shows the file in work)."""
        self.n += 1
        if self.total <= 0:
            return
        now = time.time()
        pct = 100.0 * self.n / self.total
        if self.tty:
            if now - self._last_draw < self.THROTTLE and self.n < self.total:
                return
            self._last_draw = now
            fill = int(self.BAR * self.n / self.total)
            elapsed = now - self.t0
            eta = elapsed / self.n * (self.total - self.n)
            name = item if len(item) <= 36 else item[:35] + "…"
            line = (f"  [{'#' * fill}{'-' * (self.BAR - fill)}] "
                    f"{self.n}/{self.total} ({pct:.0f}%) "
                    f"elapsed {_fmt(elapsed)} eta {_fmt(eta)}  {name}")
            self._width = max(self._width, len(line))
            self.stream.write("\r" + line.ljust(self._width))
        else:
            if pct - self._last_pct >= self.LOG_EVERY or self.n == self.total:
                self._last_pct = pct
                self.stream.write(f"  {self.label}: {self.n}/{self.total} ({pct:.0f}%), "
                                  f"eta {_fmt((now - self.t0) / self.n * (self.total - self.n))}\n")
        self.stream.flush()

    def done(self):
        """Clear the bar and print one closing line with the total elapsed time."""
        if self.tty and self._width:
            self.stream.write("\r" + " " * self._width + "\r")
        self.stream.write(f"  {self.label}: {self.n} files in {_fmt(time.time() - self.t0)}\n")
        self.stream.flush()
