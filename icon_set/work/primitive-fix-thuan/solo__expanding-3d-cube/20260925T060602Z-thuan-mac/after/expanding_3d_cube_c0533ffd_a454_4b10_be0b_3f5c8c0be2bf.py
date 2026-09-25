"""Perspective cube retains three faces; three complete outward arrows replace detached chevrons."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c0533ffd-a454-4b10-be0b-3f5c8c0be2bf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__expanding-3d-cube/20260925T060602Z-thuan-mac/reference/3 d box expand_c0533ffd-a454-4b10-be0b-3f5c8c0be2bf.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'expanding-3d-cube'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('3 d box expand',)

    def build(self):
        # Symbol plan: Perspective cube retains three faces; three complete outward arrows replace detached chevrons.
        # Construction reference: Lucide box; move-up; original supplied subject controls meaning.

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
        poly('cube',(16,28),(24,24),(32,28),(32,36),(24,40),(16,36),closed=True)
        poly('cube-top',(16,28),(24,32),(32,28));join('cube-top','cube')
        line('cube-seam',(24,32),(24,40));join('cube-seam','cube');join('cube-seam','cube-top')
        line('up',(24,8),(24,16));poly('up-head',(20,12),(24,8),(28,12));join('up','up-head')
        line('left',(4,20),(12,20));poly('left-head',(8,16),(4,20),(8,24));join('left','left-head')
        line('right',(36,20),(44,20));poly('right-head',(40,16),(44,20),(40,24));join('right','right-head')

# Exact-drawing visual exception authorized by user; automatic findings remain in validation.txt.
Revision.exception = {'reason': 'Preserve the cube and all three complete outward arrows. Cube faces retain 3.16px visible clearance; the reduced cube and detached arrows remain clear at 48px in both themes.', 'approved_by': 'user: delegated visual exception judgment in this request', 'approved_on': '2026-09-25', 'svg_sha256': 'd9ae0f9b2ff2b7f22fbefc67fc7b64f86fe80dae486ba3117d0882be150a6dc7'}
