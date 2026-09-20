"""Shared source-faithful optical currency forms for 4px side-icon artwork.

Open dollar uses short ticks, as the supplied source artwork does. Hryvnia
retains the source's curved reverse S rather than substituting a angular Z.
"""
AUTHOR='gpt-6'
def draw_open_dollar(s,cx,y):
    s.add_bezier('dollar-tip-top',(cx+4,y+2),((cx+2,y),(cx+1,y),(cx,y)))
    s.add_bezier('dollar-upper',(cx,y),((cx-6,y),(cx-6,y+6),(cx,y+7)))
    s.add_bezier('dollar-lower',(cx,y+7),((cx+6,y+8),(cx+6,y+14),(cx,y+14)))
    s.add_bezier('dollar-tip-bottom',(cx,y+14),((cx-2,y+14),(cx-3,y+13),(cx-4,y+12)))
    s.add_contour('dollar','dollar-tip-top','dollar-upper','dollar-lower','dollar-tip-bottom')
    s.add_line('dollar-top-tick',(cx,y-2),(cx,y));s.add_line('dollar-bottom-tick',(cx,y+14),(cx,y+16))
    s.relate('connect','dollar','dollar-top-tick');s.relate('connect','dollar','dollar-bottom-tick')

def draw_curved_hryvnia(s):
    s.add_bezier('upper-left',(6,3),((9,2),(11,2),(14,2)))
    s.add_bezier('upper-bowl',(14,2),((26,2),(30,6),(24,12)))
    s.add_line('middle',(24,12),(12,24))
    s.add_bezier('lower-bowl',(12,24),((6,30),(10,30),(18,30)))
    s.add_bezier('lower-tip',(18,30),((21,30),(24,30),(26,29)))
    s.add_contour('reverse-s','upper-left','upper-bowl','middle','lower-bowl','lower-tip')
    for n,y in [('bar-one',14),('bar-two',22)]:
        s.add_line(n,(2,y),(30,y));s.relate('connect',n,'reverse-s')

def draw_small_open_dollar(s,cx,y):
    """Grid-fitted short-tick source variant for complete invoice compositions."""
    s.add_bezier('dollar-tip-top',(cx+3,y+1),((cx+2,y),(cx+1,y),(cx,y)))
    s.add_bezier('dollar-upper',(cx,y),((cx-5,y),(cx-5,y+4),(cx,y+5)))
    s.add_bezier('dollar-lower',(cx,y+5),((cx+5,y+6),(cx+5,y+10),(cx,y+10)))
    s.add_bezier('dollar-tip-bottom',(cx,y+10),((cx-1,y+10),(cx-2,y+10),(cx-3,y+9)))
    s.add_contour('dollar','dollar-tip-top','dollar-upper','dollar-lower','dollar-tip-bottom')
    s.add_line('dollar-top-tick',(cx,y-2),(cx,y));s.add_line('dollar-bottom-tick',(cx,y+10),(cx,y+12))
    s.relate('connect','dollar','dollar-top-tick');s.relate('connect','dollar','dollar-bottom-tick')

def draw_narrow_pound(s):
    """Narrow source-style pound for a complete portrait invoice, retaining all strokes."""
    s.add_bezier('pound-top',(15,18),((15,12),(10,12),(10,18)))
    s.add_line('pound-stem',(10,18),(10,28))
    s.add_bezier('pound-hook',(10,28),((10,30),(10,32),(9,32)))
    s.add_line('pound-base',(9,32),(16,32))
    s.add_contour('pound','pound-top','pound-stem','pound-hook','pound-base')
    s.add_line('pound-crossbar',(9,24),(16,24));s.relate('connect','pound-crossbar','pound')

REFERENCE_PROFILE_VARIANTS = {'symbol-dollar-open-source32': {'parent_glyph': 'symbol-dollar',
                                 'character': '$',
                                 'profile': 'SUB32',
                                 'stroke_width': 4,
                                 'paths': ['M20 12C18 10 17 10 16 10C10 10 10 '
                                           '16 16 17C22 18 22 24 16 24C14 24 '
                                           '13 23 12 22',
                                           'M16 8L16 10',
                                           'M16 24L16 26'],
                                 'svg_sha256': '2e5a6875a9d5aba57f04f12521ef03a121a809dd12302b8846ec8d06e8bff338',
                                 'policy': 'Shared source-faithful optical '
                                           'variant; preserves complete '
                                           'composition and source currency '
                                           'strokes.'},
 'symbol-dollar-open-small-source32': {'parent_glyph': 'symbol-dollar',
                                       'character': '$',
                                       'profile': 'SUB32',
                                       'stroke_width': 4,
                                       'paths': ['M19 11C18 10 17 10 16 10C11 '
                                                 '10 11 14 16 15C21 16 21 20 '
                                                 '16 20C15 20 14 20 13 19',
                                                 'M16 8L16 10',
                                                 'M16 20L16 22'],
                                       'svg_sha256': 'e749612a1d4892151306d8c2ee0126f2df504c9f4eb01acb43662d483550e683',
                                       'policy': 'Shared source-faithful '
                                                 'optical variant; preserves '
                                                 'complete composition and '
                                                 'source currency strokes.'},
 'symbol-pound-portrait-source32': {'parent_glyph': 'symbol-pound',
                                    'character': '£',
                                    'profile': 'SUB32',
                                    'stroke_width': 4,
                                    'paths': ['M15 18C15 12 10 12 10 18L10 '
                                              '28C10 30 10 32 9 32L16 32',
                                              'M9 24L16 24'],
                                    'svg_sha256': '336344476987e8cc937baffaaa2d421d7d5f7b6ccf7725330c5df4ca0e6d92fb',
                                    'policy': 'Shared source-faithful optical '
                                              'variant; preserves complete '
                                              'composition and source currency '
                                              'strokes.'},
 'symbol-hryvnia-curved-source32': {'parent_glyph': 'symbol-hryvnia',
                                    'character': '₴',
                                    'profile': 'SUB32',
                                    'stroke_width': 4,
                                    'paths': ['M6 3C9 2 11 2 14 2C26 2 30 6 24 '
                                              '12L12 24C6 30 10 30 18 30C21 30 '
                                              '24 30 26 29',
                                              'M2 14L30 14',
                                              'M2 22L30 22'],
                                    'svg_sha256': '15b2ecb42d7727db3dce09c2ffe4d469e89248f9c6d79845998c96ede0c79b2a',
                                    'policy': 'Shared source-faithful optical '
                                              'variant; preserves complete '
                                              'composition and source currency '
                                              'strokes.'}}
