"""Shared small-size optical forms for dense SUB32 currency and registered marks.

Keep these adjustments reusable. They are separate from preferred text glyphs:
open dollar ticks, wider B counters, enlarged R bowl, and diagonal hryvnia spine.
"""
AUTHOR = 'gpt-6'

def draw_dollar(icon, y, top_stub=2):
    icon.add_line('dollar-top',(17,y),(16,y))
    icon.add_arc('dollar-upper',(16,y),(16,y+4),radius_x=4,radius_y=2,sweep=False)
    icon.add_arc('dollar-lower',(16,y+4),(16,y+8),radius_x=4,radius_y=2,sweep=True)
    icon.add_line('dollar-bottom',(16,y+8),(15,y+8))
    icon.add_contour('dollar','dollar-top','dollar-upper','dollar-lower','dollar-bottom')
    icon.add_line('tick-top',(16,y-top_stub),(16,y))
    icon.add_line('tick-bottom',(16,y+8),(16,y+9))
    icon.relate('connect','tick-top','dollar');icon.relate('connect','tick-bottom','dollar')

def draw_bitcoin(icon):
    icon.add_polyline('upper',(10,30),(10,14),(18,14))
    icon.add_arc('bowl-top',(18,14),(18,22),radius_x=4)
    icon.add_line('middle',(18,22),(10,22));icon.relate('connect','upper','bowl-top');icon.relate('connect','middle','upper');icon.relate('connect','middle','bowl-top')
    icon.add_arc('bowl-bottom',(18,22),(18,30),radius_x=4)
    icon.add_line('bottom',(18,30),(10,30));icon.add_contour('lower','bowl-bottom','bottom');icon.relate('connect','lower','upper');icon.relate('connect','lower','middle')
    for name,a,b in [('tick-tl',(12,10),(12,14)),('tick-tr',(20,10),(20,16)),('tick-bl',(12,30),(12,34)),('tick-br',(20,28),(20,34))]:
     icon.add_line(name,a,b)
     icon.relate('connect',name,'upper' if name=='tick-tl' else 'bowl-top' if name=='tick-tr' else 'lower')

def draw_registered_r(icon):
    icon.add_polyline('r-stem',(12,22),(12,10),(16,10))
    icon.add_bezier('r-bowl',(16,10),((22,10),(22,18),(16,18)))
    icon.add_line('r-middle',(16,18),(12,18));icon.relate('connect','r-stem','r-bowl');icon.relate('connect','r-middle','r-stem');icon.relate('connect','r-middle','r-bowl')
    icon.add_line('r-leg',(16,18),(20,22));icon.relate('connect','r-leg','r-bowl');icon.relate('connect','r-leg','r-middle')

def draw_hryvnia(icon):
    icon.add_bezier('top',(8,2),((22,2),(30,2),(22,10)))
    icon.add_line('middle',(22,10),(10,22))
    icon.add_bezier('bottom',(10,22),((2,30),(10,30),(24,30)))
    icon.add_contour('reverse-s','top','middle','bottom')
    icon.add_line('upper-bar',(2,10),(30,10));icon.add_line('lower-bar',(2,22),(30,22))
    icon.relate('connect','upper-bar','reverse-s');icon.relate('connect','lower-bar','reverse-s')

PROFILE_VARIANTS = {'symbol-bitcoin-compact32': {'parent_glyph': 'symbol-bitcoin',
                              'character': '₿',
                              'profile': 'SUB32',
                              'stroke_width': 4,
                              'paths': ['M10 30L10 14L18 14',
                                        'M18 14A4 4 0 0 1 18 22',
                                        'M18 22L10 22',
                                        'M18 22A4 4 0 0 1 18 30L10 30',
                                        'M12 10L12 14',
                                        'M20 10L20 16',
                                        'M12 30L12 34',
                                        'M20 28L20 34'],
                              'svg_sha256': '93e84d52b29485d2c3bc10fe5c0ee3d88a99d58aa94ece5d3a00c9ab53a01b73',
                              'policy': 'Shared optically adjusted small-size form; preferred '
                                        'natural-proportion glyph unchanged.'},
 'letter-r-registered32': {'parent_glyph': 'letter-r-uppercase',
                           'character': 'R',
                           'profile': 'SUB32',
                           'stroke_width': 4,
                           'paths': ['M12 22L12 10L16 10',
                                     'M16 10C22 10 22 18 16 18',
                                     'M16 18L12 18',
                                     'M16 18L20 22'],
                           'svg_sha256': '22a55081d4cc08ca1adbea07b117ef1a22b2e89228bfa4a2e01c3b6d19298b5b',
                           'policy': 'Shared optically adjusted small-size form; preferred '
                                     'natural-proportion glyph unchanged.'},
 'symbol-hryvnia-compact32': {'parent_glyph': 'symbol-hryvnia',
                              'character': '₴',
                              'profile': 'SUB32',
                              'stroke_width': 4,
                              'paths': ['M8 2C22 2 30 2 22 10L10 22C2 30 10 30 24 30',
                                        'M2 10L30 10',
                                        'M2 22L30 22'],
                              'svg_sha256': 'e3b694d39ac1378e73be48edcbe3271bf8e28173c9e25bd545fdad51284808f2',
                              'policy': 'Shared optically adjusted small-size form; preferred '
                                        'natural-proportion glyph unchanged.'},
 'symbol-dollar-compact32': {'parent_glyph': 'symbol-dollar',
                             'character': '$',
                             'profile': 'SUB32',
                             'stroke_width': 4,
                             'paths': ['M17 10L16 10A4 2 0 0 0 16 14A4 2 0 0 1 16 18L15 18',
                                       'M16 8L16 10',
                                       'M16 18L16 19'],
                             'svg_sha256': 'fa8ad871680fccaac060d6aaa1787f094c00aaf6789dda1077e27629b0857c74',
                             'policy': 'Shared optically adjusted small-size form; preferred '
                                       'natural-proportion glyph unchanged.'},
 'symbol-dollar-compact32-short-tick': {'parent_glyph': 'symbol-dollar',
                                        'character': '$',
                                        'profile': 'SUB32',
                                        'stroke_width': 4,
                                        'paths': ['M17 10L16 10A4 2 0 0 0 16 14A4 2 0 0 1 16 18L15 '
                                                  '18',
                                                  'M16 9L16 10',
                                                  'M16 18L16 19'],
                                        'svg_sha256': '439983356bc3004bff00efd60ca32fe1e0f8de1eb5d6902eaf4d65cc55a5d23a',
                                        'policy': 'Shared optically adjusted small-size form; '
                                                  'preferred natural-proportion glyph unchanged.'}}

from .reference_forms import REFERENCE_PROFILE_VARIANTS
PROFILE_VARIANTS.update(REFERENCE_PROFILE_VARIANTS)

from .framed_source_forms import FRAMED_PROFILE_VARIANTS
PROFILE_VARIANTS.update(FRAMED_PROFILE_VARIANTS)

from .source_composition_forms import SOURCE_COMPOSITION_VARIANTS
PROFILE_VARIANTS.update(SOURCE_COMPOSITION_VARIANTS)
