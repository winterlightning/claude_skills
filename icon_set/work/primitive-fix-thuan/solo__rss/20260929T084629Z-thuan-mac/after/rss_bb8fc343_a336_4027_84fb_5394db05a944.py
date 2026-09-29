"""Lucide RSS concentric arcs adapted inside the supplied rounded-square enclosure; all broadcast arcs share a center."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'bb8fc343-a336-4027-84fb-5394db05a944'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rss/20260929T084629Z-thuan-mac/reference/rss_bb8fc343-a336-4027-84fb-5394db05a944.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rss'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('rss',)

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
        rounded('frame',6,6,42,42,4)
        ellipse('origin',15,33,3)
        arc('inner-wave',(13,22),(26,35),13,13)
        arc('outer-wave',(13,13),(35,35),22,22)

    # User authorized meaning-preserving UI exceptions for this exact drawing.
    exception = {'reason': 'Preserve both broadcast waves, circular origin and enclosure. Compact frame spacing and circular origin preserve the complete requested RSS composition.', 'approved_by': 'user (delegated exception judgment to gpt-6)', 'approved_on': '2026-09-29', 'svg_sha256': '4aa9c731576a39348324ce6ab1d235b7a75ee75475fcfd44569f19ff5eee5f05'}
