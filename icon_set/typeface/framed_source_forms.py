"""Reuse the existing source-specific serif i and text-tool T, with their serifs intact."""
AUTHOR='gpt-6'
SOURCE_REFERENCES=(('3f358614-5fa8-4452-b0ea-706946b19adc','pictographic-primitives/state/information_3f358614-5fa8-4452-b0ea-706946b19adc.svg'),('c50b60b1-2dc6-4030-9b5e-382aaf24bf10','pictographic-primitives/state/circle text tool_c50b60b1-2dc6-4030-9b5e-382aaf24bf10.svg'))
def draw_information_serif(s):
    s.add_dot('dot',(32,18))
    s.add_polyline('stem',(26,28),(32,28),(32,46))
    s.add_line('foot',(26,46),(38,46));s.relate('connect','stem','foot')

def draw_text_tool_t(s):
    s.add_polyline('top',(18,24),(18,18),(46,18),(46,24))
    s.add_line('stem',(32,18),(32,46));s.add_line('foot',(26,46),(38,46))
    s.relate('connect','top','stem');s.relate('connect','stem','foot')

FRAMED_PROFILE_VARIANTS = {'letter-i-source-serif': {'parent_glyph': 'letter-i',
                           'character': 'i',
                           'profile': 'SUB32',
                           'stroke_width': 4,
                           'paths': ['M32 18L32 18',
                                     'M26 28L32 28L32 46',
                                     'M26 46L38 46'],
                           'svg_sha256': '713b4f70aacc7edf81ae8a93aebb2636e789d98516e9b55ea950d151d1206923',
                           'policy': 'Existing source-specific serif form '
                                     'reused unchanged, translated into the '
                                     'complete enclosing circle.'},
 'letter-t-source-serif': {'parent_glyph': 'letter-t-uppercase',
                           'character': 'T',
                           'profile': 'SUB32',
                           'stroke_width': 4,
                           'paths': ['M18 24L18 18L46 18L46 24',
                                     'M32 18L32 46',
                                     'M26 46L38 46'],
                           'svg_sha256': '1bccd63f4e7006f3f993c5fe9855f5783552c3b048ca2c672503b4ca9006c880',
                           'policy': 'Existing source-specific serif form '
                                     'reused unchanged, translated into the '
                                     'complete enclosing circle.'}}
