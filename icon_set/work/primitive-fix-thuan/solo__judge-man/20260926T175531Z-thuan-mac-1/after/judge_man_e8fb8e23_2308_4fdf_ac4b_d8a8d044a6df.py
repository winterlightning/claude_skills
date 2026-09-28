"""judge-man: revised SOLO48 drawing from the claimed source.

Comparison: The rejected generic bust and pointed fringe omitted the large court wig framing the face.
Revision: Redrew the reference as a tall wig frame with an oval face and curled lower ends.
Human construction: icon_set/references/human_ref/user.svg; Lucide user-round supplies simple circular head and shoulder arcs.
The emitted primitives use a shared axis where the reference is symmetric.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'e8fb8e23-2308-4fdf-ac4b-d8a8d044a6df'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__judge-man/20260926T175531Z-thuan-mac-1/reference/judge man_e8fb8e23-2308-4fdf-ac4b-d8a8d044a6df.svg'
AUTHOR = 'gpt-6'

class JudgeMan(Solo48):
    icon_id = 'judge-man'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('judge', 'man', 'avatars')

    def build(self):
        # Rounded court wig framing a plain face; its two curled ends reach below.
        axis = 24
        self.add_arc('wig-crown-left',(axis,4),(8,20),radius_x=16,sweep=False)
        self.add_line('wig-side-left',(8,20),(8,36))
        self.add_bezier('wig-curl-left',(8,36),((8,41),(10,44),(12,44)))
        self.add_contour('wig-left','wig-crown-left','wig-side-left','wig-curl-left')
        self.add_arc('wig-crown-right',(axis,4),(40,20),radius_x=16)
        self.add_line('wig-side-right',(40,20),(40,36))
        self.add_bezier('wig-curl-right',(40,36),((40,41),(38,44),(36,44)))
        self.add_contour('wig-right','wig-crown-right','wig-side-right','wig-curl-right')
        self.relate('connect','wig-left','wig-right')
        self.add_arc('face-top',(17,24),(31,24),radius_x=7,radius_y=10)
        self.add_arc('face-bottom',(31,24),(17,24),radius_x=7,radius_y=10)
        self.add_contour('face','face-top','face-bottom',closed=True)
