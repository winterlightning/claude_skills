"""Revision for bad-stroke feedback. Shared human_ref/full_body_ref.png: outlined round heads, open limbs, rounded dress.
Omissions: Fringe removed at this scale; woman hair sides retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8808cfa8-f297-4bd3-a099-3c4ba3f2b025'
SOURCE_PATH = 'pictographic-primitives/users/multiple man woman 1_8808cfa8-f297-4bd3-a099-3c4ba3f2b025.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'couple-standing-with-hair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'users'
    aliases = ()
    keywords = ('multiple', 'man', 'woman', '1')
    def build(self):

        # Typed continuous paths own their junctions. Repeated parts share parameters.
        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i, (kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                ids.append(ident);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        # Equivalent heads: r=5, bottom16; shoulders24 -> exact 4-unit ink gap.
        for who,x in [('man',13),('woman',35)]: circle(who+'-head',x,11,5)
        line('torso',(13,24),(13,32))
        poly('arms',(6,24),(13,24),(20,24))
        poly('legs',(6,42),(13,32),(20,42))
        join('arms','torso');join('legs','torso')
        self.mark_human_figure('man',head='man-head',torso='torso',torso_junction='start')
        path('dress',(35,24),[('C',(42,34),(38,24),(40,30)),('L',(39,34)),('L',(31,34)),('L',(28,34)),('C',(35,24),(30,30),(32,24))],True)
        for x in (31,39):
            line('leg-'+str(x),(x,34),(x,42));join('dress','leg-'+str(x))
        for x in (30,40):
            line('hair-'+str(x),(x,11),(x,16));join('woman-head','hair-'+str(x))
