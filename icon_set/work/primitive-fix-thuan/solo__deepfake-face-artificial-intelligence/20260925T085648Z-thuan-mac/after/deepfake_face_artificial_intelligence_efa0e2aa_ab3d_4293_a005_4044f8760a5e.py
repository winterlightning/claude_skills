"""Fresh reference reconstruction for manual fix request. Preserve complete subject and arrangement."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'efa0e2aa-ab3d-4293-a005-4044f8760a5e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__deepfake-face-artificial-intelligence/20260925T085648Z-thuan-mac/reference/deepfake face_efa0e2aa-ab3d-4293-a005-4044f8760a5e.svg'
AUTHOR = "gpt-6"

class Revision(Solo48):
    icon_id = 'deepfake-face-artificial-intelligence'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'other'
    aliases = ()
    keywords = ()

    def build(self):
        # Symmetric face: radius-10 top corners, circular jaw, scan cross and smile.
        self.add_line('top-left',(18,4),(24,4))
        self.add_line('top-right',(24,4),(30,4))
        self.add_arc('upper-right',(30,4),(40,14),radius_x=10)
        self.add_line('right-upper',(40,14),(40,20))
        self.add_line('right-lower',(40,20),(40,28))
        self.add_arc('jaw',(40,28),(8,28),radius_x=16)
        self.add_line('left-lower',(8,28),(8,20))
        self.add_line('left-upper',(8,20),(8,14))
        self.add_arc('upper-left',(8,14),(18,4),radius_x=10)
        self.add_contour('face','top-left','top-right','upper-right','right-upper','right-lower','jaw','left-lower','left-upper','upper-left',closed=True)
        self.add_polyline('scan',(8,20),(24,20),(40,20))
        self.add_polyline('nose',(24,4),(24,20),(24,25))
        self.relate('connect','face','scan')
        self.relate('connect','face','nose')
        self.relate('connect','scan','nose')
        self.add_arc('smile',(17,31),(31,31),radius_x=7,radius_y=4,sweep=False)
