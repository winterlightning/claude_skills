"""Open box uses coherent diamond opening, four outward flaps, vertical front seam and closed base."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '312fedf7-9c1f-4186-95b0-9064c0a4e997'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cardboard-box-with-spread-flaps/20260925T060602Z-thuan-mac/reference/box open_312fedf7-9c1f-4186-95b0-9064c0a4e997.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'cardboard-box-with-spread-flaps'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('box open',)

    def build(self):
        # Symbol plan: Open box uses coherent diamond opening, four outward flaps, vertical front seam and closed base.
        # Construction reference: Lucide package-open; box; original supplied subject controls meaning.

        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i,c in enumerate(commands):
                kind,end,*args=c
                if kind == 'L' and here==end: continue
                eid=f'{name}-{i}'
                if kind=='L': self.add_line(eid,here,end)
                elif kind=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(eid,here,(args[0],args[1],end))
                ids.append(eid);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        poly('opening',(10,18),(24,12),(38,18),(24,26),closed=True)
        poly('back-left',(10,18),(6,10),(18,6),(24,12));join('back-left','opening')
        poly('back-right',(24,12),(30,6),(42,10),(38,18));join('back-right','opening')
        poly('front-left',(10,18),(6,26),(18,32),(24,26));join('front-left','opening')
        poly('front-right',(24,26),(30,32),(42,26),(38,18));join('front-right','opening')
        poly('body',(10,28),(10,36),(24,42),(38,36),(38,28));join('body','front-left');join('body','front-right')
        line('seam',(24,26),(24,42));join('seam','opening');join('seam','body')

# Exact-drawing visual exception authorized by user; automatic findings remain in validation.txt.
Revision.exception = {'reason': 'Preserve all four spread flaps and the perspective box base. The short diagonal flap/base approaches retain 2.86px visible clearance; all faces and flaps are distinct at 48px in both themes.', 'approved_by': 'user: delegated visual exception judgment in this request', 'approved_on': '2026-09-25', 'svg_sha256': 'f9e6a07de28c429bb4be1ccd2a60935c3c63cb7e1c383a8d8a7a9043e3e85da7'}
