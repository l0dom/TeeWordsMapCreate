__author__ = 'Андрей'

import pickle

nameOfMap = "firstMap.map"


map = [[
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-       -               -",
       "-   -----------        -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"],
       {
           '\"':'block0.png',
           '-':'block1.png'
       },
       [(3,3),(10,3)]
        ]

if __name__ == "__main__":
    with open (nameOfMap, "wb") as data:
        pickle.dump(map,data)
        print(map)