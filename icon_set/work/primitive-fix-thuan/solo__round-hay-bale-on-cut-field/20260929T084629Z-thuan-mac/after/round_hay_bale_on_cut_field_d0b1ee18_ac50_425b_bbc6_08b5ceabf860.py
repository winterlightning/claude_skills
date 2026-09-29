"""Circular end and offset cylindrical back share upper/lower levels; field edge supports the bale and owns stubble repeats."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'd0b1ee18-ac50-425b-bbc6-08b5ceabf860'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-hay-bale-on-cut-field/20260929T084629Z-thuan-mac/reference/farming hay_d0b1ee18-ac50-425b-bbc6-08b5ceabf860.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-hay-bale-on-cut-field'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('farming hay',)

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
        ellipse('bale-end',15,20,11,12)
        ellipse('roll',15,20,4,5)
        path('bale-depth',(15,8),[('L',(30,8)),('A',(30,32),11,12),('L',(15,32))])
        path('field',(4,32),[('L',(36,32)),('A',(44,40),8,8)])
        for i,x in enumerate((8,19,30)):
            poly(f'stubble-{i}',(x-2,37),(x,40),(x+2,37))

    # User authorized meaning-preserving UI exceptions for this exact drawing.
    exception = {'reason': 'Preserve the rolled bale center, offset cylindrical depth, supporting field and repeated cut stalks. Reduced clearances retain a coherent agricultural scene.', 'approved_by': 'user (delegated exception judgment to gpt-6)', 'approved_on': '2026-09-29', 'svg_sha256': '3baef09a4e266ed2320ae028d2e5547d14a110218cdc4ba76154e6697f436872'}
