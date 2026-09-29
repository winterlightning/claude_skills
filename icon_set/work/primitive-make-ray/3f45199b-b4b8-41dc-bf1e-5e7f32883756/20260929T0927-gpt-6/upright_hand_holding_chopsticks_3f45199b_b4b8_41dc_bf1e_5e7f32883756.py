from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '3f45199b-b4b8-41dc-bf1e-5e7f32883756'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__upright-hand-holding-chopsticks/20260929T090755Z-thuan-mac/reference/chopstick_3f45199b-b4b8-41dc-bf1e-5e7f32883756.svg'
AUTHOR = "gpt-6"
# Plan: Restore two long diagonal chopsticks crossing a rounded closed grip, thumb and wrist.
# Keyshape: SQUARE; preserve reference arrangement.
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
    icon_id = 'upright-hand-holding-chopsticks'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve hand grip, thumb and two diagonal chopsticks with deliberate contact/occlusion at the grasp; small grip openings are intentional.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'ae7b9790b253ac32a7d002b97edf9dc030b3e1bb8fae025a370e226fbb5eaa40'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'outer-hand', 'M 7 42 L 9 33 C 6 23 8 17 15 16 L 26 18 C 29 19 29 23 26 24 C 30 26 28 30 25 31 C 27 35 23 37 21 37 L 22 42')
        _draw(self, 'thumb', 'M 19 13 C 23 8 29 9 30 13 C 31 16 28 18 26 18')
        _draw(self, 'finger', 'M 16 25 L 26 26')
        _draw(self, 'finger-lower', 'M 16 32 L 25 33')
        _draw(self, 'stick-upper', 'M 8 6 L 42 33')
        _draw(self, 'stick-lower-left', 'M 6 13 L 15 19')
        _draw(self, 'stick-lower-right', 'M 29 28 L 40 38')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
