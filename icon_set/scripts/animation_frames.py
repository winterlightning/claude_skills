"""Freeze an animated icon SVG at evenly spaced times and save the frames as one PNG strip.

    python3 icon_set/scripts/animation_frames.py ANIMATED.svg OUT.png [--duration 2.4] [--frames 12] [--size 96]

Every frame is the same SVG paused at ``t = i * duration / frames`` (CSS animations through the Web
Animations API, SMIL through ``setCurrentTime``), rendered by headless Chrome. Each frame has a red
canvas border, so anything drawn past the canvas edge shows as clipped against it. The last row repeats
the frames at native size to judge legibility. ``--duration`` defaults to the longest CSS animation or
SMIL ``dur`` found in the file. It also reports whether the file honours ``prefers-reduced-motion``.
"""
import argparse
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


def longest(text):
    times = [float(v) * (0.001 if unit == 'ms' else 1)
             for v, unit in re.findall(r'(?:animation(?:-duration)?\s*:[^;]*?|dur=")\s*([\d.]+)(ms|s)\b', text)]
    return max(times) if times else 2.0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('svg'); parser.add_argument('out')
    parser.add_argument('--duration', type=float, help='loop length in seconds (default: the longest found)')
    parser.add_argument('--frames', type=int, default=12)
    parser.add_argument('--size', type=int, default=96)
    parser.add_argument('--chrome', default=CHROME)
    args = parser.parse_args(argv)
    text = Path(args.svg).read_text()
    duration = args.duration or longest(text)
    body = re.sub(r'<\?xml[^>]*>', '', text)
    n, size = args.frames, args.size
    cells = ''.join(f'<div class="f big" data-t="{i * duration / n:.4f}">{body}<span>{i * duration / n:.2f}s</span></div>' for i in range(n))
    cells += ''.join(f'<div class="f small" data-t="{i * duration / n:.4f}">{body}</div>' for i in range(n))
    page = f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;padding:8px;background:#fff;font:11px Helvetica;display:grid;grid-template-columns:repeat({n},{size + 8}px);gap:6px 0}}
.f{{position:relative}} .f svg{{display:block;outline:1px solid #e33;color:#000;overflow:hidden}}
.big svg{{width:{size}px;height:{size}px}} .small svg{{width:48px;height:48px}}
span{{display:block;color:#666;margin-top:2px}}
</style></head><body>{cells}<script>
for (const f of document.querySelectorAll('.f')) {{
  const t = parseFloat(f.dataset.t), svg = f.querySelector('svg');
  if (svg.pauseAnimations) {{ svg.pauseAnimations(); svg.setCurrentTime(t); }}
  for (const a of f.getAnimations({{subtree: true}})) {{ a.pause(); a.currentTime = t * 1000; }}
}}
</script></body></html>'''
    with tempfile.TemporaryDirectory() as tmp:
        page_path = Path(tmp) / 'frames.html'
        page_path.write_text(page)
        width = 16 + n * (size + 8)
        height = 16 + size + 20 + 6 + 48 + 8
        result = subprocess.run([args.chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--virtual-time-budget=500',
                                 f'--window-size={width},{height}', f'--screenshot={Path(args.out).resolve()}', page_path.as_uri()],
                                capture_output=True, text=True)
        if result.returncode != 0 or not Path(args.out).is_file():
            sys.exit(f'chrome failed: {result.stderr.strip()[-500:]}')
    reduced = 'prefers-reduced-motion' in text
    print(f'wrote {args.out}  ({n} frames over {duration:g}s; top row {size}px, bottom row native 48px)')
    if not reduced:
        print('  WARNING: no prefers-reduced-motion rule: the icon keeps moving for viewers who asked for less motion')


if __name__ == '__main__':
    main()
