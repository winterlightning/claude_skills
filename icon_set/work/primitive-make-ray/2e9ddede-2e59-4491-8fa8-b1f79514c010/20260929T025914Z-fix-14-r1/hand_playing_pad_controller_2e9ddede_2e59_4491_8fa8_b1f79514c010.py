"""Restored the controller’s outer frame and pad grid, the pressing index finger, and a paired musical-note cue.
Before: The rejected pad controller becomes the letter E and loses the complete pad grid; the music cue shrinks to one note.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2e9ddede-2e59-4491-8fa8-b1f79514c010'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-playing-pad-controller/20260929T025914Z-thuan-mac/reference/modern music mix touch_2e9ddede-2e59-4491-8fa8-b1f79514c010.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-playing-pad-controller'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'modern music mix touch')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            ident=f"{name}-{i}"
            end=tuple(step[:2])
            if len(step)==2:
                self.add_line(ident, point, end)
            else:
                self.add_arc(ident, point, end, radius_x=step[2], radius_y=step[3], sweep=step[4])
            members.append(ident)
            point=end
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name,(cx-r,cy),(cx+r,cy,r,r,True),(cx-r,cy,r,r,True),closed=True)

    def build(self):

        # Pad grid at left is partly occluded by the foreground pointing hand.
        self.path('controller',(22,38),(7,38),(4,35,3,3,True),(4,11),(7,8,3,3,True),(29,8))
        self.add_line('grid-vertical',(14,8),(14,38))
        for i,y in enumerate((18,28)):self.add_line(f'grid-row-{i}',(4,y),(23,y))
        self.path('hand',(25,44),(20,38),(24,34,3,3,True),(28,38),(28,24),(34,24,3,3,True),(34,31),(39,31),(44,36,5,5,True),(44,44))
        self.path('note-stems',(34,16),(34,7),(44,4),(44,14))
        self.circle('note-left',31,17,2)
        self.circle('note-right',41,15,2)
        self.relate('connect','controller','grid-vertical')
        self.relate('connect','controller','grid-row-0')
        self.relate('connect','controller','grid-row-1')
        self.relate('connect','grid-vertical','grid-row-0')
        self.relate('connect','grid-vertical','grid-row-1')

