"""Restored an angled rear leaf, a clear rating star, and one text line on the front cover.
Plan and comparison: The booklet lost its angled rear cover and both text rules, and its star is cramped.
Construction reference: no useful exact Lucide match; rounded enclosure and one coherent star contour
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d9776d01-07f9-402d-ac77-fc73a405a509'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rating-booklet/20260929T043142Z-thuan-mac/reference/rating booklet_d9776d01-07f9-402d-ac77-fc73a405a509.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='rating-booklet'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def path(self, name, start, commands, closed=False):
        members=[]
        at=start
        for n,c in enumerate(commands):
            ident=f"{name}-{n}"
            if c[0]=='L':
                end=c[1]; self.add_line(ident,at,end)
            else:
                _,end,rx,ry,sweep,*large=c
                self.add_arc(ident,at,end,radius_x=rx,radius_y=ry,sweep=sweep,large_arc=bool(large and large[0]))
            members.append(ident); at=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

    def box(self,name,l,t,r,b,rad=2):
        self.path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):

        # Front cover owns star and centered text; the rear leaf projects above it.
        self.add_polyline('back',(14,10),(35,4),(35,12))
        self.box('cover',10,12,38,44,1)
        self.relate('connect','back','cover')
        self.add_polyline('star',(24,18),(27,24),(33,24),(28,28),(30,34),(24,31),(18,34),(20,28),(15,24),(21,24),closed=True)
        self.add_line('text-1',(20,38),(28,38))

Drawing.exception = {'reason': 'The five-point rating star and angled back leaf retain small openings within the booklet. One text line is retained and the second omitted to avoid congestion. Reviewed against the original and rejected drawing at 48px and enlarged size in light and dark. User explicitly delegated case-specific exceptions for UI/UX quality.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'e491ff153c2aeff2e6bc0c797c4e71b4c8251d80f80ac4f8b2df0bc47ca3d61d'}
