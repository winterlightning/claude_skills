/* Grid-aware fitting of the actual path envelope, including interior curve extrema. */
(() => {
  'use strict';
  const copy=v=>JSON.parse(JSON.stringify(v));
  const clean=n=>Math.round(n*1e6)/1e6;
  const mix=(a,b,t)=>a.map((v,i)=>v+(b[i]-v)*t);
  function roots(p,axis){
    const [a,b,c,d]=p.map(point=>point[axis]);
    const A=-a+3*b-3*c+d,B=2*(a-2*b+c),C=b-a;
    let values=[];
    if(Math.abs(A)<1e-12){if(Math.abs(B)>1e-12)values=[-C/B];}
    else {const disc=B*B-4*A*C;if(disc>=0){const q=Math.sqrt(disc);values=[(-B+q)/(2*A),(-B-q)/(2*A)];}}
    return values.filter(t=>t>1e-8 && t<1-1e-8);
  }
  function at(p,t){const u=1-t;return [0,1].map(i=>u*u*u*p[0][i]+3*u*u*t*p[1][i]+3*u*t*t*p[2][i]+t*t*t*p[3][i]);}
  function split(p,t){
    const a=mix(p[0],p[1],t),b=mix(p[1],p[2],t),c=mix(p[2],p[3],t),d=mix(a,b,t),e=mix(b,c,t),f=mix(d,e,t);
    return [[p[0],a,d,f],[f,e,c,p[3]]];
  }
  function monotoneSegments(p){
    const times=[...roots(p,0),...roots(p,1)].sort((a,b)=>a-b).filter((t,i,list)=>!i || t-list[i-1]>1e-8);
    const pieces=[];let tail=p,previous=0;
    for(const t of times){const [head,rest]=split(tail,(t-previous)/(1-previous));pieces.push(head);tail=rest;previous=t;}
    return [...pieces,tail];
  }
  function arcPoints(p){
    let rx=Math.abs(p.radius_x),ry=Math.abs(p.radius_y);
    const [x1,y1]=p.start,[x2,y2]=p.end,dx=(x1-x2)/2,dy=(y1-y2)/2;
    if(!rx || !ry || (!dx&&!dy))throw Error('An arc collapsed while snapping. Undo or adjust its endpoints before resizing.');
    const lambda=dx*dx/(rx*rx)+dy*dy/(ry*ry);
    if(lambda>1){rx*=Math.sqrt(lambda);ry*=Math.sqrt(lambda);}
    const numerator=rx*rx*ry*ry-rx*rx*dy*dy-ry*ry*dx*dx,denominator=rx*rx*dy*dy+ry*ry*dx*dx;
    let factor=denominator?Math.sqrt(Math.max(0,numerator/denominator)):0;
    if(!!p.large_arc===!!p.sweep)factor=-factor;
    const cx=factor*rx*dy/ry+(x1+x2)/2,cy=-factor*ry*dx/rx+(y1+y2)/2;
    const start=Math.atan2((y1-cy)/ry,(x1-cx)/rx),end=Math.atan2((y2-cy)/ry,(x2-cx)/rx);
    let delta=end-start;if(p.sweep&&delta<0)delta+=2*Math.PI;else if(!p.sweep&&delta>0)delta-=2*Math.PI;
    const points=[p.start,p.end],mod=n=>((n%(2*Math.PI))+2*Math.PI)%(2*Math.PI);
    for(const angle of [0,Math.PI/2,Math.PI,3*Math.PI/2]){
      const offset=delta>=0?mod(angle-start):mod(start-angle);
      if(offset<=Math.abs(delta)+1e-12)points.push([cx+rx*Math.cos(angle),cy+ry*Math.sin(angle)]);
    }
    return points;
  }
  function bounds(primitives){
    const points=[];
    for(const p of primitives){
      points.push(p.start,p.end);
      if(p.kind==='arc')points.push(...arcPoints(p));
      if(p.kind==='bezier'){
        let start=p.start;
        for(const segment of p.segments){const curve=[start,...segment];points.push(segment[2],...[...roots(curve,0),...roots(curve,1)].map(t=>at(curve,t)));start=segment[2];}
      }
    }
    if(!points.length)throw Error('No strokes to resize.');
    const xs=points.map(p=>p[0]),ys=points.map(p=>p[1]);
    const x=Math.min(...xs),y=Math.min(...ys),right=Math.max(...xs),bottom=Math.max(...ys);
    return {x,y,width:right-x,height:bottom-y,cx:(x+right)/2,cy:(y+bottom)/2};
  }
  function fit(primitives,target,strokeWidth=4,reference=primitives){
    const source=bounds(primitives),low=[target[0]+strokeWidth/2,target[1]+strokeWidth/2],high=[target[2]-strokeWidth/2,target[3]-strokeWidth/2];
    if([...low,...high].some(n=>!Number.isInteger(n)) || high.some((n,i)=>n<=low[i]))throw Error('Choose bounds with whole-grid edges and room for the stroke.');
    const origin=[source.x,source.y],extent=[source.width,source.height];
    const scale=extent.map((n,i)=>n>1e-8?(high[i]-low[i])/n:null);
    if(scale.includes(null))throw Error('This icon has a flat dimension that cannot fill the selected keyshape without adding geometry.');
    if(scale.some(n=>!Number.isFinite(n)||n<.05||n>20))throw Error('This keyshape exceeds the supported resize range.');
    const transform=p=>p.map((n,i)=>low[i]+(n-origin[i])*scale[i]);
    // Symmetric rounding retains reflected counterparts on opposite sides of the canvas.
    const snap=p=>p.map((n,i)=>{const center=(low[i]+high[i])/2;return Math.max(low[i],Math.min(high[i],center+Math.sign(n-center)*Math.floor(Math.abs(n-center)+.5)));});
    const result=primitives.map(sourcePrimitive=>{
      const p=copy(sourcePrimitive);p.start=snap(transform(p.start));p.end=snap(transform(p.end));
      if(p.kind==='bezier'){
        let start=sourcePrimitive.start;const segments=[];
        for(const segment of sourcePrimitive.segments){
          // Splitting at extrema preserves the curve exactly before snapping and makes
          // each piece monotone. Mapping handles with its snapped endpoints then keeps
          // its envelope bounded, unlike shifting handles after independently rounding knots.
          for(const piece of monotoneSegments([start,...segment])){
            const curve=piece.map(transform),a=snap(curve[0]),b=snap(curve[3]);
            const control=point=>point.map((n,i)=>Math.abs(curve[3][i]-curve[0][i])>1e-9
              ? clean(a[i]+(n-curve[0][i])*(b[i]-a[i])/(curve[3][i]-curve[0][i])) : a[i]);
            segments.push([control(curve[1]),control(curve[2]),b]);
          }
          start=segment[2];
        }
        p.segments=segments;p.end=[...segments.at(-1)[2]];
      }else if(p.kind==='arc'){
        p.radius_x=Math.max(1,Math.round(p.radius_x*scale[0]));p.radius_y=Math.max(1,Math.round(p.radius_y*scale[1]));
        const hint=reference.find(original=>original.element_id===p.element_id) || sourcePrimitive;
        const dx=Math.abs(hint.end[0]-hint.start[0]),dy=Math.abs(hint.end[1]-hint.start[1]);
        // Cardinal arcs own their endpoint tangents. Independently rounding radii
        // and knots makes a quarter corner overshoot even when both look on-grid.
        if(Math.abs(dx-hint.radius_x)<1e-5 && Math.abs(dy-hint.radius_y)<1e-5){
          p.radius_x=Math.abs(p.end[0]-p.start[0]);p.radius_y=Math.abs(p.end[1]-p.start[1]);
        }else if(dy<1e-8 && Math.abs(dx-2*hint.radius_x)<1e-5){
          p.radius_x=Math.abs(p.end[0]-p.start[0])/2;
        }else if(dx<1e-8 && Math.abs(dy-2*hint.radius_y)<1e-5){
          p.radius_y=Math.abs(p.end[1]-p.start[1])/2;
        }
        if(![p.radius_x,p.radius_y].every(n=>Number.isInteger(n)&&n>0))throw Error('This arc cannot keep its endpoints and radii on the grid at this size. Your drawing is unchanged.');
      }
      return p;
    });
    const actual=bounds(result),edges=[actual.x,actual.y,actual.x+actual.width,actual.y+actual.height],wanted=[...low,...high];
    if(edges.some((n,i)=>Math.abs(n-wanted[i])>1e-5))throw Error('The snapped arcs cannot exactly fit this keyshape. Your drawing is unchanged; adjust the arcs or choose another keyshape.');
    return result;
  }
  window.StrokeFit={bounds,fit,monotoneSegments};
})();
