# tree_stat

Count files and their size in a directory tree with stats for each level.

Given a tree:

```
0_0_root/
├── 1_0_leaf
│   ├── bold-blackburn.txt
│   ├── funny-lederberg.txt
│   └── inspiring-kirch.blu
├── 1_1_node
│   ├── 2_0_leaf
│   │   ├── adoring-dhawan.mp4
│   │   ├── festive-haslett.html
│   │   ├── interesting-poincare.jpg
│   │   └── vigorous-hopper.blu
│   ├── 2_1_node
│   │   ├── 3_0_leaf
│   │   │   └── jolly-williamson.json
│   │   └── stoic-napier.jpg
│   ├── 2_2_node
│   │   ├── 3_0_node
│   │   │   ├── 4_0_leaf
│   │   │   │   ├── stupefied-kilby.json
│   │   │   │   └── thirsty-fermi.json
│   │   │   └── 4_1_leaf
│   │   ├── 3_1_node
│   │   │   └── 4_0_leaf
│   │   │       ├── nice-franklin.json
│   │   │       └── quirky-greider.blu
│   │   ├── goofy-bose.html
│   │   ├── keen-jones.blu
│   │   ├── nervous-edison.mp4
│   │   └── nifty-mendeleev.html
│   ├── naughty-wu.jpg
│   ├── pensive-minsky.mp3
│   └── sleepy-boyd.mp3
└── 1_2_node
    ├── 2_0_node
    │   └── 3_0_leaf
    │       ├── great-lewin.mp3
    │       └── romantic-northcutt.mp3
    ├── condescending-banach.jpg
    ├── modest-chandrasekhar.jpg
    ├── objective-mendel.blu
    └── zen-noyce.mp4

14 directories, 26 files
```

It produces:

| directory | type | count | size |
| --- | --- | ---: | ---: |
| 0_0_root | ALL | 26 | 29.914 MiB |
| 0_0_root | .mp3 | 4 | 3.901 MiB |
| 0_0_root | .jpg | 5 | 211.019 KiB |
| 0_0_root | .blu | 5 | 9.829 MiB |
| 0_0_root | .html | 3 | 549.206 KiB |
| 0_0_root | .mp4 | 3 | 15.357 MiB |
| 0_0_root | .json | 4 | 64.902 KiB |
| 0_0_root | .txt | 2 | 21.407 KiB |
| 0_0_root/1_2_node | ALL | 6 | 12.852 MiB |
| 0_0_root/1_2_node | .jpg | 2 | 53.018 KiB |
| 0_0_root/1_2_node | .mp4 | 1 | 7.573 MiB |
| 0_0_root/1_2_node | .blu | 1 | 2.321 MiB |
| 0_0_root/1_2_node | .mp3 | 2 | 2.907 MiB |
| 0_0_root/1_2_node/2_0_node | ALL | 2 | 2.907 MiB |
| 0_0_root/1_2_node/2_0_node | .mp3 | 2 | 2.907 MiB |
| 0_0_root/1_2_node/2_0_node/3_0_leaf | ALL | 2 | 2.907 MiB |
| 0_0_root/1_2_node/2_0_node/3_0_leaf | .mp3 | 2 | 2.907 MiB |
| 0_0_root/1_0_leaf | ALL | 3 | 1.588 MiB |
| 0_0_root/1_0_leaf | .txt | 2 | 21.407 KiB |
| 0_0_root/1_0_leaf | .blu | 1 | 1.567 MiB |
| 0_0_root/1_1_node | ALL | 17 | 15.474 MiB |
| 0_0_root/1_1_node | .mp3 | 2 | 1018.227 KiB |
| 0_0_root/1_1_node | .jpg | 3 | 158.001 KiB |
| 0_0_root/1_1_node | .blu | 3 | 5.941 MiB |
| 0_0_root/1_1_node | .html | 3 | 549.206 KiB |
| 0_0_root/1_1_node | .mp4 | 2 | 7.785 MiB |
| 0_0_root/1_1_node | .json | 4 | 64.902 KiB |
| 0_0_root/1_1_node/2_0_leaf | ALL | 4 | 3.698 MiB |
| 0_0_root/1_1_node/2_0_leaf | .jpg | 1 | 55.229 KiB |
| 0_0_root/1_1_node/2_0_leaf | .mp4 | 1 | 1.282 MiB |
| 0_0_root/1_1_node/2_0_leaf | .blu | 1 | 2.059 MiB |
| 0_0_root/1_1_node/2_0_leaf | .html | 1 | 310.553 KiB |
| 0_0_root/1_1_node/2_1_node | ALL | 2 | 60.127 KiB |
| 0_0_root/1_1_node/2_1_node | .jpg | 1 | 51.771 KiB |
| 0_0_root/1_1_node/2_1_node | .json | 1 | 8.355 KiB |
| 0_0_root/1_1_node/2_1_node/3_0_leaf | ALL | 1 | 8.355 KiB |
| 0_0_root/1_1_node/2_1_node/3_0_leaf | .json | 1 | 8.355 KiB |
| 0_0_root/1_1_node/2_2_node | ALL | 8 | 10.673 MiB |
| 0_0_root/1_1_node/2_2_node | .blu | 2 | 3.882 MiB |
| 0_0_root/1_1_node/2_2_node | .html | 2 | 238.653 KiB |
| 0_0_root/1_1_node/2_2_node | .mp4 | 1 | 6.502 MiB |
| 0_0_root/1_1_node/2_2_node | .json | 3 | 56.547 KiB |
| 0_0_root/1_1_node/2_2_node/3_0_node | ALL | 2 | 34.133 KiB |
| 0_0_root/1_1_node/2_2_node/3_0_node | .json | 2 | 34.133 KiB |
| 0_0_root/1_1_node/2_2_node/3_0_node/4_1_leaf | ALL | 0 | 0 B |
| 0_0_root/1_1_node/2_2_node/3_0_node/4_0_leaf | ALL | 2 | 34.133 KiB |
| 0_0_root/1_1_node/2_2_node/3_0_node/4_0_leaf | .json | 2 | 34.133 KiB |
| 0_0_root/1_1_node/2_2_node/3_1_node | ALL | 2 | 2.202 MiB |
| 0_0_root/1_1_node/2_2_node/3_1_node | .json | 1 | 22.414 KiB |
| 0_0_root/1_1_node/2_2_node/3_1_node | .blu | 1 | 2.180 MiB |
| 0_0_root/1_1_node/2_2_node/3_1_node/4_0_leaf | ALL | 2 | 2.202 MiB |
| 0_0_root/1_1_node/2_2_node/3_1_node/4_0_leaf | .json | 1 | 22.414 KiB |
| 0_0_root/1_1_node/2_2_node/3_1_node/4_0_leaf | .blu | 1 | 2.180 MiB |
