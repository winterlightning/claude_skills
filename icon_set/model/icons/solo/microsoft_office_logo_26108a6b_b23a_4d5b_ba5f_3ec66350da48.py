"""A tall door-like panel in perspective: a wide left face slanting inward and a narrow right strip, joined by top and bottom edges that angle to a spine.

Symbol plan: Perspective door/panel outline with one right-hand spine. Extremes (8,4)-(40,44).
Review notes: All three visible planes remain in one coherent outline. The right strip is widened to ten units. Lucide square informs the closed contour, while perspective and the off-center spine follow the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26108a6b-b23a-4d5b-ba5f-3ec66350da48'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft office logo_26108a6b-b23a-4d5b-ba5f-3ec66350da48.svg'
AUTHOR = 'gpt-6'

class MicrosoftOfficeLogo(Solo48):
    icon_id = 'microsoft-office-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('microsoft-office', 'office', 'microsoft', 'productivity', 'logo', 'brand', 'suite')

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
        self.add_polyline('outline',(30,4),(40,8),(40,40),(30,44),(8,36),(8,12),closed=True)
        self.add_line('spine',(30,4),(30,44))
        for member in ['outline-1','outline-3','outline-4','outline-6']:self.relate('connect','spine',member)
