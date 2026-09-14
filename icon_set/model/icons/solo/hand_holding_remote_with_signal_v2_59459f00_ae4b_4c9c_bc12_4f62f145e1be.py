# Variant of hand-holding-remote-with-signal; parent file remains unchanged.
'Hand holding remote with signal: independent spacing revision.\n\nOpen the grip into a broad thumb/palm contour; remove the narrow doubled finger and remote base behind it.\nNative solo family, VRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: hand: clear finger returns and rounded joins. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '59459f00-ae4b-4c9c-bc12-4f62f145e1be'
SOURCE_PATH = 'pictographic-primitives/tv/modern tv remote hand_59459f00-ae4b-4c9c-bc12-4f62f145e1be.svg'
AUTHOR = 'gpt-6'

class HandHoldingRemoteWithSignalVariant2(Solo48):
    icon_id = 'hand-holding-remote-with-signal-v2'
    variant_of = 'hand-holding-remote-with-signal'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/media'
    aliases = ()
    keywords = ('remote', 'hand', 'tv', 'control', 'signal', 'wireless', 'channel', 'holding')

    def circle(self, name, x, y, r):
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def box(self, name, x, y, right, bottom, r=3, attachments=()):
        points = [(x + r, y), (right - r, y), (right, y + r), (right, bottom - r), (right - r, bottom), (x + r, bottom), (x, bottom - r), (x, y + r)]
        members = []
        for i, a in enumerate(points):
            b = points[(i + 1) % 8]
            k = f'{name}-{i}'
            members.append(k)
            if i % 2:
                self.add_arc(k, a, b, radius_x=r)
            else:
                nodes = [p for p in attachments if a[0] == b[0] == p[0] and min(a[1], b[1]) < p[1] < max(a[1], b[1]) or (a[1] == b[1] == p[1] and min(a[0], b[0]) < p[0] < max(a[0], b[0]))]
                if nodes:
                    members.pop()
                    nodes.sort(key=lambda p: (p[0] - a[0]) ** 2 + (p[1] - a[1]) ** 2)
                    chain = [a] + nodes + [b]
                    for j, (u, v) in enumerate(zip(chain, chain[1:])):
                        part = f'{k}-{j}'
                        members.append(part)
                        self.add_line(part, u, v)
                else:
                    self.add_line(k, a, b)
        self.add_contour(name, *members, closed=True)

    def build(self):
        self.add_arc('signal',(8, 8),(28, 8),radius_x=10,radius_y=4,sweep=True)
        self.add_polyline('remote',(8, 30),(8, 17),(24, 17),(24, 26),closed=False)
        self.add_arc('thumb',(24, 26),(16, 34),radius_x=8,radius_y=8,sweep=False)
        self.add_line('palm',(16, 34),(26, 44))
        self.add_contour('grip','thumb','palm',closed=False)
        self.add_polyline('hand',(24, 26),(40, 34),(40, 44),closed=False)
        self.relate('connect','remote','grip')
        self.relate('connect','remote','hand')
        self.relate('connect','grip','hand')
