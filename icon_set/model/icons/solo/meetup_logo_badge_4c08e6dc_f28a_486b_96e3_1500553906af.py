"""A scalloped badge outline holds a cursive lowercase m with slanted strokes.

Symbol plan: Eight-lobed badge from four repeated scalloped quadrants, enclosing three equally slanted m stems. Radial maximum20.
Review notes: Retains the scalloped badge and slanted m. Widened the badge, used shallower scallops, and widened the repeated stem step to nine units. Shared rotated curves keep the enclosure smooth and balanced; the m retains its intentional lean.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c08e6dc-f28a-486b-96e3-1500553906af'
SOURCE_PATH = 'pictographic-primitives/logos/meetup alternate logo_4c08e6dc-f28a-486b-96e3-1500553906af.svg'
AUTHOR = 'gpt-6'

class MeetupLogoBadge(Solo48):
    icon_id = 'meetup-logo-badge'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('meetup', 'events', 'community', 'badge', 'logo', 'brand', 'letter-m')

    def build(self):

        def chain(name, *points):
            for i,(start,end) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{i}',start,end)
        def ring(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def rounded(name, left, top, right, bottom, r):
            points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for i,start in enumerate(points):
                end=points[(i+1)%8]; ident=f'{name}-{i}'
                if start==end: continue
                if i%2:self.add_arc(ident,start,end,radius_x=r)
                else:self.add_line(ident,start,end)
                members.append(ident)
            self.add_contour(name,*members,closed=True)
        # One smooth scalloped quadrant, rotated in integer quarter-turns.
        quarter=[((3,-20),(3,-17),(6,-17)),((10,-17),(12,-16),(14,-14)),((16,-12),(17,-10),(17,-6)),((17,-3),(20,-3),(20,0))]
        def turn(point,k):
            x,y=point
            for _ in range(k):x,y=-y,x
            return (24+x,24+y)
        segments=[tuple(turn(p,k) for p in segment) for k in range(4) for segment in quarter]
        self.add_bezier('badge',(24,4),*segments)
        self.add_contour('outline','badge',closed=True)

        for i,x in enumerate((16,25,34)):
            self.add_line(f'm-stem-{i}',(x,23),(x-1,28))
        for i,x in enumerate((16,25)):
            self.add_arc(f'm-arch-{i}',(x,23),(x+9,23),radius_x=5)
            for j in (i,i+1):self.relate('connect',f'm-arch-{i}',f'm-stem-{j}')
        self.relate('connect','m-arch-0','m-arch-1')
