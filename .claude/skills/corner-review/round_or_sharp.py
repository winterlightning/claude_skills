"""round_or_sharp.py BATCH_JSON ICON [--round X,Y ...] [--sharp X,Y ...]
-> JSON {"paths": {path id: {old, new}}, "missing": [...]}: the sharp output with each --round corner put back to the
input's own arc (same radius, same end points), or, at a plain line join with no input arc, drawn with a small
round fillet (the input's round join), and each --sharp corner (one the sharp output kept round) drawn as a
point at its apex, each --cut X,Y[:R] join kept sharp with its point cut flat R u (default 2) past the join, and each --slice X,Y:A,B point shaved flat with the keyshape cut of its mirrored partner A,B
(":rot" for a point-symmetric pair, ":move" for a repeated shape). X,Y is the corner's apex as the sheet and the logs give it. "missing" lists
corners not found."""
import copy, json, math, os, re, sys

TOL = 0.6


def parse(d):
    """Absolute M/L/H/V/A/C/Z path -> list of subpaths, each {"start": pt, "segs": [(cmd, args, end)], "closed": bool}.
    H and V become L; a number after a command repeats it (after M it means L)."""
    toks = re.findall(r"[MLHVACZ]|-?(?:\d+\.?\d*|\.\d+)(?:e-?\d+)?", d)
    subs, i, cur, last, at = [], 0, None, None, (0.0, 0.0)
    while i < len(toks):
        c = toks[i]
        if c in "MLHVACZ":
            i += 1
        else:
            c = "L" if last == "M" else last
        last = c
        n = {"M": 2, "L": 2, "H": 1, "V": 1, "A": 7, "C": 6, "Z": 0}[c]
        args = [float(t) for t in toks[i:i + n]]; i += n
        if c == "H":
            c, args = "L", [args[0], at[1]]
        elif c == "V":
            c, args = "L", [at[0], args[0]]
        if c == "M":
            cur = {"start": tuple(args), "segs": [], "closed": False}; subs.append(cur); at = tuple(args)
        elif c == "Z":
            cur["closed"] = True; at = cur["start"]
        else:
            cur["segs"].append((c, args, tuple(args[-2:]))); at = tuple(args[-2:])
    return subs


def fmt(v):
    return ("%.3f" % v).rstrip("0").rstrip(".")


def pt(p):
    return fmt(p[0]) + " " + fmt(p[1])


def emit(subs):
    out = []
    for s in subs:
        out.append("M" + pt(s["start"]))
        for c, a, e in s["segs"]:
            if c == "A":
                out.append("A%s %s %s %d %d %s" % (fmt(a[0]), fmt(a[1]), fmt(a[2]), a[3], a[4], pt(e)))
            elif c == "C":
                out.append("C" + " ".join(fmt(v) for v in a))
            else:
                out.append("L" + pt(e))
        if s["closed"]:
            out.append("Z")
    return "".join(out)


def near(a, b, t=TOL):
    return math.dist(a, b) <= t


def arc_center(s, e, r, large, sweep):
    mx, my = (s[0] + e[0]) / 2, (s[1] + e[1]) / 2
    dx, dy = e[0] - s[0], e[1] - s[1]
    q = math.hypot(dx, dy)
    h = math.sqrt(max(r * r - (q / 2) ** 2, 0))
    ux, uy = -dy / q, dx / q
    sign = 1 if large != sweep else -1
    return (mx + sign * h * ux, my + sign * h * uy)


def arc_apex(s, e, rx, ry, rot, large, sweep):
    """Where the arc's two end tangents meet (None for a rotated ellipse or a half circle)."""
    if abs(rot) > 1e-6 and abs(rx - ry) > 1e-6:
        return None
    k = rx / ry
    S, E = (s[0], s[1] * k), (e[0], e[1] * k)
    if math.dist(S, E) > 2 * rx + 1e-6:
        return None
    cx, cy = arc_center(S, E, rx, large, sweep)
    mx, my = (S[0] + E[0]) / 2 - cx, (S[1] + E[1]) / 2 - cy
    m = math.hypot(mx, my)
    if m < 1e-6:
        return None
    return (cx + mx * rx * rx / m / m, (cy + my * rx * rx / m / m) / k)


def input_arcs(paths):
    """Every arc of the input with its apex (where its two tangents meet)."""
    arcs = []
    for d in paths.values():
        for sub in parse(d):
            p = sub["start"]
            for c, a, e in sub["segs"]:
                if c == "A":
                    apex = arc_apex(p, e, a[0], a[1], a[2], int(a[3]), int(a[4]))
                    if apex:
                        arcs.append({"s": p, "e": e, "rx": a[0], "ry": a[1], "rot": a[2], "large": int(a[3]),
                                     "sweep": int(a[4]), "apex": apex})
                p = e
    return arcs


def on_segment(q, a, b):
    """q lies on the straight segment a-b."""
    ab, aq = math.dist(a, b), math.dist(a, q) + math.dist(q, b)
    return abs(aq - ab) < 0.05


def arc_seg(arc, frm, to):
    sweep = arc["sweep"] if near(frm, arc["s"], 0.05) else 1 - arc["sweep"]
    return ("A", [arc["rx"], arc["ry"], arc["rot"], arc["large"], sweep, *to], to)


def keep(paths, arc, p):
    """Rewrite the sharp paths so the corner at p becomes `arc` again. Returns True when done."""
    s, e = arc["s"], arc["e"]
    # ends of straight segments touching p: (path id, sub index, seg index, 'in'|'out', other end)
    ends = []
    for pid, subs in paths.items():
        for si, sub in enumerate(subs):
            prev = sub["start"]
            for gi, (c, a, end) in enumerate(sub["segs"]):
                if c == "L" and near(end, p):
                    ends.append((pid, si, gi, "in", prev))
                if c == "L" and near(prev, p):
                    ends.append((pid, si, gi, "out", end))
                prev = end
            if sub["closed"] and near(sub["start"], p) and not near(prev, p):
                ends.append((pid, si, len(sub["segs"]), "in", prev))       # the Z segment
            if sub["closed"] and near(prev, p) and not near(sub["start"], p):
                ends.append((pid, si, len(sub["segs"]), "out", sub["start"]))  # Z leaves p
    # pick an incoming and an outgoing straight end whose lines hold the two arc ends
    def holder(q, kinds):
        for en in ends:
            if en[3] in kinds and on_segment(q, en[4], p):
                return en
    found = None
    for a_end, b_end in ((s, e), (e, s)):
        hin, hout = holder(a_end, ("in",)), holder(b_end, ("out",))
        if hin and hout:
            found = (a_end, b_end, hin, hout)
            break
    if not found:
        for a_end, b_end in ((s, e), (e, s)):
            h1, h2 = holder(a_end, ("in",)), holder(b_end, ("in",))
            if h1 and h2 and h1[:3] != h2[:3]:
                found = (a_end, b_end, h1, None)
                break
    if not found:
        return False
    a_end, b_end, hin, hout = found
    pid, si, gi, _, _ = hin
    sub = paths[pid][si]
    if hout is None:                       # two path ends meet at p: first path takes the arc, second is cut short
        sub["segs"][gi] = ("L", list(a_end), a_end)
        sub["segs"].insert(gi + 1, arc_seg(arc, a_end, b_end))
        q = holder(b_end, ("in",))
        qs = paths[q[0]][q[1]]
        qs["segs"][q[2]] = ("L", list(b_end), b_end)
        return True
    if gi == len(sub["segs"]):             # corner at the start of a closed subpath: open it at the arc
        sub["segs"].append(("L", list(a_end), a_end))
        sub["segs"].append(arc_seg(arc, a_end, b_end))
        sub["start"] = b_end
        sub["closed"] = True
        return True
    if (hout[0], hout[1]) == (pid, si) and hout[2] == gi + 1:      # also the Z edge (gi + 1 == len(segs))
        sub["segs"][gi] = ("L", list(a_end), a_end)
        sub["segs"].insert(gi + 1, arc_seg(arc, a_end, b_end))
        return True
    if (hout[0], hout[1]) != (pid, si) or hout[2] != 0:
        # outgoing starts a later subpath at p ("...L p M p L n"): join them through the arc
        osub = paths[hout[0]][hout[1]]
        if hout[2] == 0 and near(osub["start"], p):
            sub["segs"][gi] = ("L", list(a_end), a_end)
            sub["segs"].insert(gi + 1, arc_seg(arc, a_end, b_end))
            osub["start"] = b_end
            return True
    return False


def _meet(a, da, b, db):
    """Where the line through a (direction da) meets the line through b (direction db), or None."""
    den = da[0] * db[1] - da[1] * db[0]
    if abs(den) < 1e-9:
        return None
    t = ((b[0] - a[0]) * db[1] - (b[1] - a[1]) * db[0]) / den
    return (a[0] + da[0] * t, a[1] + da[1] * t)


def sharpen(paths, p):
    """Turn the round corner of the sharp output at p into a point. The point is where the straight edges on both
    sides of the arc meet (so a lopsided arc still gives the true corner), else the arc's own apex.
    Returns True when done."""
    for subs in paths.values():
        for sub in subs:
            pts = [sub["start"]] + [e for _, _, e in sub["segs"]]
            n = len(sub["segs"])
            for gi, (c, a, end) in enumerate(sub["segs"]):
                if c != "A":
                    continue
                prev = pts[gi]
                corner = None
                before = pts[gi - 1] if gi > 0 else (pts[-1] if sub["closed"] and not near(pts[-1], prev, 0.01) else
                                                      (pts[-2] if sub["closed"] and n > 1 else None))
                if gi + 1 < n:
                    after = sub["segs"][gi + 1][2] if sub["segs"][gi + 1][0] == "L" else None
                elif sub["closed"]:
                    after = sub["start"] if not near(sub["start"], end, 0.01) else (pts[1] if n > 1 else None)
                else:
                    after = None
                if before is not None and after is not None and (gi == 0 or sub["segs"][gi - 1][0] == "L"):
                    corner = _meet(prev, (prev[0] - before[0], prev[1] - before[1]),
                                   end, (after[0] - end[0], after[1] - end[1]))
                apex = corner if corner and near(corner, p, 1.0) else arc_apex(prev, end, a[0], a[1], a[2], int(a[3]), int(a[4]))
                if apex and near(apex, p, 1.0):
                    sub["segs"][gi:gi + 1] = [("L", list(apex), apex), ("L", list(end), end)]
                    return True
    return False


FILLET = 0.25      # centreline radius of a round join: stroked 4 wide its outside is a 2.25 turn, the input's 2 near enough


def _split_c(p0, a, t):
    """de Casteljau: cubic p0, a=[c1x,c1y,c2x,c2y,ex,ey] split at t -> (first half args, second half args)."""
    P = [p0, tuple(a[0:2]), tuple(a[2:4]), tuple(a[4:6])]
    lerp = lambda u, v: (u[0] + (v[0] - u[0]) * t, u[1] + (v[1] - u[1]) * t)
    p01, p12, p23 = lerp(P[0], P[1]), lerp(P[1], P[2]), lerp(P[2], P[3])
    p012, p123 = lerp(p01, p12), lerp(p12, p23)
    m = lerp(p012, p123)
    return [*p01, *p012, *m], [*p123, *p23, *P[3]]


def _bez(p0, a, t):
    P = [p0, tuple(a[0:2]), tuple(a[2:4]), tuple(a[4:6])]
    s = 1 - t
    return tuple(s ** 3 * P[0][i] + 3 * s * s * t * P[1][i] + 3 * s * t * t * P[2][i] + t ** 3 * P[3][i] for i in (0, 1))


def _t_at(p0, a, at_end, d):
    """Parameter of the cubic point about d away (along the curve) from its end (at_end) or start."""
    pts = [_bez(p0, a, k / 200) for k in range(201)]
    if at_end:
        pts = pts[::-1]
    run = 0.0
    for k in range(1, 201):
        run += math.dist(pts[k - 1], pts[k])
        if run >= d:
            return 1 - k / 200 if at_end else k / 200
    return None


def _arc_to_cubics(p0, a):
    """SVG elliptical arc from p0 with args [rx, ry, rot, large, sweep, x, y] -> list of ("C", args, end) segments."""
    rx, ry, rot, large, sweep, x, y = a
    x1, y1 = p0
    if rx == 0 or ry == 0:
        return [("L", [x, y], (x, y))]
    phi = math.radians(rot)
    cp, sp = math.cos(phi), math.sin(phi)
    dx, dy = (x1 - x) / 2, (y1 - y) / 2
    x1p, y1p = cp * dx + sp * dy, -sp * dx + cp * dy
    rx, ry = abs(rx), abs(ry)
    lam = x1p ** 2 / rx ** 2 + y1p ** 2 / ry ** 2
    if lam > 1:
        rx, ry = rx * math.sqrt(lam), ry * math.sqrt(lam)
    num = rx * rx * ry * ry - rx * rx * y1p * y1p - ry * ry * x1p * x1p
    den = rx * rx * y1p * y1p + ry * ry * x1p * x1p
    co = math.sqrt(max(num / den, 0)) * (-1 if int(large) == int(sweep) else 1)
    cxp, cyp = co * rx * y1p / ry, -co * ry * x1p / rx
    cx, cy = cp * cxp - sp * cyp + (x1 + x) / 2, sp * cxp + cp * cyp + (y1 + y) / 2
    ang = lambda ux, uy, vx, vy: math.atan2(ux * vy - uy * vx, ux * vx + uy * vy)
    t1 = ang(1, 0, (x1p - cxp) / rx, (y1p - cyp) / ry)
    dt = ang((x1p - cxp) / rx, (y1p - cyp) / ry, (-x1p - cxp) / rx, (-y1p - cyp) / ry)
    if not sweep and dt > 0:
        dt -= 2 * math.pi
    elif sweep and dt < 0:
        dt += 2 * math.pi
    n = max(1, math.ceil(abs(dt) / (math.pi / 2)))
    step = dt / n
    k = 4 / 3 * math.tan(step / 4)
    pt_at = lambda t: (cx + rx * math.cos(t) * cp - ry * math.sin(t) * sp, cy + rx * math.cos(t) * sp + ry * math.sin(t) * cp)
    der = lambda t: (-rx * math.sin(t) * cp - ry * math.cos(t) * sp, -rx * math.sin(t) * sp + ry * math.cos(t) * cp)
    out, t = [], t1
    for i in range(n):
        a0, a1 = t, t + step
        P0, P3 = pt_at(a0), pt_at(a1)
        d0, d1 = der(a0), der(a1)
        c1 = (P0[0] + k * d0[0], P0[1] + k * d0[1])
        c2 = (P3[0] - k * d1[0], P3[1] - k * d1[1])
        end = (x, y) if i == n - 1 else P3
        out.append(("C", [*c1, *c2, *end], end))
        t = a1
    return out


def clip_d(icon):
    """The sharp output's keyshape-cut clip path d (its first subpath is the big frame, the rest are the cuts)."""
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "corner_processing"))
    svg = open(os.path.join(root, "outputs", "solo48", "sharp", icon), encoding="utf-8").read()
    m = re.search(r'<clipPath id="keyshape-cut">\s*<path d="([^"]+)"', svg)
    return m.group(1) if m else None


def slice_like(clip, x, a, how="mirror"):
    """Copy the keyshape cut that shaves corner a onto corner x, so a pair is shaved flat alike: "mirror" = the
    reflection that swaps a and x, "rot" = the half turn about their midpoint (point symmetry), "move" = shifted
    from a to x (a repeated shape). -> new clip d or None."""
    subs = parse(clip)
    holes = subs[1:]
    if not holes:
        return None
    dist = lambda sub: min(math.dist(q, a) for q in [sub["start"]] + [e for _, _, e in sub["segs"]])
    hole = min(holes, key=dist)
    if dist(hole) > 6:
        return None
    mx, my = (a[0] + x[0]) / 2, (a[1] + x[1]) / 2
    L = math.dist(a, x)
    if L < 1e-6:
        return None
    nx, ny = (x[0] - a[0]) / L, (x[1] - a[1]) / L
    def mirror(q):
        if how == "rot":
            return (2 * mx - q[0], 2 * my - q[1])
        if how == "move":
            return (q[0] + x[0] - a[0], q[1] + x[1] - a[1])
        k = (q[0] - mx) * nx + (q[1] - my) * ny
        return (q[0] - 2 * k * nx, q[1] - 2 * k * ny)
    pts = [hole["start"]] + [e for c, _, e in hole["segs"]]
    if any(c != "L" for c, _, _ in hole["segs"]):
        return None
    new = [mirror(q) for q in pts]
    copy = {"start": new[0], "segs": [("L", list(q), q) for q in new[1:]], "closed": True}
    return emit(subs + [copy])


CUT_REACH = 2.0   # u past the join: a cut tip ends where the input's round join reached (half the stroke width)
HALF_W = 2.0
CUT_MIN_DEPTH = 0.4   # u: shortest trim of a cut join (the cut then ends 1.6 u past it)


def round_join(paths, p, cut=None):
    """round_join_sub on every subpath until one takes it; a subpath it fails on is left exactly as it was."""
    for subs in paths.values():
        for k, sub in enumerate(subs):
            keep = copy.deepcopy(sub)
            got = round_join_sub(sub, p, cut)
            if got:
                return got
            subs[k].clear()
            subs[k].update(keep)
    return False


def round_join_sub(sub, p, cut=None):
    """With cut (u past the join, e.g. CUT_REACH): the join stays sharp but its mitre point is cut flat at that
    reach, perpendicular to the corner's bisector - each arm is shortened a little and a short straight edge joins
    them, so the stroke's outer edges keep their lines up to the cut (the same ink as the point sliced flat).

    A plain line join at p (no arc in the input; its round look came from stroke-linejoin) drawn round: a small
    fillet arc (radius FILLET) replaces the vertex, so the stroke turns round instead of growing a mitre point.
    Works between straight (L) and cubic (C) segments. Returns True when done."""
    for sub in [sub]:
        if True:
            pts = [sub["start"]] + [e for _, _, e in sub["segs"]]
            if sub["closed"] and near(pts[-1], p, 0.3) and not near(pts[-1], sub["start"], 0.01):
                sub["segs"].append(("L", list(sub["start"]), sub["start"]))   # the Z edge leaves p: make it real
                pts.append(sub["start"])
            hit = next((gi for gi, q in enumerate(pts[1:-1]) if near(q, p, 0.3)), None)
            if hit is None and sub["closed"] and near(sub["start"], p, 0.3):
                if not near(pts[-1], sub["start"], 0.01):          # make the Z edge a real segment, then rotate
                    sub["segs"].append(("L", list(sub["start"]), sub["start"]))
                sub["start"] = sub["segs"][0][2]
                sub["segs"] = sub["segs"][1:] + sub["segs"][:1]
                pts = [sub["start"]] + [e for _, _, e in sub["segs"]]
                hit = len(sub["segs"]) - 2
            if hit is None:
                continue
            for k in (hit + 1, hit):                             # an arc next to the join: as cubics first
                if sub["segs"][k][0] == "A":
                    sub["segs"][k:k + 1] = _arc_to_cubics(pts[k], sub["segs"][k][1])
                    if k == hit:
                        hit += len(sub["segs"]) - len(pts) + 1
                    pts = [sub["start"]] + [e for _, _, e in sub["segs"]]
            (c1, a1, q), (c2, a2, e2) = sub["segs"][hit], sub["segs"][hit + 1]
            if c1 not in "LC" or c2 not in "LC":
                return False
            prev = pts[hit]
            din = (q[0] - (a1[2] if c1 == "C" else prev[0]), q[1] - (a1[3] if c1 == "C" else prev[1]))
            dout = ((a2[0] if c2 == "C" else e2[0]) - q[0], (a2[1] if c2 == "C" else e2[1]) - q[1])
            if c1 == "C" and math.hypot(*din) < 1e-9:              # control point on the join: use the other one
                din = (q[0] - a1[0], q[1] - a1[1])
            if c2 == "C" and math.hypot(*dout) < 1e-9:
                dout = (a2[2] - q[0], a2[3] - q[1])
            li, lo = math.hypot(*din), math.hypot(*dout)
            if li < 1e-9 or lo < 1e-9:
                return False
            cosv = -(din[0] * dout[0] + din[1] * dout[1]) / li / lo        # cos of the angle between the arms
            theta = math.acos(max(-1, min(1, cosv)))
            if theta > math.radians(175):
                return False                                            # straight through: no corner
            cusp = theta < math.radians(20)                    # arms leave p together: a U-turn, not a fillet
            if cut is not None:
                # both arms trimmed to the same depth h behind q along the corner's bisector, so the short edge
                # between them is square to the point even where the arms curve; the cut then lies HALF_W - h
                # past q (h >= CUT_MIN_DEPTH keeps that edge long enough to steer the two new mitres)
                bx, by = din[0] / li - dout[0] / lo, din[1] / li - dout[1] / lo
                bl = math.hypot(bx, by)
                if bl < 1e-9:
                    return False
                bx, by = bx / bl, by / bl
                h = max(CUT_MIN_DEPTH, HALF_W - cut)
                depth = lambda z: (q[0] - z[0]) * bx + (q[1] - z[1]) * by
                if c1 == "L":
                    k = depth(prev)
                    if k <= h:
                        return False
                    s1 = (q[0] + (prev[0] - q[0]) * h / k, q[1] + (prev[1] - q[1]) * h / k)
                    seg1 = ("L", list(s1), s1)
                else:
                    t = next((1 - i / 400 for i in range(1, 401) if depth(_bez(prev, a1, 1 - i / 400)) >= h), None)
                    if t is None:
                        return False
                    first, _ = _split_c(prev, a1, t)
                    s1 = tuple(first[4:6]); seg1 = ("C", first, s1)
                if c2 == "L":
                    k = depth(e2)
                    if k <= h:
                        return False
                    s2 = (q[0] + (e2[0] - q[0]) * h / k, q[1] + (e2[1] - q[1]) * h / k)
                    seg2 = ("L", list(e2), e2)
                else:
                    t = next((i / 400 for i in range(1, 401) if depth(_bez(q, a2, i / 400)) >= h), None)
                    if t is None:
                        return False
                    _, second = _split_c(q, a2, t)
                    s2 = _bez(q, a2, t); seg2 = ("C", second, tuple(second[4:6]))
                sub["segs"][hit:hit + 2] = [seg1, ("L", list(s2), s2), seg2]
                return {"angle": round(math.degrees(theta), 1)}   # truthy even for a 0° cusp
            d = 0.6 if cusp else FILLET / math.tan(theta / 2)
            if c1 == "L":
                if d >= math.dist(prev, q):
                    return False
                s1 = (q[0] - din[0] / li * d, q[1] - din[1] / li * d)
                seg1 = ("L", list(s1), s1)
            else:
                t = _t_at(prev, a1, True, d)
                if t is None:
                    return False
                first, _ = _split_c(prev, a1, t)
                s1 = tuple(first[4:6]); seg1 = ("C", first, s1)
            if c2 == "L":
                if d >= math.dist(q, e2):
                    return False
                s2 = (q[0] + dout[0] / lo * d, q[1] + dout[1] / lo * d)
                seg2 = ("L", list(e2), e2)
            else:
                t = _t_at(q, a2, False, d)
                if t is None:
                    return False
                _, second = _split_c(q, a2, t)
                s2 = _bez(q, a2, t); seg2 = ("C", second, tuple(second[4:6]))
            sweep = 1 if din[0] * dout[1] - din[1] * dout[0] > 0 else 0
            if cusp:                                          # half circle across the small gap
                rr = max(math.dist(s1, s2) / 2, 0.01)
                mid = ((s1[0] + s2[0]) / 2 - q[0], (s1[1] + s2[1]) / 2 - q[1])
                # bulge away from the arms: toward p from the gap's middle
                cr = (s2[0] - s1[0]) * (-mid[1]) - (s2[1] - s1[1]) * (-mid[0])
                arc = ("A", [rr, rr, 0, 0, 0 if cr > 0 else 1, *s2], s2)
            else:
                arc = ("A", [FILLET, FILLET, 0, 0, sweep, *s2], s2)
            sub["segs"][hit:hit + 2] = [seg1, arc, seg2]
            return True
    return False


def rect_d(v):
    """A rounded rect ("x=10 y=20 width=28 height=18 rx=6 ry=6") as a path, so its corner arcs count; else None."""
    if v.startswith("M") or "width=" not in v:
        return None
    a = {k: float(x) for k, x in (kv.split("=") for kv in v.split())}
    x, y, w, h = a.get("x", 0), a.get("y", 0), a["width"], a["height"]
    r = min(a.get("rx", a.get("ry", 0)), w / 2, h / 2)
    if r <= 0:
        return None
    return (f"M{fmt(x + r)} {fmt(y)}L{fmt(x + w - r)} {fmt(y)}A{fmt(r)} {fmt(r)} 0 0 1 {fmt(x + w)} {fmt(y + r)}"
            f"L{fmt(x + w)} {fmt(y + h - r)}A{fmt(r)} {fmt(r)} 0 0 1 {fmt(x + w - r)} {fmt(y + h)}"
            f"L{fmt(x + r)} {fmt(y + h)}A{fmt(r)} {fmt(r)} 0 0 1 {fmt(x)} {fmt(y + h - r)}"
            f"L{fmt(x)} {fmt(y + r)}A{fmt(r)} {fmt(r)} 0 0 1 {fmt(x + r)} {fmt(y)}Z")


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("batch")
    ap.add_argument("icon")
    ap.add_argument("--round", nargs="*", action="extend", default=[], help="corners to keep round (apex X,Y)")
    ap.add_argument("--sharp", nargs="*", action="extend", default=[], help="kept-round corners to make sharp (apex X,Y)")
    ap.add_argument("--cut", nargs="*", action="extend", default=[],
                    help="X,Y[:R] - keep the join at X,Y sharp but cut its point flat R u past the join (default 2, "
                         "where the input's round join reached)")
    ap.add_argument("--slice", nargs="*", action="extend", default=[],
                    help="X,Y:A,B[:rot|:move] - shave the point at X,Y flat with the keyshape cut of its partner A,B "
                         "(mirrored; rot = point symmetry; move = a repeated shape, shifted)")
    cfg = ap.parse_args()
    pt_of = lambda a: tuple(map(float, a.split(",")))
    e = next(x for x in json.load(open(cfg.batch))["icons"] if x["icon"] == cfg.icon)
    arcs = input_arcs({k: v if v.startswith("M") else rect_d(v) for k, v in e["paths"]["input"].items()
                       if v.startswith("M") or rect_d(v)})
    old = {k: v for k, v in e["paths"]["sharp"].items() if v.startswith("M")}
    paths = {k: parse(v) for k, v in old.items()}
    missing = []
    for p in map(pt_of, cfg.round):
        arc = next((a for a in arcs if near(a["apex"], p, 1.0)), None)
        if arc and keep(paths, arc, p):
            continue
        if not arc and round_join(paths, p):               # a plain line join (no input arc), drawn round
            continue
        missing.append(["round", *p])
    cuts = []
    for spec in cfg.cut:
        xy, _, r = spec.partition(":")
        p = pt_of(xy)
        got = round_join(paths, p, cut=float(r) if r else CUT_REACH)
        if got:
            cuts.append({"p": list(p), **got})
        else:
            missing.append(["cut", *p])
    for p in map(pt_of, cfg.sharp):
        if not sharpen(paths, p):
            missing.append(["sharp", *p])
    new = {k: emit(v) for k, v in paths.items()}
    out = {k: {"old": old[k], "new": new[k]} for k in old if new[k] != old[k].replace(" Z", "Z")}
    if cfg.slice:
        clip0 = clip = clip_d(cfg.icon)
        for spec in cfg.slice:
            parts = spec.split(":")
            x, a = pt_of(parts[0]), pt_of(parts[1])
            got = slice_like(clip, x, a, parts[2] if len(parts) > 2 else "mirror") if clip else None
            if got:
                clip = got
            else:
                missing.append(["slice", *x])
        if clip and clip != clip0:
            out["keyshape-cut"] = {"old": clip0, "new": clip}
    print(json.dumps({"paths": out, "missing": missing, **({"cuts": cuts} if cuts else {})}))


if __name__ == "__main__":
    main()
