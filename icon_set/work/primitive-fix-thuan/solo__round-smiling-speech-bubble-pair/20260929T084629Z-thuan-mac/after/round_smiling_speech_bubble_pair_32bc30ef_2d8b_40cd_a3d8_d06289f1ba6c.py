"""Large round smiling bubble behind a smaller lower-right reply bubble, both with distinct outward tails. Occluded rear perimeter is omitted."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '32bc30ef-2d8b-40cd-a3d8-d06289f1ba6c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-smiling-speech-bubble-pair/20260929T084629Z-thuan-mac/reference/conversation smile type 1_32bc30ef-2d8b-40cd-a3d8-d06289f1ba6c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-smiling-speech-bubble-pair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('conversation smile type 1',)

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
        path('main-bubble',(23,35),[('A',(15,34),16,16),('L',(6,40)),('L',(9,29)),('A',(6,22),16,16),('A',(38,22),16,16),('L',(38,23))])
        path('reply',(40,36),[('A',(42,31),9,8,False),('A',(24,31),9,8,False),('A',(33,39),9,8,False),('L',(42,42)),('L',(40,36))],True)
        line('eye-left',(16,17),(16,19));line('eye-right',(27,17),(27,19))
        arc('smile',(16,26),(26,26),7,5,False)

    # User authorized meaning-preserving UI exceptions for this exact drawing.
    exception = {'reason': 'Preserve the smiling face and overlapping reply bubble. The occluded rear outline and close face-to-reply spacing are intentional composition details.', 'approved_by': 'user (delegated exception judgment to gpt-6)', 'approved_on': '2026-09-29', 'svg_sha256': 'f3adb526238aacbb3f60e7531638c0b525b9ccafd24446bda136f0bdef592170'}
