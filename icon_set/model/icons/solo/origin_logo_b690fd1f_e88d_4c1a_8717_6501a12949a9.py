"""A ring sits at the centre of a circular swirl whose two halves are offset, each ending in a pointed hook at the top and bottom like a spinning orbit.

Symbol plan: Two offset hooked swirl halves around a radius3 ring; extremes (8,4)-(40,44).
Review notes: Retains the two hooked tips and center ring. Broad coherent curves replace the source tracing; deliberate offset hooks carry the rotating direction. Circle construction informs the center.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b690fd1f-e88d-4c1a-8717-6501a12949a9'
SOURCE_PATH = 'pictographic-primitives/logos/origin logo_b690fd1f-e88d-4c1a-8717-6501a12949a9.svg'
AUTHOR = 'gpt-6'

class OriginLogo(Solo48):
    icon_id = 'origin-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('origin', 'ea', 'gaming', 'swirl', 'logo', 'brand', 'store')

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
        self.add_bezier('upper-left',(24,4),((14,6),(8,16),(8,24)))
        self.add_bezier('lower-left',(8,24),((8,32),(12,36),(18,36)))
        self.add_line('lower-hook',(18,36),(24,44))
        self.add_bezier('lower-right',(24,44),((34,42),(40,32),(40,24)))
        self.add_bezier('upper-right',(40,24),((40,16),(36,12),(30,12)))
        self.add_line('upper-hook',(30,12),(24,4))
        self.add_contour('swirl','upper-left','lower-left','lower-hook','lower-right','upper-right','upper-hook',closed=True)
        ring('center',24,24,3)
