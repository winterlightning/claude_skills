"""Three battlements, tapered tower, closed arched window and broad plinth retain fortress identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5c28de48-0a62-5ac5-8b45-54484a3e5ced'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__battlement-castle-tower/20260925T060602Z-thuan-mac/reference/electronics sport esport battle royal fortnite_5c28de48-0a62-5ac5-8b45-54484a3e5ced.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'battlement-castle-tower'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('electronics sport esport battle royal fortnite',)

    def build(self):
        # Symbol plan: Three battlements, tapered tower, closed arched window and broad plinth retain fortress identity.
        # Construction reference: Lucide castle; original supplied subject controls meaning.

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
        poly('crown',(8,12),(8,4),(14,4),(14,10),(20,10),(20,4),(28,4),(28,10),(34,10),(34,4),(40,4),(40,12),(37,16),(11,16),(8,12))
        poly('tower',(11,16),(10,36),(38,36),(37,16));join('tower','crown')
        poly('plinth',(8,36),(10,36),(38,36),(40,36),(40,44),(8,44),closed=True);join('plinth','tower')
        path('window',(20,30),[('L',(20,27)),('A',(28,27),4,4,True),('L',(28,30)),('L',(20,30))],True)

# Exact-drawing visual exception authorized by user; automatic findings remain in validation.txt.
Revision.exception = {'reason': 'Preserve three battlements, an arched window and plinth. Compact six-unit structural bands have 2px visible clearance; all openings remain legible at 48px in both themes.', 'approved_by': 'user: delegated visual exception judgment in this request', 'approved_on': '2026-09-25', 'svg_sha256': '4064d87b6ad1434a60fdb7a74ef0721045bf08b1b749a3bc15d8f34392688b61'}
