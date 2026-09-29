"""Rounded bowl beneath domed lid, small circular knob, graceful open spout left and loop handle right."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '8287521a-3079-4a79-bfd5-354b8067a810'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-teapot-with-curved-spout-and-domed-lid/20260929T084629Z-thuan-mac/reference/tea pot_8287521a-3079-4a79-bfd5-354b8067a810.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-teapot-with-curved-spout-and-domed-lid'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('tea pot',)

    def build(self):

        def line(n, a, b): self.add_line(n, a, b)
        def poly(n, *p, closed=False): self.add_polyline(n, *p, closed=closed)
        def arc(n, a, b, rx, ry=None, sweep=True, large=False):
            self.add_arc(n, a, b, radius_x=rx, radius_y=ry or rx, sweep=sweep, large_arc=large)
        def ellipse(n, x, y, rx, ry=None):
            ry = ry or rx
            arc(n+'-top', (x-rx,y), (x+rx,y), rx, ry)
            arc(n+'-bottom', (x+rx,y), (x-rx,y), rx, ry)
            self.add_contour(n, n+'-top', n+'-bottom', closed=True)
        def path(n, start, segments, closed=False):
            p = start; members = []
            for i, seg in enumerate(segments):
                name = f'{n}-{i}'; q = seg[1]
                if seg[0] == 'L': line(name,p,q)
                else: arc(name,p,q,*seg[2:])
                members.append(name); p=q
            self.add_contour(n,*members,closed=closed)
        def rounded(n, x1,y1,x2,y2,r):
            path(n,(x1+r,y1), [('L',(x2-r,y1)),('A',(x2,y1+r),r),
                ('L',(x2,y2-r)),('A',(x2-r,y2),r),('L',(x1+r,y2)),
                ('A',(x1,y2-r),r),('L',(x1,y1+r)),('A',(x1+r,y1),r)],True)
        path('body',(14,19),[('A',(12,29),21,21,False),('A',(18,40),10,10,False),('L',(30,40)),('A',(36,29),10,10,False),('A',(34,19),21,21,False)],False)
        path('lid',(14,19),[('A',(34,19),12,9),('L',(14,19))],True)
        ellipse('knob',24,8,3)
        path('spout',(12,29),[('A',(6,23),6,6),('L',(6,16)),('L',(4,13))])
        path('handle',(36,20),[('A',(36,34),8,7)])
