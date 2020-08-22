// import palettes from './palettes.js';
import palettes from './palettes-json.js'

function getRandom() {
  return palettes[Math.floor(Math.random() * palettes.length)];
}

function get(name) {
  if (name === undefined) return getRandom();
  return palettes.find(pal => pal.name == name);
}

function getAll() {
  return palettes;
}

function getNames() {
  return palettes.map(p => p.name);
}

function getAllByHarmony(harmony) {
  if (harmony === undefined) return getRandom();
  var pals = palettes.filter(pal => pal.harmony == harmony)
  return (pals.length == 0 ?  'No palettes with that harmony code' :  pals);
}

function getAllByTags(tag) {
  if (tag === undefined) return getRandom();
  var pals = palettes.filter(pal => pal.tags == tag)
  return (pals.length == 0 ?  'No palettes with that tag' :  pals);
}

function getAllBySize(size) {
  if (size === undefined) return getRandom();
  var pals = palettes.filter(pal => pal.colors.length == size);
  return (pals.length == 0 ?  'No palettes of that size' :  pals);
}

export { getRandom, get, getAll, getNames, getAllByHarmony, getAllByTags, getAllBySize };