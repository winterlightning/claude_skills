"""A postage stamp bearing a cropped continuous face profile.
Plan: SQUARE centerline extremes (6,6)-(42,42); rounded right corners and
two repeated radius4 perforations on left. Profile attaches to top and
bottom stamp boundary, preserving the reviewed integrated subject.
Shared human_ref/user.svg inspected for minimal anatomical detail; this source
is a continuous cropped profile, so detached head/body gap does not apply.
No useful Lucide portrait-stamp match; source owns the asymmetric profile.
Use circular chin transition; omit the source forehead seam to keep openings.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7666422-a3f3-4822-a1b9-b8fa242e2e68'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/emails/stamps famous_b7666422-a3f3-4822-a1b9-b8fa242e2e68.svg'
AUTHOR = "gpt-6"

class PostageStampWithFaceProfile(Solo48):
    icon_id = 'postage-stamp-with-face-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "emails"
    aliases = ()
    keywords = ('postage', 'stamp', 'with', 'face', 'profile')

    def build(self):
        self.add_line('top0',(6, 16),(6, 6))
        self.add_line('top1',(6, 6),(28, 6))
        self.add_line('top2',(28, 6),(38, 6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('bottom0',(38, 42),(32, 42))
        self.add_line('bottom1',(32, 42),(6, 42))
        self.add_line('bottom2',(6, 42),(6, 32))
        names=[]
        for i in range(2):
            y=32-i*8
            name=f'perforation-{i}'
            self.add_arc(name,(6,y),(6,y-8),radius_x=4,sweep=False)
            names.append(name)
        self.add_contour('stamp','top0','top1','top2','tr','right','br','bottom0','bottom1','bottom2',*names,closed=True)
        self.add_line('nose0',(28, 6),(20, 26))
        self.add_line('nose1',(20, 26),(24, 26))
        self.add_line('nose2',(24, 26),(24, 29))
        self.add_arc('chin',(24,29),(28,33),radius_x=4,sweep=False)
        self.add_line('neck0',(28, 33),(32, 33))
        self.add_line('neck1',(32, 33),(32, 42))
        self.add_contour('profile','nose0','nose1','nose2','chin','neck0','neck1')
        self.relate('connect','stamp','profile')
