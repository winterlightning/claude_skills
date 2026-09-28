"""Crescent with circular outer bulge, concave inner face and intentional pointed cusps."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6dd077fd-c745-464e-9bfc-be53b27bf22e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__astrology-moon/20260925T060602Z-thuan-mac/reference/astrology moon_6dd077fd-c745-464e-9bfc-be53b27bf22e.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'astrology-moon'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('astrology moon',)

    def build(self):
        # Symbol plan: Crescent with circular outer bulge, concave inner face and intentional pointed cusps.
        # Construction reference: Lucide moon; original supplied subject controls meaning.

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
        path('crescent',(8,8),[('A',(20,4),20,20,True),('A',(40,24),20,20,True),('A',(20,44),20,20,True),('A',(8,40),20,20,True),('A',(8,8),18,16,False)],True)

# Exact-drawing visual exception authorized by user; automatic findings remain in validation.txt.
Revision.exception = {'reason': 'Preserve the pointed crescent cusps. Short inner/outer curve approaches retain 3.11px visible clearance and a broad readable crescent; reviewed at 48px in both themes.', 'approved_by': 'user: delegated visual exception judgment in this request', 'approved_on': '2026-09-25', 'svg_sha256': 'c5a024d55edd5eb6464759fe22b5f3acc3fe864eee5bd053669b5bbc7503895f'}
