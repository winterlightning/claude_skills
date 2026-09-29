"""sport rafting equipment.
Plan: Restored the surrounding air tube, recessed cockpit and a seat, beside a separate paddle with a wide blade and end grip.
Construction: sailboat: coherent vessel contours; the raft structure comes from the original.
Keyshape: VRECT_L; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '92104123-8895-5407-a206-a94ae12de98d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__inflatable-raft-and-paddle/20260929T033633Z-thuan-mac/reference/sport rafting equipment_92104123-8895-5407-a206-a94ae12de98d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'inflatable-raft-and-paddle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('sport', 'rafting', 'equipment')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def rect(self,n,x,y,w,h,r=3):
        self.add_line(n+'t',(x+r,y),(x+w-r,y))
        self.add_arc(n+'tr',(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line(n+'r',(x+w,y+r),(x+w,y+h-r))
        self.add_arc(n+'br',(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line(n+'b',(x+w-r,y+h),(x+r,y+h))
        self.add_arc(n+'bl',(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line(n+'l',(x,y+h-r),(x,y+r))
        self.add_arc(n+'tl',(x,y+r),(x+r,y),radius_x=r)
        self.add_contour(n,*[n+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)

    def build(self):

        self.add_arc('raft-top',(4,16),(28,16),radius_x=12)
        self.add_line('raft-right',(28,16),(28,32));self.add_arc('raft-bottom',(28,32),(4,32),radius_x=12)
        self.add_line('raft-left',(4,32),(4,16));self.add_contour('raft','raft-top','raft-right','raft-bottom','raft-left',closed=True)
        self.rect('cockpit',10,12,12,24,6)
        self.add_line('seat',(10,24),(22,24));self.relate('connect','seat','cockpit')
        self.rect('blade',35,4,9,14,3)
        self.add_line('shaft',(40,18),(40,44));self.add_line('grip',(36,44),(44,44));self.relate('connect','shaft','blade');self.relate('connect','shaft','grip')

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Preserve the inflatable raft rim, inner cockpit and separate paddle. Compact parallel rim and cockpit spacing remain clearly separated at native size.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '44a05e76f0aadb4d078f77ad530c81a7a436a72876b3886eea2fb4517bfbe4fe'}
