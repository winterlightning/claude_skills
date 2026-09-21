"""Central user surrounded by square, circle and triangle with two orbital arcs. SQUARE follows the arrangement extremes. Human user.svg supplies circular head and open shoulders; source supplies shapes and layout. Head center(24,24) radius2, shoulders top34 gives exact8 centerline gap. Unresolved: triangle hole fails; central user loses prominence at native48. Larger head/shoulders and outer shapes were tried and fail clearance. Bottom orbital arc omitted during repair; rotating the complete diagram cannot free enough room."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0bed2a31-9297-4a65-99ad-c1ed293776b1'
SOURCE_PATH = 'work/drawn-unpublished-2026-09-21/batch-04/06-user-centered-geometric-interaction/reference.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'user-centered-shape-diagram-v2'
    variant_of = 'user-centered-shape-diagram'
    variant_label = 'Distilled reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('user', 'centered', 'shape', 'diagram', 'v2')

    def build(self):
        def circle(name, x, y, r):
            self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        def path(name, start, commands, closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                part=f'{name}-{i}'
                if kind=='L': self.add_line(part,here,end)
                elif kind=='A': self.add_arc(part,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                else: self.add_bezier(part,here,(args[0],args[1],end))
                here=end; members.append(part)
            self.add_contour(name,*members,closed=closed)
        self.add_polyline('square',(20,6),(28,6),(28,14),(20,14),closed=True)
        circle('circle',8,38,2)
        self.add_polyline('triangle',(34,42),(42,42),(38,34),closed=True)
        circle('head',24,24,2)
        path('shoulders',(21,37),[('A',(24,34),3,3,True),('A',(27,37),3,3,True)])
        path('orbit-left',(6,24),[('C',(11,14),(6,20),(8,17))])
        path('orbit-right',(37,14),[('C',(42,24),(40,17),(42,20))])
