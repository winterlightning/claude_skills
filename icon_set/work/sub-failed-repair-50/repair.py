"""Batch-specific, source-preserving SUB32 repairs. Never modifies parents."""
from pathlib import Path
import ast,json,sys,textwrap,inspect,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import factories
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/sub-failed-repair-50/batch.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
rows=json.loads((W/'batch.json').read_text())
HELPERS='''
def box(s,n,l,t,r,b,k=3):
    # One rounded rectangle owns all four matching corner radii.
    points=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
    members=[]
    for i,p in enumerate(points):
        q=points[(i+1)%8];name=f"{n}-{i}"
        if i%2:s.add_arc(name,p,q,radius_x=k)
        else:s.add_line(name,p,q)
        members.append(name)
    s.add_contour(n,*members,closed=True)

def circle(s,n,cx,cy,r):
    s.add_arc(n+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
    s.add_arc(n+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
    s.add_contour(n,n+'-top',n+'-bottom',closed=True)
'''
# Each entry is an authored construction, never a scaled parent drawing.
DESIGNS={
1:('VRECT_XL','Can, rounded actuator, two separate spray strokes. Restore diverging spray.','spray-can','''
box(self,'can',4,12,20,30,3)
box(self,'nozzle',8,2,16,12,2)
self.relate('connect','can','nozzle')
self.add_line('spray-upper',(24,5),(28,2))
self.add_line('spray-lower',(26,12),(28,14))
'''),
2:('HRECT_XL','One airplane outline, two mirrored wings, tail and rounded nose.','plane','''
self.add_polyline('upper',(2,10),(8,12),(12,12),(9,4),(15,4),(22,12),(26,12))
self.add_arc('nose',(26,12),(26,20),radius_x=4)
self.add_polyline('lower',(26,20),(22,20),(15,28),(9,28),(12,20),(8,20),(2,22),(5,16),(2,10))
self.relate('connect','upper','nose')
self.relate('connect','lower','nose')
self.relate('connect','upper','lower')
'''),
5:('SQUARE','Smooth circular return arrow with original left-facing arrowhead.','rotate-ccw','''
self.add_arc('lower-left',(2,16),(16,30),radius_x=14,sweep=False)
self.add_arc('right',(16,30),(16,2),radius_x=14,sweep=False)
self.add_arc('upper-left',(16,2),(8,4),radius_x=17,sweep=False)
self.add_contour('return','lower-left','right','upper-left')
self.add_polyline('head',(12,2),(8,4),(12,8))
self.relate('connect','return','head')
'''),
6:('SQUARE','Cursor outline with widened diagonal tail; direction and all corners retained.','mouse-pointer-2','''
self.add_polyline('cursor',(2,2),(30,10),(21,15),(30,24),(24,30),(15,21),(10,30),closed=True)
'''),
7:('VRECT_XL','Up arrow; common axis and mirrored shoulders, constant-width stem.','arrow-big-up','''
axis=16;half_stem=6;half_head=12
self.add_polyline('arrow',(axis-half_head,16),(axis,2),(axis+half_head,16),(axis+half_stem,16),(axis+half_stem,30),(axis-half_stem,30),(axis-half_stem,16),closed=True)
'''),
8:('VRECT_XL','Source trapezoid shopping bag with rounded handle; remove invented side panel.','shopping-bag','''
self.add_polyline('bag',(6,12),(26,12),(28,30),(4,30),closed=True)
self.add_line('handle-left',(10,16),(10,8))
self.add_arc('handle-top',(10,8),(22,8),radius_x=6)
self.add_line('handle-right',(22,8),(22,16))
self.add_contour('handle','handle-left','handle-top','handle-right')
self.relate('connect','bag','handle')
'''),
9:('VRECT_XL','Rounded source shopping bag and arched handle; remove invented flap.','shopping-bag','''
self.add_line('top',(7,12),(25,12))
self.add_line('right',(25,12),(28,26))
self.add_arc('corner-r',(28,26),(24,30),radius_x=4)
self.add_line('base',(24,30),(8,30))
self.add_arc('corner-l',(8,30),(4,26),radius_x=4)
self.add_line('left',(4,26),(7,12))
self.add_contour('bag','top','right','corner-r','base','corner-l','left',closed=True)
self.add_line('handle-left',(10,15),(10,8))
self.add_arc('handle-top',(10,8),(22,8),radius_x=6)
self.add_line('handle-right',(22,8),(22,15))
self.add_contour('handle','handle-left','handle-top','handle-right')
self.relate('connect','bag','handle')
'''),
12:('HRECT_XL','Laptop screen and base, eight-unit centerline separation at base.','laptop','''
box(self,'screen',4,4,28,20,3)
self.add_polyline('base',(4,20),(2,28),(30,28),(28,20))
self.relate('connect','screen','base')
'''),
13:('HRECT_XL','Battery shell with attached eight-unit-wide terminal.','battery','''
box(self,'body',2,4,22,28,3)
self.add_polyline('terminal',(22,10),(30,10),(30,22),(22,22))
self.relate('connect','body','terminal')
'''),
14:('VRECT_XL','Battery shell, attached terminal and open lightning bolt.','battery-charging','''
box(self,'body',4,10,28,30,3)
self.add_polyline('terminal',(10,10),(10,2),(22,2),(22,10))
self.relate('connect','body','terminal')
self.add_polyline('charge',(18,16),(13,21),(19,21),(14,25))
'''),
15:('VRECT_XL','Battery body and rounded attached terminal with full-size opening.','battery','''
box(self,'body',4,10,28,30,2)
self.add_line('terminal-left',(10,10),(10,5))
self.add_arc('terminal-tl',(10,5),(13,2),radius_x=3)
self.add_line('terminal-top',(13,2),(19,2))
self.add_arc('terminal-tr',(19,2),(22,5),radius_x=3)
self.add_line('terminal-right',(22,5),(22,10))
self.add_contour('terminal','terminal-left','terminal-tl','terminal-top','terminal-tr','terminal-right')
self.relate('connect','body','terminal')
'''),
16:('VRECT_XL','Round-bottom flask with symmetric flowing shoulders and eight-unit neck.','flask-round','''
self.add_line('neck-left',(12,2),(12,7))
self.add_bezier('shoulder-left',(12,7),((12,11),(4,11),(4,18)))
self.add_arc('bowl',(4,18),(28,18),radius_x=12,sweep=False)
self.add_bezier('shoulder-right',(28,18),((28,11),(20,11),(20,7)))
self.add_line('neck-right',(20,7),(20,2))
self.add_contour('flask','neck-left','shoulder-left','bowl','shoulder-right','neck-right')
self.add_line('rim',(9,2),(23,2))
self.relate('connect','flask','rim')
'''),
17:('HRECT_XL','Bed posts and two mattress rails; eight-unit rail spacing.','bed','''
self.add_line('headpost',(2,4),(2,28))
self.add_line('footpost',(30,16),(30,28))
self.add_line('mattress-top',(2,16),(30,16))
self.add_line('mattress-bottom',(2,24),(30,24))
for rail in ('mattress-top','mattress-bottom'):
    for post in ('headpost','footpost'):self.relate('connect',rail,post)
'''),
18:('VRECT_XL','Bell with separate knob, tangent dome and mirrored flared hem, curved clapper.','bell','''
self.add_dot('knob',(16,2))
self.add_arc('dome',(8,17),(24,17),radius_x=8)
self.add_line('right-wall',(24,17),(24,18))
self.add_arc('right-flare',(24,18),(28,22),radius_x=4,sweep=False)
self.add_line('hem',(28,22),(4,22))
self.add_arc('left-flare',(4,22),(8,18),radius_x=4,sweep=False)
self.add_line('left-wall',(8,18),(8,17))
self.add_contour('bell','dome','right-wall','right-flare','hem','left-flare','left-wall',closed=True)
self.add_arc('clapper',(13,29),(19,29),radius_x=3,radius_y=1,sweep=False)
'''),
23:('HRECT_M','Almond eye with ascending slash as in source, joined exactly to outline.','eye-off','''
self.add_bezier('top-left',(2,16),((6,10),(10,8),(16,8)))
self.add_bezier('top-right',(16,8),((22,8),(26,10),(30,16)))
self.add_bezier('bottom-right',(30,16),((26,22),(22,24),(16,24)))
self.add_bezier('bottom-left',(16,24),((10,24),(6,22),(2,16)))
self.add_contour('eye','top-left','top-right','bottom-right','bottom-left',closed=True)
# Opposite points on the two symmetric cubic arcs at t=1/2.
self.add_line('slash',(9,22),(23,10))
self.relate('connect','eye','slash')
'''),
25:('VRECT_XL','Closed book from source: cover, curved lower binding, no invented vertical divider.','book','''
self.add_line('cover-top',(8,2),(28,2))
self.add_line('cover-right',(28,2),(28,22))
self.add_line('page-top',(28,22),(8,22))
self.add_arc('binding',(8,22),(4,26),radius_x=4,sweep=False)
self.add_line('spine',(4,26),(4,6))
self.add_arc('cover-corner',(4,6),(8,2),radius_x=4)
self.add_contour('cover','cover-top','cover-right','page-top','binding','spine','cover-corner',closed=True)
self.add_arc('lower-binding',(4,26),(8,30),radius_x=4,sweep=False)
self.add_line('bottom',(8,30),(28,30))
self.add_arc('pages',(28,30),(28,22),radius_x=8,sweep=True)
self.add_contour('pages-bottom','lower-binding','bottom','pages')
self.relate('connect','cover','pages-bottom')
'''),
26:('HRECT_XL','Open book: two matching bowed pages and single central fold.','book-open','''
self.add_bezier('left-top',(2,6),((6,3),(12,3),(16,7)))
self.add_bezier('right-top',(16,7),((20,3),(26,3),(30,6)))
self.add_line('right-edge',(30,6),(30,26))
self.add_bezier('right-bottom',(30,26),((26,23),(20,23),(16,28)))
self.add_bezier('left-bottom',(16,28),((12,23),(6,23),(2,26)))
self.add_line('left-edge',(2,26),(2,6))
self.add_contour('pages','left-top','right-top','right-edge','right-bottom','left-bottom','left-edge',closed=True)
self.add_line('fold',(16,7),(16,28))
self.relate('connect','pages','fold')
'''),
28:('SQUARE','Briefcase, rounded handle, flap seam and central clasp; retain all parts.','briefcase-business','''
box(self,'body',2,10,30,30,3)
box(self,'handle',10,2,22,10,3)
self.add_line('flap',(2,18),(30,18))
self.add_line('clasp',(16,18),(16,23))
self.relate('connect','body','handle')
self.relate('connect','body','flap')
self.relate('connect','flap','clasp')
'''),
32:('VRECT_XL','Two overlapping buildings, baseline and short window dash.','building','''
self.add_polyline('back',(7,30),(7,2),(19,2),(19,10))
self.add_polyline('front',(14,30),(14,10),(28,10),(28,30))
self.add_line('ground',(4,30),(28,30))
self.add_line('window',(21,17),(22,17))
self.relate('connect','back','front')
self.relate('connect','back','ground')
self.relate('connect','front','ground')
'''),
33:('VRECT_XL','Sloping building and original short entrance marker; no invented box door.','building','''
self.add_line('left',(8,2),(8,30))
self.add_polyline('roof-wall',(8,6),(28,18),(28,30))
self.add_line('base',(4,30),(28,30))
self.add_line('door',(18,24),(18,30))
self.relate('connect','left','roof-wall')
self.relate('connect','left','base')
self.relate('connect','roof-wall','base')
self.relate('connect','door','base')
'''),
34:('VRECT_XL','Front bus: rounded body, window rail, two headlights and two legs.','bus-front','''
box(self,'body',4,2,28,26,3)
self.add_line('window',(4,12),(28,12))
self.relate('connect','body','window')
for x in (10,22):
    self.add_dot(f'headlight-{x}',(x,19))
    self.add_line(f'wheel-{x}',(x,26),(x,30))
    self.relate('connect','body',f'wheel-{x}')
'''),
36:('HRECT_XL','Camera body with raised housing, equal corners, centered round lens.','camera','''
self.add_polyline('top',(5,10),(8,10),(12,4),(20,4),(24,10),(27,10))
self.add_arc('tr',(27,10),(30,13),radius_x=3)
self.add_line('right',(30,13),(30,25))
self.add_arc('br',(30,25),(27,28),radius_x=3)
self.add_line('bottom',(27,28),(5,28))
self.add_arc('bl',(5,28),(2,25),radius_x=3)
self.add_line('left',(2,25),(2,13))
self.add_arc('tl',(2,13),(5,10),radius_x=3)
self.relate('connect','top','tr');self.relate('connect','top','tl')
self.add_contour('sides','tr','right','br','bottom','bl','left','tl')
circle(self,'lens',16,18,4)
'''),
38:('HRECT_XL','Engine outline, top stem and cap, left shaft and end marker.','car','''
self.add_polyline('body',(2,16),(10,16),(10,12),(22,12),(26,18),(30,18),(30,28),(15,28),(10,24),(2,24))
self.add_line('end',(2,12),(2,28))
self.add_line('stem',(16,4),(16,12))
self.add_line('cap',(11,4),(21,4))
self.relate('connect','body','end')
self.relate('connect','body','stem')
self.relate('connect','stem','cap')
'''),
40:('HRECT_XL','Rounded card with original short horizontal mark.','laptop','''
box(self,'card',2,4,30,28,3)
self.add_line('mark',(20,20),(22,20))
'''),
}
PATCHES={
24:('Widen bone shaft symmetrically to eight units; retain four round lobes.','bone',{'(9, 13)':'(9, 12)','(23, 13)':'(23, 12)','(9, 19)':'(9, 20)','(23, 19)':'(23, 20)'}),
43:('Integer-radius paired muzzle arcs; preserve all face parts.','cat',{'(11, 21)':'(10, 21)','(21, 21)':'(22, 21)','radius_x=2.5':'radius_x=3','radius_y=2.5':'radius_y=3'}),
49:('Move both slanted eyes up one unit, preserve circular head and asymmetric hair.','baby',{'(11, 22)':'(11, 21)','(13, 23)':'(13, 22)','(20, 23)':'(20, 22)','(21, 22)':'(21, 21)'}),
50:('Restore exact top and bottom envelope, align stalk junction tangent.','none',{'(15, 27)':'(15, 28)','(22, 27)':'(22, 28)','(8, 27)':'(8, 28)','(27, 5)':'(27, 4)','(29, 5)':'(29, 4)','(29, 12)':'(28, 15)'}),
}
def main():
    existing=json.loads((W/'candidates.json').read_text()) if (W/'candidates.json').exists() else {}
    out={}
    for row in rows:
        n=row['number']
        if n not in DESIGNS and n not in PATCHES:continue
        parent=row['icon']
        if str(n) in existing:
            info=existing[str(n)];path=Path(info['python_source']);uid=info['icon']
            # Recreate from the original snapshot on each refinement.
            text=Path(row['python_source']).read_text();tree=ast.parse(text)
            cls=next(v for v in tree.body if isinstance(v,ast.ClassDef))
            cls.name='RepairVariant';cls.body.insert(0,ast.Assign([ast.Name('variant_of',ast.Store())],ast.Constant(parent)))
            cls.body.insert(0,ast.Assign([ast.Name('variant_label',ast.Store())],ast.Constant('Centerline and source fidelity repair')))
            for v in cls.body:
                if isinstance(v,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='icon_id' for t in v.targets):v.value=ast.Constant(uid)
        else:
            path,uid,text=prepare_variant(parent,'sub','Centerline and source fidelity repair');tree=ast.parse(text)
            mod=sys.modules[factories()[parent].__module__];sid=mod.SOURCE_ICON_ID
            if sid:path=path.with_name(path.stem+'_'+sid.replace('-','_')+'.py')
            cls=next(v for v in tree.body if isinstance(v,ast.ClassDef))
        if n in DESIGNS:
            shape,plan,ref,body=DESIGNS[n]
            for v in cls.body:
                if isinstance(v,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='keyshape' for t in v.targets):v.value=ast.Attribute(ast.Name('Keyshape',ast.Load()),shape,ast.Load())
            build=next(v for v in cls.body if isinstance(v,ast.FunctionDef) and v.name=='build');build.body=ast.parse(textwrap.dedent(body)).body
            tree.body.extend(ast.parse(HELPERS).body)
        else:
            plan,ref,replacements=PATCHES[n]
            ast.fix_missing_locations(tree)
            code=ast.unparse(tree)
            for old,new in replacements.items():
                assert old in code,(n,old)
                code=code.replace(old,new)
            tree=ast.parse(code)
        tree.body.append(ast.Assign([ast.Name('REPAIR_PLAN',ast.Store())],ast.Constant(plan)))
        tree.body.append(ast.Assign([ast.Name('CONSTRUCTION_REFERENCE',ast.Store())],ast.Constant(ref)))
        ast.fix_missing_locations(tree)
        path.write_text('# Independent repair; parent preserved.\n'+ast.unparse(tree)+'\n')
        out[str(n)]=dict(number=n,parent=parent,icon=uid,python_source=str(path),plan=plan,reference=ref)
    (W/'candidates.json').write_text(json.dumps(out,indent=2));print('Authored',len(out),'candidates')
if __name__=='__main__':main()
