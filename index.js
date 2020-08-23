import palettes from './palettes-json.js'

function getAll() {
  return palettes;
}

function getRandom() {
  return palettes[Math.floor(Math.random() * palettes.length)];
}

function get(name) {
  var pal = palettes.find(pal => pal.name == name);
  return (pal ? pal : 'No palette with that name')
}

function getNames() {
  return palettes.map(p => p.name);
}

function getAllByHarmony(harmony) {
  var pals = palettes.filter(pal => pal.harmony == harmony)
  return (pals.length == 0 ?  'No palettes with that harmony code' :  pals);
}

function getAllByTags(tag) {
  var pals = palettes.filter(pal => pal.tags == tag)
  return (pals.length == 0 ?  'No palettes with that tag' :  pals);
}

function getAllBySize(size) {
  var pals = palettes.filter(pal => pal.colors.length == size);
  return (pals.length == 0 ?  'No palettes of that size' :  pals);
}

function getRandomByHarmony(harmony) {
  var pals = getAllByHarmony(harmony)
  return pals[Math.floor(Math.random() * pals.length)]
}

function getRandomByTag(tag) {
  var pals = getAllByTag(tag)
  return pals[Math.floor(Math.random() * pals.length)]
}

function getRandomBySize(size) {
  var pals = getAllBySize(size)
  return pals[Math.floor(Math.random() * pals.length)]
}

export { getRandom, get, getAll, getNames, getAllByHarmony, getAllByTags, getAllBySize, getRandomByHarmony, getRandomByTag, getRandomBySize };