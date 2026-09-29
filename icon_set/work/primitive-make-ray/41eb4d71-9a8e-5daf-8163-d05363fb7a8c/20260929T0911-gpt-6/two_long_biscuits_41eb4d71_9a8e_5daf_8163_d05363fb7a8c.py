from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '41eb4d71-9a8e-5daf-8163-d05363fb7a8c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-long-biscuits/20260929T090755Z-thuan-mac/reference/chef gear biscuits_41eb4d71-9a8e-5daf-8163-d05363fb7a8c.svg'
AUTHOR = "gpt-6"
# Plan: Restore a pair of broad rounded biscuits with a flowing central groove in each.
# Keyshape: VRECT_L; preserve reference arrangement.
# Construction reference: none.

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
    icon_id = 'two-long-biscuits'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'biscuit-a', 'M 14 4 L 14 4 A 6 6 1 20 10 L 20 38 A 6 6 1 14 44 L 14 44 A 6 6 1 8 38 L 8 10 A 6 6 1 14 4 Z')
        _draw(self, 'biscuit-b', 'M 34 4 L 34 4 A 6 6 1 40 10 L 40 38 A 6 6 1 34 44 L 34 44 A 6 6 1 28 38 L 28 10 A 6 6 1 34 4 Z')
        _draw(self, 'groove-a', 'M 14 14 C 11 21 17 27 14 35')
        _draw(self, 'groove-b', 'M 34 14 C 31 21 37 27 34 35')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
