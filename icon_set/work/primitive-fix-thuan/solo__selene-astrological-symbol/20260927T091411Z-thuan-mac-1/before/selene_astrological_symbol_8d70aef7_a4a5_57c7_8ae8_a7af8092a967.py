"""Moved the lunar arc as one unit and shortened the lower stem.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: moon: coherent lunar curve.
"""
# Independent repair of selene-astrological-symbol; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8d70aef7-a4a5-57c7-8ae8-a7af8092a967'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/astrology selene_8d70aef7-a4a5-57c7-8ae8-a7af8092a967.svg'
AUTHOR = 'gpt-6'

class SeleneAstrologicalSymbol(Solo48):
    icon_id = 'selene-astrological-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('selene', 'astrology', 'moon', 'symbol', 'horoscope', 'glyph', 'lunar', 'goddess')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self):
        # The moon is now an exact half circle above a clearly separated cross.

        def path(n, start, commands, closed=False):
            names=[];here=start
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                names.append(ident);here=end
            self.add_contour(n,*names,closed=closed)
        def ellipse(n,x,y,rx,ry):
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('moon',(24,4),[('A',(36,16),12,12,True),('A',(24,28),12,12,True)])
        poly('stem',(24,28),(24,36),(24,44));poly('crossbar',(16,36),(24,36),(32,36));join('moon','stem');join('stem','crossbar')
