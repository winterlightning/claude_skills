'use strict';

/* Side-effect-free profile resolution for the Profile Manager.
 * The local server remains authoritative when saving configuration. */
const ProfileConfig = (() => {
  const DEFAULT_VALIDATION = Object.freeze({ gridStep: 1, majorGridStep: 4, geometryTolerance: 0.001, keyshapeTolerance: 0.03125, minimumDistinctCenterlineDistance: 4, minimumEnclosedRadius: 1, minimumSolidFillDepth: 1 });
  const VALIDATION_LABELS = Object.freeze({ gridStep: 'Grid step', majorGridStep: 'Major grid step', geometryTolerance: 'Geometry tolerance', keyshapeTolerance: 'Keyshape tolerance', minimumDistinctCenterlineDistance: 'Distinct centerline distance', minimumEnclosedRadius: 'Enclosed radius minimum', minimumSolidFillDepth: 'Solid fill depth minimum' });
  const record = value => value !== null && typeof value === 'object' && !Array.isArray(value);
  const clone = value => JSON.parse(JSON.stringify(value));
  const safeName = value => typeof value === 'string' && /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(value) && !['constructor', 'prototype'].includes(value);
  const finite = value => typeof value === 'number' && Number.isFinite(value);

  function inspect(configuration) {
    const errors = [], resolved = Object.create(null), visiting = new Set();
    const fail = (path, message) => errors.push(`${path}: ${message}`);
    const keys = (value, allowed, path) => { for (const key of Object.keys(value)) if (!allowed.includes(key)) fail(path, `unknown field ${key}`); };
    function validation(value, path, partial = false) {
      if (!record(value)) { fail(path, 'must be an object'); return {}; }
      keys(value, Object.keys(DEFAULT_VALIDATION), path);
      if (!partial) for (const name of Object.keys(DEFAULT_VALIDATION)) if (!Object.hasOwn(value, name)) fail(path, `missing ${name}`);
      for (const [name, number] of Object.entries(value)) if (Object.hasOwn(DEFAULT_VALIDATION, name) && (!finite(number) || (name === 'minimumSolidFillDepth' ? number < 0 : number <= 0))) fail(`${path}.${name}`, `must be ${name === 'minimumSolidFillDepth' ? 'nonnegative' : 'positive'} and finite`);
      return value;
    }
    if (!record(configuration)) return { errors: ['Configuration must be an object.'], resolvedProfiles: resolved };
    keys(configuration, ['schemaVersion', 'defaultIconType', 'validationDefaults', 'profiles'], 'configuration');
    if (configuration.schemaVersion !== 2) fail('schemaVersion', 'must be 2');
    const defaults = validation(configuration.validationDefaults, 'validationDefaults');
    const profiles = configuration.profiles;
    if (!record(profiles) || !Object.keys(profiles).length) return { errors: [...errors, 'profiles: must contain at least one profile'], resolvedProfiles: resolved };
    if (!safeName(configuration.defaultIconType) || !Object.hasOwn(profiles, configuration.defaultIconType)) fail('defaultIconType', 'must identify an existing profile');
    function resolve(name) {
      if (Object.hasOwn(resolved, name)) return resolved[name];
      if (visiting.has(name)) { fail(name, 'inheritance cycle'); return null; }
      if (!Object.hasOwn(profiles, name)) { fail(name, 'unknown parent profile'); return null; }
      const raw = profiles[name], path = `profiles.${name}`;
      if (!safeName(name)) fail(path, 'profile id must be safe kebab-case');
      if (!record(raw)) { fail(path, 'must be an object'); return null; }
      keys(raw, ['label', 'canvas', 'strokeWidth', 'validation', 'keyshapes', 'extends', 'containerSlot'], path);
      if (typeof raw.label !== 'string' || !raw.label.trim()) fail(`${path}.label`, 'must be nonempty text');
      visiting.add(name);
      let base = {};
      if (raw.extends !== undefined) {
        if (!safeName(raw.extends)) fail(`${path}.extends`, 'must identify a parent profile');
        else base = resolve(raw.extends) || {};
      }
      const merged = { ...base, ...raw, iconType: name, validation: { ...defaults, ...(base.validation || {}), ...(raw.validation === undefined ? {} : validation(raw.validation, `${path}.validation`, true)) } };
      delete merged.extends;
      visiting.delete(name);
      if (!finite(merged.canvas) || merged.canvas <= 0 || !Number.isInteger(merged.canvas)) fail(`${path}.canvas`, 'must resolve to a positive integer');
      if (!finite(merged.strokeWidth) || merged.strokeWidth <= 0 || merged.strokeWidth > merged.canvas) fail(`${path}.strokeWidth`, 'must be positive and no larger than canvas');
      const v = merged.validation;
      const ratio = v.majorGridStep / v.gridStep;
      if (finite(v.gridStep) && finite(v.majorGridStep) && (!Number.isFinite(ratio) || ratio < 1 || Math.abs(ratio - Math.round(ratio)) > 1e-9)) fail(`${path}.validation.majorGridStep`, 'must be an integer multiple of gridStep');
      if (!Array.isArray(merged.keyshapes) || !merged.keyshapes.length) fail(`${path}.keyshapes`, 'must resolve to a nonempty list');
      else {
        const names = new Set();
        for (const [index, token] of merged.keyshapes.entries()) {
          const tp = `${path}.keyshapes[${index}]`;
          if (!record(token)) { fail(tp, 'must be an object'); continue; }
          keys(token, ['name', 'shape', 'orientation', 'width', 'height', 'diameter'], tp);
          if (!safeName(token.name) || names.has(token.name)) fail(`${tp}.name`, 'must be unique safe kebab-case');
          names.add(token.name);
          if (!['circle', 'rect'].includes(token.shape)) fail(`${tp}.shape`, 'must be circle or rect');
          for (const dim of ['width', 'height']) if (!finite(token[dim]) || token[dim] <= 0 || token[dim] > merged.canvas || token[dim] < merged.strokeWidth) fail(`${tp}.${dim}`, 'must be at least the stroke width and no larger than canvas');
          if (token.shape === 'circle') {
            if (token.orientation !== 'circle' || token.width !== token.height || token.diameter !== token.width) fail(tp, 'circle requires circle orientation and matching width, height, diameter');
          } else if (token.shape === 'rect') {
            if (!['square', 'portrait', 'landscape'].includes(token.orientation)) fail(`${tp}.orientation`, 'must be square, portrait, or landscape');
            if ((token.orientation === 'square' && token.width !== token.height) || (token.orientation === 'portrait' && token.width >= token.height) || (token.orientation === 'landscape' && token.width <= token.height)) fail(tp, 'rectangle orientation must match its proportions');
            if (Object.hasOwn(token, 'diameter')) fail(tp, 'rectangles cannot have a diameter');
          }
        }
      }
      merged.center = { x: merged.canvas / 2, y: merged.canvas / 2 };
      merged.designCanvas = merged.shipCanvas = merged.canvas;
      merged.designStroke = merged.shipStroke = merged.strokeWidth;
      merged.minimumDistinctCenterlineDistance = v.minimumDistinctCenterlineDistance;
      if (merged.containerSlot === null) delete merged.containerSlot;
      resolved[name] = merged;
      return merged;
    }
    for (const name of Object.keys(profiles)) resolve(name);
    for (const [name, profile] of Object.entries(resolved)) {
      const slot = profile.containerSlot, path = `profiles.${name}.containerSlot`;
      if (slot === undefined) continue;
      if (!record(slot)) { fail(path, 'must be an object or null'); continue; }
      keys(slot, ['x', 'y', 'w', 'h', 'acceptedProfile', 'minimumClearSquare'], path);
      for (const field of ['x', 'y', 'w', 'h', 'minimumClearSquare']) if (!finite(slot[field]) || (['x', 'y'].includes(field) ? slot[field] < 0 : slot[field] <= 0)) fail(`${path}.${field}`, 'must be finite with positive dimensions and nonnegative coordinates');
      const accepted = safeName(slot.acceptedProfile) ? resolved[slot.acceptedProfile] : null;
      if (!accepted) fail(`${path}.acceptedProfile`, 'must identify an existing profile');
      else {
        if (slot.acceptedProfile === name) fail(path, 'cannot accept its own profile');
        if (slot.w !== accepted.canvas || slot.h !== accepted.canvas) fail(path, 'width and height must equal the accepted profile canvas');
        if (slot.minimumClearSquare < accepted.canvas) fail(path, 'minimum clear square must contain the accepted profile canvas');
      }
      if (slot.x !== (profile.canvas - slot.w) / 2 || slot.y !== (profile.canvas - slot.h) / 2 || slot.w > profile.canvas || slot.h > profile.canvas) fail(path, 'must be centered and contained by the owning canvas');
      if (slot.minimumClearSquare > Math.min(slot.w, slot.h)) fail(path, 'minimum clear square cannot exceed the slot');
    }
    for (const name of Object.keys(resolved)) {
      let current = name; const chain = new Set();
      while (resolved[current]?.containerSlot) {
        if (chain.has(current)) { fail(`profiles.${name}.containerSlot`, 'cyclic accepted profile references'); break; }
        chain.add(current); current = resolved[current].containerSlot.acceptedProfile;
      }
    }
    return { errors: [...new Set(errors)], resolvedProfiles: resolved };
  }
  function resolve(configuration) { const result = inspect(configuration); if (result.errors.length) throw new Error(result.errors.join('\n')); return result.resolvedProfiles; }
  function gridCoordinates(canvas, step, limit = 256) {
    // Valid configurations can have extremely small grid steps. Thin only the
    // displayed grid; never iterate once per logical grid point.
    const count = canvas / step;
    if (!Number.isFinite(count)) return Array.from({ length: limit + 1 }, (_, index) => canvas * (index / limit));
    const displayStep = step * Math.max(1, Math.ceil(count / limit));
    return Array.from({ length: Math.min(limit, Math.floor(canvas / displayStep)) + 1 }, (_, index) => index * displayStep);
  }
  function duplicate(configuration, source, name) {
    if (!safeName(name) || Object.hasOwn(configuration.profiles, name)) throw new Error('Choose an unused kebab-case profile id.');
    const next = clone(configuration); next.profiles[name] = { ...clone(configuration.profiles[source]), label: `${configuration.profiles[source].label} copy` }; return next;
  }
  function remove(configuration, name) {
    if (configuration.defaultIconType === name) throw new Error('Choose another default profile before deleting this one.');
    if (Object.keys(configuration.profiles).length <= 1) throw new Error('At least one profile must remain.');
    const resolved = resolve(configuration);
    const dependents = Object.keys(configuration.profiles).filter(other => other !== name && (configuration.profiles[other].extends === name || resolved[other].containerSlot?.acceptedProfile === name));
    if (dependents.length) throw new Error(`Update dependent profiles first: ${dependents.join(', ')}.`);
    const next = clone(configuration); delete next.profiles[name]; return next;
  }
  return Object.freeze({ DEFAULT_VALIDATION, VALIDATION_LABELS, clone, safeName, inspect, resolve, gridCoordinates, duplicate, remove });
})();
if (typeof module !== 'undefined' && module.exports) module.exports = ProfileConfig;
