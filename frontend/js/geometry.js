'use strict';

/* Registry-free SVG geometry. Imported markup, transforms, presentation
 * attributes and URLs are never accepted or inserted into the document. */
const IconGeometry = (() => {
  const NS = 'http://www.w3.org/2000/svg';
  const NUMBER = /^[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?$/;
  const TOKEN = /[a-zA-Z]|[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?/gy;
  const ARITY = { M: 2, L: 2, H: 1, V: 1, C: 6, S: 4, Q: 4, T: 2, A: 7, Z: 0 };
  const ATTRS = {
    path: ['d'], line: ['x1', 'y1', 'x2', 'y2'], circle: ['cx', 'cy', 'r'],
    ellipse: ['cx', 'cy', 'rx', 'ry'], rect: ['x', 'y', 'width', 'height', 'rx', 'ry'],
    polyline: ['points'], polygon: ['points'],
  };
  const REQUIRED = { path: ['d'], line: [], circle: ['r'], ellipse: ['rx', 'ry'], rect: ['width', 'height'], polyline: ['points'], polygon: ['points'] };
  const clone = value => JSON.parse(JSON.stringify(value));
  const format = value => String(Object.is(value, -0) ? 0 : value);
  const isRecord = value => value !== null && typeof value === 'object' && !Array.isArray(value);

  function numeric(value, name) {
    if (typeof value !== 'number' && !(typeof value === 'string' && NUMBER.test(value.trim()))) throw new Error(`${name} must be a finite number.`);
    const number = Number(value);
    if (!Number.isFinite(number)) throw new Error(`${name} must be finite.`);
    return number;
  }

  function tokens(text, allowCommands) {
    if (typeof text !== 'string' || !text.trim() || text.length > 200000) throw new Error('Geometry must be nonempty text of at most 200,000 characters.');
    const result = [];
    let index = 0, comma = false;
    while (index < text.length) {
      const char = text[index];
      if (/\s/.test(char)) { index++; continue; }
      if (char === ',') {
        if (comma || !result.length || typeof result[result.length - 1] === 'string') throw new Error('Unexpected comma in geometry.');
        comma = true; index++; continue;
      }
      TOKEN.lastIndex = index;
      const match = TOKEN.exec(text);
      if (!match) throw new Error(`Invalid geometry near "${text.slice(index, index + 16)}".`);
      const token = match[0];
      if (/^[a-z]$/i.test(token)) {
        if (!allowCommands || !Object.hasOwn(ARITY, token.toUpperCase()) || comma) throw new Error(`Invalid geometry command: ${token}.`);
        result.push(token);
      } else result.push(numeric(token, 'Coordinate'));
      comma = false; index = TOKEN.lastIndex;
    }
    if (comma) throw new Error('Geometry cannot end with a comma.');
    return result;
  }

  function pathCommands(d) {
    const data = tokens(d, true), result = [];
    let i = 0, command = null;
    while (i < data.length) {
      if (typeof data[i] === 'string') command = data[i++];
      else if (command === null) throw new Error('Expected a path command.');
      const upper = command.toUpperCase(), count = ARITY[upper];
      if (!result.length && upper !== 'M') throw new Error('A path must start with M or m.');
      if (upper === 'Z') { result.push({ command, values: [] }); command = null; continue; }
      const values = data.slice(i, i + count);
      if (values.length !== count || values.some(value => typeof value !== 'number')) throw new Error(`Path command ${command} needs ${count} numbers.`);
      if (upper === 'A') {
        if (values[0] < 0 || values[1] < 0) throw new Error('Arc radii cannot be negative.');
        if (![0, 1].includes(values[3]) || ![0, 1].includes(values[4])) throw new Error('Arc flags must be 0 or 1.');
      }
      result.push({ command, values }); i += count;
      if (upper === 'M') command = command === 'm' ? 'l' : 'L';
    }
    return result;
  }

  function points(value, tag = 'polyline') {
    const values = tokens(value, false);
    if (values.length % 2 !== 0 || values.length < (tag === 'polygon' ? 6 : 4)) throw new Error(`${tag} needs ${tag === 'polygon' ? 'three' : 'two'} or more complete x,y pairs.`);
    return values;
  }

  function validateElement(element) {
    if (!isRecord(element)) throw new Error('Each element must be an object.');
    for (const key of Object.keys(element)) if (!['id', 'role', 'tag', 'attrs'].includes(key)) throw new Error(`Unsupported element field: ${key}.`);
    if (typeof element.id !== 'string' || !/^[A-Za-z][A-Za-z0-9_.:-]*$/.test(element.id)) throw new Error('Element id must be a safe identifier beginning with a letter.');
    if (element.role !== undefined && typeof element.role !== 'string') throw new Error('Element role must be text.');
    if (!Object.hasOwn(ATTRS, element.tag)) throw new Error(`Unsupported geometry tag: ${element.tag}.`);
    if (!isRecord(element.attrs)) throw new Error('Element attrs must be an object.');
    const attrs = {};
    for (const [name, value] of Object.entries(element.attrs)) {
      if (!ATTRS[element.tag].includes(name)) throw new Error(`${name} is not a geometry attribute for ${element.tag}.`);
      if (name === 'd') { pathCommands(value); attrs[name] = value; }
      else if (name === 'points') { points(value, element.tag); attrs[name] = value; }
      else attrs[name] = numeric(value, name);
    }
    for (const name of REQUIRED[element.tag]) if (!Object.hasOwn(attrs, name)) throw new Error(`${element.tag} requires ${name}.`);
    for (const name of ['r', 'rx', 'ry', 'width', 'height']) {
      if (!Object.hasOwn(attrs, name)) continue;
      const zeroAllowed = element.tag === 'rect' && ['rx', 'ry'].includes(name);
      if (zeroAllowed ? attrs[name] < 0 : attrs[name] <= 0) throw new Error(`${name} must be ${zeroAllowed ? 'nonnegative' : 'positive'}.`);
    }
    return { id: element.id, ...(element.role === undefined ? {} : { role: element.role }), tag: element.tag, attrs };
  }

  function validateElements(elements) {
    if (!Array.isArray(elements) || elements.length > 2000) throw new Error('elements must be an array of at most 2,000 items.');
    const ids = new Set();
    return elements.map(element => {
      const checked = validateElement(element);
      if (ids.has(checked.id)) throw new Error(`Duplicate element id: ${checked.id}.`);
      ids.add(checked.id); return checked;
    });
  }

  function node(element) {
    const checked = validateElement(element), result = document.createElementNS(NS, checked.tag);
    for (const [name, value] of Object.entries(checked.attrs)) result.setAttribute(name, value);
    return result;
  }

  // Bake translations into coordinates, including relative/implicit commands.
  // Radii, rotations and control-point relationships are preserved. Canonical
  // elements never contain transforms or introduce stroke scaling.
  function translatePath(d, dx, dy) {
    let x = 0, y = 0, startX = 0, startY = 0;
    return pathCommands(d).map(({ command, values }) => {
      const relative = command === command.toLowerCase(), upper = command.toUpperCase(), v = [...values];
      if (upper === 'Z') { x = startX; y = startY; return 'Z'; }
      const pairs = upper === 'A' ? [5] : ['H', 'V'].includes(upper) ? [] : Array.from({ length: v.length / 2 }, (_, index) => index * 2);
      for (const index of pairs) if (relative) { v[index] += x; v[index + 1] += y; }
      if (upper === 'H') { if (relative) v[0] += x; x = v[0]; v[0] += dx; }
      else if (upper === 'V') { if (relative) v[0] += y; y = v[0]; v[0] += dy; }
      else {
        x = v[v.length - 2]; y = v[v.length - 1];
        if (upper === 'M') { startX = x; startY = y; }
        for (const index of pairs) { v[index] += dx; v[index + 1] += dy; }
      }
      return `${upper} ${v.map(format).join(' ')}`;
    }).join(' ');
  }

  function translate(element, dx, dy) {
    const result = validateElement(element);
    dx = numeric(dx, 'Translation x'); dy = numeric(dy, 'Translation y');
    const attrs = result.attrs;
    if (result.tag === 'path') attrs.d = translatePath(attrs.d, dx, dy);
    else if (['polyline', 'polygon'].includes(result.tag)) attrs.points = points(attrs.points, result.tag).map((value, index) => format(value + (index % 2 ? dy : dx))).join(' ');
    else {
      const coordinates = result.tag === 'line' ? [['x1', dx], ['x2', dx], ['y1', dy], ['y2', dy]]
        : result.tag === 'rect' ? [['x', dx], ['y', dy]] : [['cx', dx], ['cy', dy]];
      for (const [key, delta] of coordinates) attrs[key] = (attrs[key] || 0) + delta;
    }
    return validateElement(result);
  }

  const STARTERS = Object.freeze([
    { tag: 'path', name: 'Path', attrs: { d: 'M -10 8 L -10 -4 Q -10 -8 -6 -8 L 4 -8 C 10 -8 10 0 4 0 L -2 0' } },
    { tag: 'line', name: 'Line', attrs: { x1: -8, y1: 0, x2: 8, y2: 0 } },
    { tag: 'circle', name: 'Circle', attrs: { cx: 0, cy: 0, r: 8 } },
    { tag: 'ellipse', name: 'Ellipse', attrs: { cx: 0, cy: 0, rx: 10, ry: 6 } },
    { tag: 'rect', name: 'Rectangle', attrs: { x: -10, y: -8, width: 20, height: 16, rx: 2 } },
    { tag: 'polyline', name: 'Polyline', attrs: { points: '-8 6 0 -6 8 6' } },
    { tag: 'polygon', name: 'Polygon', attrs: { points: '-8 6 0 -8 8 6' } },
  ]);
  return Object.freeze({ NS, ATTRS, STARTERS, clone, numeric, pathCommands, points, validateElement, validateElements, node, translate });
})();
if (typeof module !== 'undefined' && module.exports) module.exports = IconGeometry;
