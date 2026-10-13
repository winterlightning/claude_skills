"""Draw the official punctuation glyphs (colon, period, percent, question mark, plus, degree) on the capitals'
19 x 19 canvas: cap line y 2, x-height y 7, baseline y 17, stroke 4, glyph axis x 9 like the digits.

    python3 Letters/official/source/punctuation.py   ->  Letters/official/punctuation/<name>.svg

Construction
- Dots are zero-length round strokes (4 units of ink), as the i and j dots are.
- period: one dot on the baseline. colon: dots on the x-height and the baseline (6 units of white).
- question mark: the 2's top bowl (same curve, x 5 to 13), turning back down to a short stem at x 10 that stops
  6 above the baseline dot (2 units of white, like the i dot). Ending the stem on the axis (x 9) leaves only 3.1
  units of white to the bowl, so it stays 1 to the right.
- percent: the slash runs cap line to baseline over the O's width (x 4 to 14); one dot in each open corner, just
  outside that width (x 3 and 15), so each keeps 4 units of white to the slash.
- plus: 8 by 8 centred on the middle of the x-height band (y 10), the size of a lowercase letter.
- degree: a ring hanging from the cap line, radius 4 (y 2 to 10), so 4 units of white inside.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / 'punctuation'
HEAD = '<svg width="19" height="19" viewBox="0 0 19 19" fill="none" xmlns="http://www.w3.org/2000/svg">\n'
STYLE = 'stroke="black" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"'
AXIS, CAP, XH, BASE = 9, 2, 7, 17


def path(d):
    return f'<path d="{d}" {STYLE}/>\n'


def dot(x, y):
    return path(f'M{x:g} {y:g}L{x:g} {y:g}')


GLYPHS = {
    'period': dot(AXIS, BASE),
    'colon': dot(AXIS, XH) + dot(AXIS, BASE),
    'question': path('M5 6C5 3.79 6.79 2 9 2C11.21 2 13 3.79 13 6C13 8.2 11 9.3 10 10.5V11') + dot(AXIS, BASE),
    'percent': path('M14 2L4 17') + dot(3, 4) + dot(15, 15),
    'plus': path('M5 10H13') + path('M9 6V14'),
    'degree': f'<circle cx="{AXIS}" cy="6" r="4" {STYLE}/>\n',
}
# The character each file stands for (file names stay plain on every file system).
CHARACTERS = {'period': '.', 'colon': ':', 'question': '?', 'percent': '%', 'plus': '+', 'degree': '°'}

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    for name, body in GLYPHS.items():
        (OUT / f'{name}.svg').write_text(HEAD + body + '</svg>\n')
    print('wrote', ', '.join(GLYPHS), 'to', OUT)
