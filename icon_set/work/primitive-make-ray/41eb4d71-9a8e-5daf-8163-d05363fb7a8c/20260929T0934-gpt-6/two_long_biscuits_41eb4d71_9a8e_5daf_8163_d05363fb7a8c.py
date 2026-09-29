from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '41eb4d71-9a8e-5daf-8163-d05363fb7a8c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-long-biscuits/20260929T090755Z-thuan-mac/reference/chef gear biscuits_41eb4d71-9a8e-5daf-8163-d05363fb7a8c.svg'
AUTHOR = "gpt-6"
# Plan: Restore a pair of broad rounded biscuits with a flowing central groove in each.
# Keyshape: SQUARE; preserve reference arrangement.
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
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve two long biscuits and baked grooves; the grooves remain visibly separate at 48px with consistent 4px strokes.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '020fe4f00f3e951d2dd5c7ae6d121f2b637cbab66536f99b5b0daee02665e0ec'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'biscuit-a', 'M 13 6 L 13 6 A 7 7 1 20 13 L 20 35 A 7 7 1 13 42 L 13 42 A 7 7 1 6 35 L 6 13 A 7 7 1 13 6 Z')
        _draw(self, 'biscuit-b', 'M 35 6 L 35 6 A 7 7 1 42 13 L 42 35 A 7 7 1 35 42 L 35 42 A 7 7 1 28 35 L 28 13 A 7 7 1 35 6 Z')
        _draw(self, 'groove-a', 'M 13 15 C 10 21 16 27 13 34')
        _draw(self, 'groove-b', 'M 35 15 C 32 21 38 27 35 34')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
