"""Bounded in-place repair of the frozen first 50 gallery entries.

SOURCE_ICON_ID and SOURCE_PATH are preserved individually in selection.json and
in every edited model. No profiles, validators, or emitted SVGs are patched.
"""
SOURCE_ICON_ID = None
SOURCE_PATH = 'http://127.0.0.1:8000/gallery/failures.html'
AUTHOR = 'gpt-6'
import ast,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
WORK=Path(__file__).parent
selection=json.loads((WORK/'selection.json').read_text())
# Boundary nodes move together throughout each owning contour and its joins.
X={n:{6:4,42:44} for n in (3,5,6,12,13,18,24,25,30,32,34,36,40,45,47,48,50)}
X[7]={11:8,37:40};X[28]={6:8,42:40};X[44]={6:8}
Y={7:{6:8,39:37,42:44},16:{6:4,42:44},17:{6:4,42:44},19:{6:4},21:{41:41,42:44},23:{6:4,42:44},26:{42:44},28:{6:4,42:44},33:{5:8,40:38},44:{6:4,42:44},46:{6:4,42:44}}
KEY={4:'SQUARE',9:'SQUARE',14:'SQUARE',41:'SQUARE'}
# Elliptical quarter-arcs below explicitly own the envelope extremum.
ARCS={
2:{'sun-top':(8,8),'sun-bottom':(8,8),'day-arc':(14,18)},
4:{'arch-left':(16,12),'arch-right':(16,12)},
7:{'body-2':(10,7),'body-4':(10,7),'teat-2':(12,4),'teat-6':(12,4)},
9:{'tub-1':(15,16),'tub-5':(18,8)},
10:{'hood':(14,14),'body-bottom-left':(6,10),'handle-curve':(6,10)},
11:{'hood':(14,14),'body-bottom-left':(6,10),'handle-curve':(6,10)},
13:{'right-wing':(6,22),'left-wing':(6,22)},
14:{'chin':(16,15),'left-ear-lower':(2,6),'left-ear-top':(4,7),'left-ear-inner':(6,5),'right-ear-inner':(6,5),'right-ear-top':(4,7),'right-ear-lower':(2,6)},
15:{'left-wing-upper':(10,8),'left-wing-lower':(10,8),'right-wing-upper':(10,8),'right-wing-lower':(10,8)},
17:{'wick-rise':(8,10)},
20:{'left-upper-out':(6,10),'left-shoulder':(6,10),'left-lower-out':(6,8),'left-lower-base':(8,4),'left-lower-in':(10,6),'right-upper-out':(6,10),'right-shoulder':(6,10),'right-lower-out':(6,8),'right-lower-base':(8,4),'right-lower-in':(10,6)},
21:{'knee':(3,3)},
22:{'tail-top':(8,9),'tail-tip':(5,5),'tail-bottom':(15,2)},
27:{'mist-a':(9,2),'mist-b':(9,2)},
28:{'crest-top':(15,6),'beak-top':(5,8),'beak-hook':(5,8),'chin':(12,14),'nape':(2,25)},
29:{'muzzle-bottom':(8,5),'ear-left':(8,11),'ear-right':(8,11),'ear-bottom-left':(7,1),'ear-bottom-right':(7,1)},
31:{'crest':(6,2)},
33:{'water-left':(10,2),'water-right':(10,2)},
35:{'left-middle-tine':(6,4),'right-middle-tine':(6,4)},
36:{'shell-3':(20,22),'shell-4':(20,22)},
37:{'wings-left-2':(6,6),'wings-left-3':(4,5),'wings-left-5':(5,6),'wings-right-2':(6,6),'wings-right-3':(4,5),'wings-right-5':(5,6)},
38:{'upper-left-2':(3,12),'upper-right-2':(3,12),'lower-left-2':(7,6),'lower-right-2':(7,6)},
40:{'belly-left':(14,16)},
41:{'crown':(11,10),'hem-right':(8,5),'beak-outer':(6,14)},
43:{'trunk-outer':(8,16),'cheek':(6,12),'neck':(6,2),'ear-bottom':(11,9),'back':(4,8)},
44:{'head-right':(13,11),'head-left':(10,11),'spine':(15,16),'tucked-leg':(10,3),'foot':(2,5)},
46:{'upper-left-a':(16,12),'upper-left-b':(16,12),'upper-right-a':(16,8),'upper-right-b':(16,8),'terminal-a':(12,10),'terminal-b':(12,10)},
47:{'outer-forearm':(10,24),'lower-arm-right':(20,14),'lower-arm-left':(20,8)},
48:{'fleece-left-bottom':(4,7),'fleece-left-top':(4,7),'head-top-right':(8,12),'head-bottom':(8,6)},
49:{'breast':(17,14),'tail':(17,7)},
}

def edit(src,xmap,ymap,arcs):
 tree=ast.parse(src);edits=[];lines=src.splitlines(keepends=True);offset=[0]
 for l in lines:offset.append(offset[-1]+len(l))
 def replace(node,value):edits.append((offset[node.lineno-1]+node.col_offset,offset[node.end_lineno-1]+node.end_col_offset,value))
 # Literal coordinate pairs are shared consistently; radii and scalar dimensions
 # are handled separately, never by a whole-drawing transform.
 for node in ast.walk(tree):
  if isinstance(node,ast.Tuple) and len(node.elts)==2 and all(isinstance(v,ast.Constant) and type(v.value)==int for v in node.elts):
   a,b=[v.value for v in node.elts];new=(xmap.get(a,a),ymap.get(b,b))
   if new!=(a,b):replace(node,str(new))
  if isinstance(node,ast.Call) and node.args and isinstance(node.args[0],ast.Constant) and node.args[0].value in arcs:
   name=node.args[0].value;rx,ry=arcs[name]
   fn=node.func.attr if isinstance(node.func,ast.Attribute) else getattr(node.func,'id','')
   if fn=='add_arc':
    keys={k.arg:k for k in node.keywords}
    replace(keys['radius_x'].value,str(rx))
    if 'radius_y' in keys:replace(keys['radius_y'].value,str(ry))
    else:
     pos=offset[node.end_lineno-1]+node.end_col_offset-1;edits.append((pos,pos,f', radius_y={ry}'))
   elif fn in ('arc','A'):
    replace(node.args[3],str(rx))
    if len(node.args)>4:replace(node.args[4],str(ry))
    else:
     pos=offset[node.end_lineno-1]+node.end_col_offset-1;edits.append((pos,pos,f', ry={ry}'))
 for a,b,t in sorted(edits,reverse=True):src=src[:a]+t+src[b:]
 return src

for n,item in enumerate(selection,1):
 path=ROOT/item['file'];src=(WORK/'before-models'/path.name).read_text()
 src=edit(src,X.get(n,{}),Y.get(n,{}),ARCS.get(n,{}))
 if n in KEY:src=re.sub(r'keyshape = Keyshape\.\w+','keyshape = Keyshape.'+KEY[n],src)
 src=re.sub(r'Keyshape\.HRECT_(XL|M|S)\b','Keyshape.HRECT_L',src)
 src=re.sub(r'Keyshape\.VRECT_(XL|M|S)\b','Keyshape.VRECT_L',src)
 if n==2:src=src.replace('(6, 16)','(4, 16)').replace('(42, 40)','(44, 40)').replace('(6, 40)','(4, 40)')
 if n==33:src=src.replace('(6, 38)','(4, 38)').replace('(42, 38)','(44, 38)')
 if n==9:src=src.replace('radius_x=18, radius_y=8','radius_x=18, radius_y=8')
 src=re.sub(r'AUTHOR\s*=\s*[^\n]+',"AUTHOR = 'gpt-6'",src)
 # Keep a repair-specific plan by the owning build method.
 marker='        # Envelope repair: shared boundary nodes and cardinal curve extrema;\n        # retain the subject, grid, stroke, and declared physical joins.\n'
 src=re.sub(r'(    def build\([^\n]+\n)',lambda m:m[0]+marker,src,count=1)
 path.write_text(src)
