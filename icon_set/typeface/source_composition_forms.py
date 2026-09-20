"""Shared source-specific letterforms for complete original compositions.

The primary typeface glyphs remain unchanged. These explicitly named variants
preserve the plain I, sloping M and round O/curved 2 in their source artwork.
"""
AUTHOR = 'gpt-6'
def draw_plain_i(s):
    s.add_line('plain-i',(36,16),(36,34))
def draw_sloping_m(s):
    s.add_polyline('sloping-m',(35,41),(39,23),(43,37),(47,23),(51,41))
def draw_oxygen(s):
    s.add_arc('o-top',(13,27),(33,27),radius_x=10)
    s.add_arc('o-bottom',(33,27),(13,27),radius_x=10)
    s.add_contour('o','o-top','o-bottom',closed=True)
    s.add_bezier('two-head',(40,30),((44,25),(51,29),(49,34)))
    s.add_polyline('two-foot',(49,34),(40,44),(50,44))
    s.relate('connect','two-head','two-foot')

SOURCE_COMPOSITION_VARIANTS = {
 'letter-i-source-plain': dict(parent_glyph='letter-i-uppercase',character='I',profile='SUB32',stroke_width=4,paths=['M36 16L36 34']),
 'letter-m-source-sloping': dict(parent_glyph='letter-m-uppercase',character='M',profile='SUB32',stroke_width=4,paths=['M35 41L39 23L43 37L47 23L51 41']),
 'letter-o-source-round': dict(parent_glyph='letter-o-uppercase',character='O',profile='SUB32',stroke_width=4,paths=['M13 27A10 10 0 0 1 33 27A10 10 0 0 1 13 27Z']),
 'digit-2-source-curved': dict(parent_glyph='digit-2',character='2',profile='SUB32',stroke_width=4,paths=['M40 30C44 25 51 29 49 34L40 44L50 44']),
}
for record in SOURCE_COMPOSITION_VARIANTS.values():
    record['policy']='Source-specific shared profile form; preferred natural glyph unchanged.'

def draw_bitcoin_serifs(s):
    """Source left-hand terminals, attached to the existing shared bitcoin body."""
    s.add_line('bitcoin-top-serif',(19,20),(22,20))
    s.add_line('bitcoin-bottom-serif',(19,38),(22,38))
    s.relate('connect','bitcoin-top-serif','glyph-path-1-1')
    s.relate('connect','bitcoin-bottom-serif','glyph-path-1-1')
    s.relate('connect','bitcoin-bottom-serif','glyph-path-2-1')

SOURCE_COMPOSITION_VARIANTS['symbol-bitcoin-source-serifs'] = dict(
    parent_glyph='symbol-bitcoin', character='₿', profile='SUB32', stroke_width=4,
    paths=['M19 20L22 20','M19 38L22 38'],
    policy='Source terminal supplement to the shared bitcoin body; retain both vertical currency bars.')
