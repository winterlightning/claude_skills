"""Two lane contours share center (24,24) and radii 18 and 10; separate right-facing arrow centered at y28. Ink extremes (4,4)-(44,44).
Lucide undo-2: a semicircular turn with tangent straight sections and an open chevron arrowhead. The source sets the rightward direction."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bbab0c61-cd66-44e3-8954-bcb31ddc3d23'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__running-track-curve-arrow/20260928T175139Z-thuan-mac/reference/athletics running 1_bbab0c61-cd66-44e3-8954-bcb31ddc3d23.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'running-track-curve-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('running', 'track', 'curve', 'arrow')

    exception = {'reason': 'User authorized visual exceptions for UI quality. Two concentric lanes retain an analytical 4px ink gap (sampled curve warning); the open arrowhead retains 3px clearance from the horizontal lanes. Native light/dark review confirms a clear arrow, visible shaft and smooth track. All strokes 4px.', 'approved_by': 'user: delegated visual-exception decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'f58b08afbc665e502d26da86bc99fa0f81c4ffca6f73eb788b0fa32543e2356b'}

    def build(self):

        def curve(name,start,c1,c2,end):
            self.add_bezier(name,start,(c1,c2,end))
        def path(name,start,steps,closed=False):
            point=start
            ids=[]
            for j,(kind,end,*args) in enumerate(steps):
                part=f'{name}-{j}'
                if kind=='L': self.add_line(part,point,end)
                elif kind=='A': self.add_arc(part,point,end,radius_x=args[0],sweep=args[1])
                elif kind=='C': curve(part,point,args[0],args[1],end)
                ids.append(part)
                point=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)

        for name,r,end in [('outer',18,42),('inner',10,25)]:
            path(name,(42,24-r),[('L',(24,24-r)),('A',(24,24+r),r,False),('L',(end,24+r))])
        self.add_polyline('arrowhead',(34,21),(42,28),(34,35))
        self.add_line('shaft',(31,28),(42,28))
        self.relate('connect','arrowhead','shaft')
