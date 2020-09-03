import json
import colorsys

pals = """[
  {
    "name": "lawn",
    "harmony": "sc",
    "tags": "nature",
    "background": "#ffffff",
    "stroke": "#000000",
    "colors": ["#183617", "#4b6720",  "#c4cd47", "#2e717a", "#d7a0a4"]
  },
  {
    "name": "prismatica",
    "harmony": "co",
    "tags": "nature",
    "background": "#000000038",
    "stroke": "#000000",
    "colors": ["#e37430", "#e3c39f", "#8ed2e6", "#7ef5db"]
  },
  {
    "name": "timp",
    "harmony": "co",
    "tags": "nature",
    "background": "#BBCFC9",
    "stroke": "#000000",
    "colors": ["#3c80bd", "#D6C19B",  "#6B8B70"]
  },
  {
    "name": "cabin",
    "harmony": "co",
    "tags": "nature",
    "background": "#2f2f2d",
    "stroke": "#D9D9D0",
    "colors": ["#5f4a49", "#a88671", "#879f85", "#336558"]
  },
  {
    "name": "frijole",
    "harmony": "an",
    "tags": "food",
    "background": "#c3a66c",
    "stroke": "#000000",
    "colors": ["#de3802", "#c97f1a", "#f5bf3c", "#ac703d"]
  },
  {
    "name": "afghan",
    "harmony": "mo",
    "tags": "object",
    "background": "#efe5cc",
    "stroke": "#000000",
    "colors": ["#d1bf25", "#666446", "#857d3f"]
  },
  {
    "name": "bearpot",
    "harmony": "an",
    "tags": "object",
    "background": "#2d2e30",
    "stroke": "#000000",
    "colors": ["#d39388", "#d1c8cb", "#93746d", "#806f55", "#595350"]
  },
  {
    "name": "flathead",
    "harmony": "sc",
    "tags": "nature",
    "background": "#ffffff",
    "stroke": "#000000",
    "colors": ["#3b7566", "#2d4242", "#263923", "#a3a194", "#df7c72"]
  },
  {
    "name": "hotchicken",
    "harmony": "sc",
    "tags": "food",
    "background": "#000000",
    "stroke": "#000000",
    "colors": ["#3387da", "#FCFBEB", "#c24d0e", "#ffdc84"]
  },
  {
    "name": "baja",
    "harmony": "mo",
    "tags": "food",
    "background": "#000000",
    "stroke": "#000000",
    "colors": ["#B7D7CA", "#95DCCF", "#67EDBE", "#A15AB3"]
  },
  {
    "name": "shelf",
    "harmony": "co",
    "tags": "object",
    "background": "#f6f4f5",
    "stroke": "#000000",
    "colors": ["#1c6029", "#663f35", "#ebdbc4", "#7f8893"]
  },
  {
    "name": "shakespeare",
    "harmony": "tr",
    "tags": "artwork",
    "background": "#0b061c",
    "stroke": "#0b061c",
    "colors": ["#D6E9F2", "#E4E0B8", "#be8b88"]
  },
  {
    "name": "fence",
    "harmony": "co",
    "tags": "object",
    "background": "#ffffff",
    "stroke": "#000000",
    "colors": ["#2791BB", "#248170", "#E1B473", "#b7a477"]
  },
  {
    "name": "birthday",
    "harmony": "sq",
    "tags": "object",
    "background": "#726c49",
    "stroke": "#000000",
    "colors": ["#e65131", "#306a74", "#90b33d", "#dcaf35"]
  },
  {
    "name": "slam01",
    "harmony": "ds",
    "tags": "artwork",
    "background": "#ffffff",
    "stroke": "#000000",
    "colors": ["#0c4a93", "#e3cb3e", "#dd7e45", "#7cbc74", "#F6B4A9"]
  },
  {
    "name": "chirico",
    "harmony": "sc",
    "tags": "artwork",
    "background": "#D5C29C",
    "stroke": "#000000",
    "colors": ["#234459", "#d29c1d", "#73663d", "#814110", "#372f1b"]
  },
  {
    "name": "richter",
    "harmony": "an",
    "tags": "artwork",
    "background": "#230000",
    "stroke": "#000000",
    "colors": ["#61583f", "#D6A451", "#8C2A14", "#BF705E"]
  },
  {
    "name": "moa01",
    "harmony": "an",
    "tags": "artwork",
    "background": "#ffffff",
    "stroke": "#000000",
    "colors": ["#c9993f", "#787b35", "#C24D04", "#666b5d"]
  },
  {
    "name": "bluff",
    "harmony": "tr",
    "tags": "nature",
    "background": "#EEEAD0",
    "stroke": "#9d8361",
    "colors": ["#a35739", "#4E5C1B", "#66a2b4"]
  },
  {
    "name": "crane",
    "harmony": "co",
    "tags": "object",
    "background": "#EBB591",
    "stroke": "#000000",
    "colors": ["#ac5a1f", "#f4ede8", "#5a7478", "#BABECC"]
  },
  {
    "name": "tidepool01",
    "harmony": "sc",
    "tags": "nature",
    "background": "#DDEEFF",
    "stroke": "#000000",
    "colors": ["#a44e2b", "#8594a5", "#3a6929", "#d5c0a7"]
  },
  {
    "name": "tidepool02",
    "harmony": "mo",
    "tags": "nature",
    "background": "#3b6a7a",
    "stroke": "#ffffff",
    "colors": ["#316c22", "#78995c", "#99b48b"]
  },
  {
    "name": "castle",
    "harmony": "co",
    "tags": "object",
    "background": "#E6DADA",
    "stroke": "#000000",
    "colors": ["#0f554a", "#72ceeb", "#c9615e", "#c62f2a"]
  },
  {
    "name": "droid",
    "harmony": "an",
    "tags": "object",
    "background": "#ffffff",
    "stroke": "#000000",
    "colors": ["#24AD70", "#B5A465", "#dfe0e4", "#c0dad7", "#abd3e4"]
  },
  {
    "name": "carl",
    "harmony": "ds",
    "tags": "object",
    "background": "#ffffff",
    "stroke": "#000000",
    "colors": ["#58abdb", "#b5b2ac", "#a99597", "#7C848A", "#1e2229"]
  },
  {
    "name": "dorados",
    "harmony": "an",
    "tags": "food",
    "background": "#DDDDBB",
    "stroke": "#000000",
    "colors": ["#9EAD2C", "#e9c32c", "#c18119", "#c0520e"]
  },
  {
    "name": "monte01",
    "harmony": "sc",
    "tags": "artwork",
    "background": "#083c64",
    "stroke": "#000000",
    "colors": ["#0298B3", "#EDD6B1", "#e69382", "#a92d19", "#BD7F23"]
  },
  {
    "name": "ferry",
    "harmony": "an",
    "tags": "object",
    "background": "#CCEDDD",
    "stroke": "#C9BEBA",
    "colors": ["#767d69", "#34A357", "#187674", "#83b0ca"]
  },
  {
    "name": "poppy01",
    "harmony": "mo",
    "tags": "nature",
    "background": "#ffffff",
    "stroke": "#000000",
    "colors": ["#9a6031", "#e0b365", "#eee4c9"]
  },
  {
    "name": "skylight",
    "harmony": "ds",
    "tags": "object",
    "background": "#ffffffECE",
    "stroke": "#000000",
    "colors": ["#fc0000", "#00ead9", "#00d62e", "#0054ff", "#ffa900"]
  },
  {
    "name": "lowell",
    "harmony": "tr",
    "tags": "object",
    "background": "#000000",
    "stroke": "#f1f3ff",
    "colors": ["#E6C440", "#E85168", "#3E76E6", "#84D9E9"]
  },
  {
    "name": "af",
    "harmony": "mo",
    "tags": "object",
    "background": "#DDE1DF",
    "stroke": "#000000",
    "colors": ["#f7d59c", "#d89556", "#6b5136", "#312214"]
  },
  {
    "name": "jack",
    "harmony": "co",
    "tags": "object",
    "background": "#ffffff",
    "stroke": "#D4D4D4",
    "colors": ["#bd7628", "#0e1d23", "#0260a6"]
  },
  {
    "name": "kernel",
    "harmony": "mo",
    "tags": "nature",
    "background": "#ffffff",
    "stroke": "#000000",
    "colors": ["#e2d1b9", "#c3a163", "#a3720a"]
  },
  {
    "name": "primary01",
    "harmony": "tr",
    "tags": "design",
    "background": "#000000",
    "stroke": "#000000",
    "colors": ["#30a6e6", "#fffffff75", "#ff7169"]
  },
  {
    "name": "albers01",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#b7c4cc",
    "stroke": "#000000",
    "colors": ["#437db8","#387877","#293769"]
  },
  {
    "name": "albers02",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#bac0cc",
    "stroke": "#000000",
    "colors": ["#97692e","#a12f2a","#874368","#c7637b"]
  },
  {
    "name": "albers03",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#c5ab8c",
    "stroke": "#000000",
    "colors": ["#953a41","#4262ab","#785a98","#346864"]
  },
  {
    "name": "albers04",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#cecabf",
    "stroke": "#000000",
    "colors": ["#8d5c19","#797a7d","#415a44", "#74afdd","#ba977b"]
  },
  {
    "name": "albers05",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#d9613f",
    "stroke": "#000000",
    "colors": ["#97423f","#d1725a","#694d41","#1f487a"]
  },
  {
    "name": "albers06",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#326e5b",
    "stroke": "#000000",
    "colors": ["#53585f","#becad3","#14191d"]
  },
  {
    "name": "albers07",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#8d9699",
    "stroke": "#000000",
    "colors": ["#a9bbc5","#0f181c","#80471c"]
  },
  {
    "name": "albers08",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#4c99cd",
    "stroke": "#000000",
    "colors": ["#7a8594","#afc0d2","#9c9100"]
  },
  {
    "name": "matisse01",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#f2e8ce",
    "stroke": "#f2e8ce",
    "colors": ["#0d2e75"]
  },
  {
    "name": "peachbowl",
    "harmony": "tbd",
    "tags": "food",
    "background": "#d0ab8a",
    "stroke": "#3a3027",
    "colors": ["#cd4024","#e88f61","#7c7a24"]
  },
  {
    "name": "blanket",
    "harmony": "tbd",
    "tags": "object",
    "background": "#f9efe3",
    "stroke": "#ca421b",
    "colors": ["#393657","#6e4b4b","#9a99a3"]
  },
  {
    "name": "donut",
    "harmony": "tbd",
    "tags": "food",
    "background": "#dbd1d9",
    "stroke": "#ffffff",
    "colors": ["#b9305e","#bf5f32"]
  },
  {
    "name": "stainedglass",
    "harmony": "tbd",
    "tags": "object",
    "background": "#6a6663",
    "stroke": "#2a0505",
    "colors": ["#f6530e","#f68a26","#fdfd29","#2a0505"]
  },
  {
    "name": "pivoines",
    "harmony": "tbd",
    "tags": "nature",
    "background": "#faf0e8",
    "stroke": "#4a8540",
    "colors": ["#ffa376","#c91116","#fee658"]
  },
  {
    "name": "vangogh01",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#addfd4",
    "stroke": "#feffd7",
    "colors": ["#7ca995","#cfc971","#c18431"]
  },
  {
    "name": "cezanne01",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#ba7144",
    "stroke": "#ba7144",
    "colors": ["#212e3b","#8d7956","#c6cccc", "#945668"]
  },
  {
    "name": "vangogh02",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#ffffff",
    "stroke": "#000000",
    "colors": ["#37577c","#2f3826","#9b8850","#895343","#99978b"]
  },
  {
    "name": "vangogh03",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#fcf2b3",
    "stroke": "#0e1e15",
    "colors": ["#93a2c9","#cca32f","#9b2c19","#7b7415"]
  },
  {
    "name": "monet01",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#ffffff",
    "stroke": "#000000",
    "colors": ["#fbe6c9","#b99181","#909daf","#737841"]
  },
  {
    "name": "macaron",
    "harmony": "tbd",
    "tags": "food",
    "background": "#bde0da",
    "stroke": "#443035",
    "colors": ["#b8485f","#c9a43b","#bb9c70","#4e3423"]
  },
  {
    "name": "palais",
    "harmony": "tbd",
    "tags": "object",
    "background": "#6f7787",
    "stroke": "#dfd3c7",
    "colors": ["#986855","#dcb26d","#5a6171"]
  },
  {
    "name": "cellar",
    "harmony": "tbd",
    "tags": "object",
    "background": "#b7afa1",
    "stroke": "#2b2118",
    "colors": ["#7d313f","#e28346","#bb9b79","#5b7f57","#7c533c"]
  },
  {
    "name": "tricolore",
    "harmony": "tbd",
    "tags": "object",
    "background": "#c0c1bc",
    "stroke": "#8b7e6f",
    "colors": ["#4b69c9","#f0eabc","#8c1934"]
  },
  {
    "name": "vitrail",
    "harmony": "tbd",
    "tags": "object",
    "background": "#0e0d0a",
    "stroke": "#0e0d0a",
    "colors": ["#0100cb","#f6c731"]
  },
  {
    "name": "mosaic",
    "harmony": "tbd",
    "tags": "object",
    "background": "#000000",
    "stroke": "#ffffff",
    "colors": ["#44302f","#f3aa2d","#d1a567","#adaeb0"]
  },
  {
    "name": "overwings",
    "harmony": "tbd",
    "tags": "object",
    "background": "#dbd3c6",
    "stroke": "#20201e",
    "colors": ["#e6d853","#c6343e","#20201e"]
  },
  {
    "name": "tiles",
    "harmony": "tbd",
    "tags": "object",
    "background": "#edd5bb",
    "stroke": "#5a4b3f",
    "colors": ["#c56559","#c3f8fa","#676d80","#ffffff0aa","#faac93"]
  },
  {
    "name": "capistrano01",
    "harmony": "tbd",
    "tags": "object",
    "background": "#fbf0e7",
    "stroke": "#fbf0e7",
    "colors": ["#5f91e1","#fe7755","#808b66"]
  },
  {
    "name": "capistrano02",
    "harmony": "tbd",
    "tags": "object",
    "background": "#6f96d9",
    "stroke": "#201f2e",
    "colors": ["#ac6b5f","#f8faf0","#908d87","#5f6e3d"]
  },
  {
    "name": "cowboy",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#987d70",
    "stroke": "#615b55",
    "colors": ["#7f5d58","#dbad7c","#c3665c"]
  },
  {
    "name": "flannel",
    "harmony": "tbd",
    "tags": "object",
    "background": "#e8e1de",
    "stroke": "#806a62",
    "colors": ["#c83a36","#392a2a","#b9b0b0"]
  },
  {
    "name": "sweater",
    "harmony": "tbd",
    "tags": "object",
    "background": "#b69e77",
    "stroke": "#5b4d44",
    "colors": ["#b57862","#5b4d44","#dbc2a0"]
  },
  {
    "name": "hill",
    "harmony": "tbd",
    "tags": "nature",
    "background": "#eaeaec",
    "stroke": "#463d3b",
    "colors": ["#637953","#676475","#663339","#a46645"]
  },
  {
    "name": "belle",
    "harmony": "tbd",
    "tags": "object",
    "background": "#0f0e18",
    "stroke": "#9d9892",
    "colors": ["#464236","#42171b","#9d9892"]
  },
  {
    "name": "thrift",
    "harmony": "tbd",
    "tags": "object",
    "background": "#827a65",
    "stroke": "#000000",
    "colors": ["#2b2c30","#4d5153","#e7d4c5","#e1d8cd"]
  },
  {
    "name": "fruitplate",
    "harmony": "tbd",
    "tags": "food",
    "background": "#ede6e1",
    "stroke": "#4e433e",
    "colors": ["#848955","#aa4e41","#3a525a","#ca9b4d"]
  },
  {
    "name": "stovetop",
    "harmony": "tbd",
    "tags": "food",
    "background": "#60574d",
    "stroke": "#fcf6ea",
    "colors": ["#cd473b","#dc875a","#efc47b"]
  },
  {
    "name": "citycenter",
    "harmony": "tbd",
    "tags": "object",
    "background": "#266f9b",
    "stroke": "#291812",
    "colors": ["#c8692c","#544945","#f3e2b0","#e0b782"]
  },
  {
    "name": "sneaker",
    "harmony": "tbd",
    "tags": "object",
    "background": "#262822",
    "stroke": "#e9ede8",
    "colors": ["#406b56","#523326"]
  },
  {
    "name": "nebo",
    "harmony": "tbd",
    "tags": "nature",
    "background": "#f3f1f6",
    "stroke": "#3f494c",
    "colors": ["#a1b1d3","#aa4e45","#f2e4ad","#44699d","#c9936d"]
  },
  {
    "name": "smore",
    "harmony": "tbd",
    "tags": "nature",
    "background": "#080f10",
    "stroke": "#f9fafc",
    "colors": ["#0a56b4","#0e1d1d","#786756"]
  },
  {
    "name": "mesa",
    "harmony": "tbd",
    "tags": "object",
    "background": "#e7c8b4",
    "stroke": "#545448",
    "colors": ["#d8a688","#8f7a6b","#b4c7d8"]
  },
  {
    "name": "swami",
    "harmony": "tbd",
    "tags": "object",
    "background": "#f3d2a1",
    "stroke": "#7e6057",
    "colors": ["#435467","#516426","#fdfcf8"]
  },
  {
    "name": "bucerias",
    "harmony": "tbd",
    "tags": "object",
    "background": "#ffffffffd",
    "stroke": "#2b1b23",
    "colors": ["#fe0969","#920dac","#b82912"]
  },
  {
    "name": "provost",
    "harmony": "tbd",
    "tags": "object",
    "background": "#3e3b34",
    "stroke": "#7f6c4b",
    "colors": ["#eed899","#b4bdb8","#536531"]
  },
  {
    "name": "jump",
    "harmony": "tbd",
    "tags": "object",
    "background": "#040406",
    "stroke": "#b0b0b0",
    "colors": ["#5a665c","#283848","#3860a5"]
  },
  {
    "name": "joe",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#dfd6cd",
    "stroke": "#222222",
    "colors": ["#293468","#9b2224","#9e9a91"]
  },
  {
    "name": "picasso01",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#4a3c2f",
    "stroke": "#1a1a16",
    "colors": ["#d45638","#d8932d","#dfc386","#3f3e44"]
  },
  {
    "name": "pear",
    "harmony": "tbd",
    "tags": "food",
    "background": "#b4c295",
    "stroke": "#403c3b",
    "colors": ["#b25132","#df9c43","#dbbd7b"]
  },
  {
    "name": "dodger",
    "harmony": "tbd",
    "tags": "object",
    "background": "#7999c6",
    "stroke": "#dfdcf5",
    "colors": ["#26333e","#bfa66f","#637335"]
  },
  {
    "name": "patch",
    "harmony": "tbd",
    "tags": "object",
    "background": "#ded1c8",
    "stroke": "#a1b5b4",
    "colors": ["#c6253e"]
  },
  {
    "name": "camper",
    "harmony": "tbd",
    "tags": "object",
    "background": "#1b182e",
    "stroke": "#ced5e7",
    "colors": ["#3957b1","#51305c","#242663","#ac253d"]
  },
  {
    "name": "bo",
    "harmony": "tbd",
    "tags": "artwork",
    "background": "#161417",
    "stroke": "#ffffff",
    "colors": ["#393870","#bb8520","#c22f3b","#d1e38d"]
  },
  {
    "name": "chiquita",
    "harmony": "tbd",
    "tags": "object",
    "background": "#cbaf84",
    "stroke": "#21180d",
    "colors": ["#485949","#9cba9e","#731f13","#d58c4c"]
  },
  {
    "name": "beloeil",
    "harmony": "tbd",
    "tags": "nature",
    "background": "#fefefe",
    "stroke": "#15100a",
    "colors": ["#d84023","#c7940a","#556c38"]
  }
]"""

def main():
    pals_json = json.loads(pals)
    new_pals = []

    for p in pals_json:
        background = convert_color(p['background'])
        stroke = convert_color(p['stroke'])
        hsv_background = colorsys.rgb_to_hsv(background[0],background[1],background[2])
        hsv_stroke = colorsys.rgb_to_hsv(stroke[0],stroke[1],stroke[2])
        colors = []
        hsv_colors = []
        for c in p['colors']:
            color = convert_color(c)
            colors.append(color)
            hsv_color = colorsys.rgb_to_hsv(color[0],color[1],color[2])
            hsv_colors.append(hsv_color)
        pal_obj = {"name": p['name'], "harmony": p['harmony'], "tags": p['tags'], "rgb": {"background": background, "stroke": stroke, "colors": colors}, "hex": {"background": p['background'], "stroke": p['stroke'], "colors": p['colors']},"hsv": {"background": hsv_background, "stroke": hsv_stroke, "colors": hsv_colors}}
        new_pals.append(pal_obj)


    with open('convert.js', 'w') as jsonfile:
        json.dump(new_pals, jsonfile)


def convert_color(hexcode):
    print(hexcode)
    h = hexcode.lstrip('#')
    r = tuple(int(h[i:i+2],16) for i in (0,2,4))
    print(r)
    print('---------')
    return r

main()