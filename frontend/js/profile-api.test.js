'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const API = require('./profile-api.js');
test('API uses same-origin token header and optimistic revision without URL tokens', async () => {
  const calls = [], envelope = { configuration: { schemaVersion: 2 }, revision: 'revision', resolvedProfiles: {} };
  const api = API.create('session-secret', async (url, options) => { calls.push({ url, options }); return { ok: true, json: async () => envelope }; });
  assert.deepEqual(await api.load(), envelope);
  await api.save(envelope.configuration, 'original-revision');
  assert.equal(calls[0].url, '/api/profiles'); assert.equal(calls[0].options.method, 'GET');
  assert.equal(calls[0].options.headers['X-Profile-Token'], 'session-secret');
  assert.equal(calls[1].options.method, 'PUT');
  assert.deepEqual(JSON.parse(calls[1].options.body), { configuration: envelope.configuration, revision: 'original-revision' });
});
test('API exposes conflict status for preserved-draft recovery and rejects bad envelopes', async () => {
  const conflict = API.create('', async () => ({ ok: false, status: 409, json: async () => ({ error: 'Saved configuration changed.' }) }));
  await assert.rejects(conflict.load(), error => error.status === 409 && /changed/.test(error.message));
  const malformed = API.create('', async () => ({ ok: true, json: async () => ({}) }));
  await assert.rejects(malformed.load(), /invalid profile response/);
});
