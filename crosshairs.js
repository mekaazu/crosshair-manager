/* =============================================================
   crosshairs.js — THE ONLY FILE YOU EDIT TO ADD A CROSSHAIR
   =============================================================

   TO ADD A CROSSHAIR (2 steps):

     1. Put the image in  images/  named after its Roblox ID.
          e.g.  images/123456789.png
     2. Add one line to the CROSSHAIRS list below:
          { id: "123456789", name: "My Crosshair", color: "red" },

   That's it. Save, refresh, done. No other file needs touching.

   FIELDS
     id     (required) Roblox decal ID. Must match the image filename.
     name   (optional) Shown on the card. Defaults to the ID.
     color  (optional) Powers the colour filter buttons. One of:
              white  black  red  orange  yellow  green  cyan  blue
              purple  pink
            Leave it out and the crosshair still shows under "All".
     tags   (optional) Extra words to make it findable in the search box,
            e.g. tags: "sniper thin outline"

   Order matters: the list renders top to bottom, so put new or popular
   crosshairs near the top if you want them seen first.
   ============================================================= */

const CROSSHAIRS = [
  // ---- White ----------------------------------------------------
  { id: "7808856331",      name: "Small White (0.75x)",  color: "white" },
  { id: "973818318",       name: "Classic SMG White",    color: "white" },
  { id: "12230011198",     name: "Perfect White Dot",    color: "white" },
  { id: "5317446797",      name: "White Cross",          color: "white" },
  { id: "973821519",       name: "White Ring Reticle",   color: "white" },
  { id: "970416008",       name: "RCL",                  color: "white" },

  // ---- Green ----------------------------------------------------
  { id: "7808857452",      name: "Small Green",          color: "green" },
  { id: "5345033072",      name: "Green Dot (1.5x)",     color: "green" },
  { id: "12045455478",     name: "CommandoJesus2",       color: "green" },
  { id: "974334349",       name: "Green Dot",            color: "green" },
  { id: "7962972875",      name: "Bright Green Dot",     color: "green" },
  { id: "4882930015",      name: "Green Cross",          color: "green" },
  { id: "5355743699",      name: "Green Dot Hollow",     color: "green" },
  { id: "4813359774",      name: "Green Hollow Box [ST]", color: "green" },
  { id: "2897930456",      name: "Lime Green Dot",       color: "green" },
  { id: "973823951",       name: "Green Bracket Reticle", color: "green" },

  // ---- Cyan / Blue ----------------------------------------------
  { id: "1175800511",      name: "Cyan Dot",             color: "cyan" },
  { id: "138657308513869", name: "Small Cyan Dot",       color: "cyan" },
  { id: "974339313",       name: "ST",                   color: "cyan" },
  { id: "4845399440",      name: "Dark Blue Dot",        color: "blue" },

  // ---- Purple / Pink --------------------------------------------
  { id: "3045906966",      name: "Purple Pixel",         color: "purple" },
  { id: "6513760525",      name: "Purple Glow Dot",      color: "purple" },
  { id: "2833910141",      name: "Hot Pink Dot",         color: "pink" },
  { id: "98289740245491",  name: "Light Pink Dot",       color: "pink" },

  // ---- Yellow / Orange ------------------------------------------
  { id: "4867961490",      name: "Gold Dot",             color: "orange" },
  { id: "4813642997",      name: "Yellow Dot",           color: "yellow" },
  { id: "12230015092",     name: "Small Yellow Dot",     color: "yellow" },
  { id: "5119932947",      name: "Orange Glow Dot",      color: "orange" },
  { id: "4996338151",      name: "Orange Dot Outlined",  color: "orange" },

  // ---- Red ------------------------------------------------------
  { id: "7808856842",      name: "Small Red",            color: "red" },
  { id: "2666442734",      name: "Red Glowing Dot",      color: "red" },
  { id: "76178984348183",  name: "Red Dot",              color: "red" },
  { id: "125629214210152", name: "Red Dot (alt ID)",     color: "red" },
  { id: "973823018",       name: "Red ST Cursor",        color: "red" },
  { id: "10717562036",     name: "Red RCL",              color: "red" },

  // ---- Black ----------------------------------------------------
  { id: "71554656973830",  name: "Black Dot",            color: "black" },
  { id: "95263908240239",  name: "Black Crosshair",      color: "black" },
];

/* =============================================================
   PREVIEW BACKGROUNDS

   TO ADD A BACKGROUND (2 steps):

     1. Drop a screenshot in  backgrounds/  (jpg keeps the page fast).
     2. Add one line below:
          { file: "myshot.jpg", name: "My Game" },

   Optional but recommended: also drop a small version in
   backgrounds/thumbs/ using the SAME filename. The picker uses it so
   the page doesn't download seven full-size screenshots on load.
   Run  python3 tools/make_thumbs.py  and it does that for you.
   ============================================================= */

const BACKGROUNDS = [
  { file: "wh1.jpg",  name: "Weapon Hunt 1" },
  { file: "wh2.jpg",  name: "Weapon Hunt 2" },
  { file: "wh3.jpg",  name: "Weapon Hunt 3" },
  { file: "gt1.jpg",  name: "Gun Test 1" },
  { file: "gt2.jpg",  name: "Gun Test 2" },
  { file: "ord1.jpg", name: "Ordnance 1" },
  { file: "ord2.jpg", name: "Ordnance 2" },
];
