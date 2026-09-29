from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '8d871e7d-03c3-4f02-90aa-ec0ac69a56b5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__squeeze-sides/20260929T091947Z-thuan-mac/reference/squeeze sides_8d871e7d-03c3-4f02-90aa-ec0ac69a56b5.svg'
AUTHOR = "gpt-6"
# Plan: Restore a rounded upright phone, four gripping finger segments, side hand and inward squeeze arrows.
# Keyshape: VRECT_L; preserve reference arrangement.
# Construction reference: hand.

def _draw(icon, name, description):
    tokens=description.split(); pos=0; part=0; count=0; members=[]; start=None; point=None
    def finish(closed=False):
        nonlocal members,part
        if members: icon.add_contour(name if part==0 else f"{name}-part{part}",*members,closed=closed)
        members=[];part+=1
    while pos<len(tokens):
        op=tokens[pos];pos+=1
        if op=='M':
            if members: finish()
            point=tuple(map(int,tokens[pos:pos+2]));pos+=2;start=point
        elif op=='Z':
            if point!=start:
                count+=1;eid=f"{name}-{count}";icon.add_line(eid,point,start);members.append(eid);point=start
            finish(True)
        else:
            count+=1;eid=f"{name}-{count}";members.append(eid)
            if op=='L':
                end=tuple(map(int,tokens[pos:pos+2]));pos+=2;icon.add_line(eid,point,end)
            elif op=='C':
                values=list(map(int,tokens[pos:pos+6]));pos+=6;c1=tuple(values[:2]);c2=tuple(values[2:4]);end=tuple(values[4:]);icon.add_bezier(eid,point,(c1,c2,end))
            elif op=='A':
                rx,ry,sweep,x,y=map(int,tokens[pos:pos+5]);pos+=5;end=(x,y);icon.add_arc(eid,point,end,radius_x=rx,radius_y=ry,sweep=bool(sweep))
            point=end
    if members: finish()

class Revision(Solo48):
    icon_id = 'squeeze-sides'
    keyshape = Keyshape.VRECT_L
    exception = {'reason': 'Preserve four grasping fingers, an upright phone and two inward arrows; repeated 2px finger openings and intended hand contacts remain readable.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '917fd3f98ef2e54d05512c7374b0daf79deec2e80238a3c81e157c353f09d619'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'phone', 'M 16 44 L 29 44 A 3 3 0 32 41 L 32 7 A 3 3 0 29 4 L 17 4 A 3 3 0 14 7 L 14 16')
        _draw(self, 'finger-top', 'M 11 17 L 18 17 A 3 3 1 21 20 L 21 20 A 3 3 1 18 23 L 11 23 A 3 3 1 8 20 L 8 20 A 3 3 1 11 17 Z')
        _draw(self, 'finger-mid', 'M 11 23 L 18 23 A 3 3 1 21 26 L 21 26 A 3 3 1 18 29 L 11 29 A 3 3 1 8 26 L 8 26 A 3 3 1 11 23 Z')
        _draw(self, 'finger-low', 'M 11 29 L 18 29 A 3 3 1 21 32 L 21 32 A 3 3 1 18 35 L 11 35 A 3 3 1 8 32 L 8 32 A 3 3 1 11 29 Z')
        _draw(self, 'finger-last', 'M 11 35 L 18 35 A 3 3 1 21 38 L 21 38 A 3 3 1 18 41 L 11 41 A 3 3 1 8 38 L 8 38 A 3 3 1 11 35 Z')
        _draw(self, 'thumb', 'M 32 17 C 40 15 36 31 42 32')
        _draw(self, 'left-arrow', 'M 4 10 L 10 10')
        _draw(self, 'left-arrowhead', 'M 7 7 L 10 10 L 7 13')
        _draw(self, 'right-arrow', 'M 44 10 L 38 10')
        _draw(self, 'right-arrowhead', 'M 41 7 L 38 10 L 41 13')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
