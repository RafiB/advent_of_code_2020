import attr

# TEST_INPUT = """0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"

# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb"""

TEST_INPUT = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31 | 42 11 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42 | 42 8
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""


PUZZLE_INPUT = """18: 48 48
25: 48 81 | 41 7
48: "b"
4: 131 48 | 70 41
20: 61 48 | 57 41
89: 41 41 | 41 48
74: 41 107 | 48 124
98: 41 48
99: 97 48 | 92 41
91: 34 48
100: 48 41 | 67 48
6: 48 100 | 41 132
40: 81 48 | 7 41
124: 83 48 | 130 41
50: 7 41 | 7 48
68: 64 41 | 24 48
60: 30 41 | 86 48
75: 89 41 | 39 48
103: 67 67
58: 41 22 | 48 111
71: 67 34
56: 34 48 | 39 41
122: 48 120 | 41 89
12: 41 18 | 48 98
95: 34 41 | 103 48
93: 110 41 | 34 48
13: 43 41 | 69 48
44: 101 48 | 114 41
69: 106 41 | 32 48
67: 48 | 41
45: 7 48
117: 48 120 | 41 39
46: 48 29 | 41 82
121: 48 49 | 41 47
130: 103 48 | 89 41
132: 41 48 | 48 41
94: 41 4 | 48 76
14: 9 48 | 93 41
26: 41 72 | 48 81
79: 67 1
115: 67 132
15: 41 20 | 48 63
47: 120 41 | 81 48
27: 100 41 | 7 48
11: 42 31 | 42 11 31
113: 49 41 | 56 48
31: 48 133 | 41 127
131: 90 41 | 28 48
81: 48 48 | 67 41
23: 84 41 | 27 48
84: 18 48
107: 79 41 | 33 48
83: 67 89
49: 81 41 | 7 48
108: 102 41 | 60 48
37: 41 7 | 48 120
120: 48 41
32: 41 96 | 48 95
2: 48 85 | 41 128
102: 48 62 | 41 50
5: 41 110
61: 41 37 | 48 6
97: 41 120 | 48 34
85: 120 41 | 89 48
80: 120 48 | 98 41
92: 48 103 | 41 34
65: 16 48 | 58 41
112: 48 71 | 41 123
70: 87 48 | 115 41
39: 41 67 | 48 41
41: "a"
38: 2 48 | 77 41
110: 48 41 | 41 41
88: 7 48 | 89 41
52: 41 73 | 48 104
96: 100 48 | 103 41
66: 41 126 | 48 121
77: 40 48 | 47 41
3: 48 118 | 41 25
126: 75 48 | 27 41
1: 41 41 | 48 48
19: 48 72 | 41 18
42: 41 68 | 48 105
129: 48 110 | 41 120
72: 48 48 | 41 67
7: 41 41
59: 41 47 | 48 125
73: 1 48 | 103 41
114: 41 117 | 48 73
118: 89 41 | 132 48
51: 41 1 | 48 81
101: 129 48 | 93 41
133: 48 15 | 41 13
104: 48 1 | 41 81
123: 110 48 | 98 41
0: 8 11
55: 48 1 | 41 18
30: 89 41 | 18 48
76: 48 14 | 41 35
43: 52 48 | 112 41
24: 48 109 | 41 38
29: 116 48 | 3 41
106: 88 41
9: 89 41 | 100 48
125: 41 120 | 48 132
22: 103 48 | 18 41
21: 48 83 | 41 51
64: 48 44 | 41 74
111: 103 67
54: 41 36 | 48 55
119: 48 12 | 41 19
35: 123 48 | 91 41
127: 41 94 | 48 10
116: 41 93 | 48 122
8: 42 | 42 8
128: 48 72 | 41 1
28: 41 132 | 48 120
63: 41 59 | 48 17
87: 103 48 | 72 41
36: 48 81 | 41 100
17: 62 48 | 26 41
62: 100 48 | 98 41
34: 48 41 | 48 48
82: 23 48 | 21 41
78: 41 65 | 48 66
33: 120 41
109: 48 113 | 41 99
57: 41 92 | 48 80
86: 48 89 | 41 39
53: 54 48 | 119 41
10: 108 48 | 53 41
90: 81 41 | 34 48
16: 48 5 | 41 45
105: 46 41 | 78 48

bbaaabbbbaabbaababaababbbabbbaaa
bbbbbaabbabaaaaabbaaaabbabaababbbbabbbbababaabaabaaaaaabbbaaaaab
baabbaabababbabbaaaaabba
ababbbbbbbabaaaaabaabbabbbbaaaabbabbaaba
abbbbabaabbbabbbabbaaaaaaaaaabba
bbaaaaaabaabbbababbaabbabbabaaaabbbaababaaaabbbaabababaa
bbbbbaabbabbbbabaabbbbaaaaaaabba
bbbaabbaaababbbbabbbaabb
abbbbaaabbbaabababaababa
aaaababbabaaabaaabbbbbaaaabaaabaaababbbbbaabaabababbbbbbbaabaaaa
babaababaabbbbabbabbbbabbababbaa
babbaaabababbaaabbbaabab
aaaabaabbbababbbbbbbbbbb
aabbbbbabbbbabbbbbbbbababbbabababaaaababbbaaaabaaaabaaaaabbaabbaaababaaaabaaabab
aaabbaabaaaabbbababbbbbbbabaaabaababaabb
abbaaaaabbaabaabbbabbbab
baabbbaabbabbabaabbabbbb
abababbbaaaaabbbbbbbbabaabaababbabbbbbbbbbabbabbaaabaaba
abbaaaaaaabbabbaaaababab
baabababbaaaaaaabbbbabab
babbabaaaaabaabbbbbaaaab
aabaaaababbaaabbbbbbaaaa
babaaaaabaaaababbbabbabb
abbabaaaabbababbaaabbaba
aaabaaaaaabaaaababaaaabaaaaabaabaababbabaabababa
ababbabbaaabaabababaabbaaabbabababaabbaa
baaaabbbbbabaaaabbbabaabbabbbaaa
abaabaaaababababbaabaabb
aabaabbbbabaaabbaababbaabbbbbbabbbbaabababbabbaa
abaaaaaabbaaaabaaabbaaab
aaaabbbbbabaabaaababaaabbbbbaaabbbbbabbbaaaabaaabababaaa
bbabbbbaaababbbbaaababbbbbbaabbaababbabbaaaabbbaaaaabbbaaabbabbbaaababab
babaaaaaaabaaabaabbbabab
aaaabbaaabaaabaabaabbbabaaaabbbbabbaaabbbbabbbbbbbaabbabbbbbababababaabb
abbbabbabbabbbbaaabaaaaababbaabbaabaaabb
abbaaabbbbaaababbbbaaabbabbbbbbbbbbbbaababbbbbbbabbbbabbabbabbbb
babbbaababbaabaaaabbbbbb
baaaabbbbbbbaabbbabbbababaaaabba
aaabbbaababbaaaabaaaabbbbaaabaaa
abbbbaaaaababbabbbabaaabbbaaabba
babbabaabaaaabbbbbbaaaab
abbababaabbbbaababaaabba
aababbbbbababaababbaababababbbbbbaaabbbbaaabaaab
baabbaabaaabaabaababbaaaabaaaabaaaababbbbbbabbbbbbbbabab
bbababbaaaabaaaaabbabbaa
bbababbbbababbabbbaababbbabaabbaabbaaabaabababaa
baababbabababbabaababbab
abbababbbaababababaaabaaababbbabbbbaaaab
abbbbbaaaabaaaaaabababbb
abbbbaaabaaabbbaababbbaa
bbababbbbabaabaabbbbabaaaaaaaabb
aaaabbaaaabbbbaaaaababba
abaaabaaaababbabbaabaaba
babbabababbaabaaabaaabbb
babababbbaaaabbbbabaababbbbaaaaaaabbaababbaababbaaabaaababaaaaabbbabbbab
baaabbabbaababbaaabbbaaa
bbbababbbabababbaaaabaabababaabaaabbabbb
bababbabbabbbbabaababbbbabaabbabaababaabbbaaaabaaaabbaabaaabbaaa
bbabbbaabaaaabbbbbabaaabababaababaaababa
aabbbbaabaaaaaaaaabbbaabbbbabaababbaaabbbabbabbbaaabababbaabbaba
bbbbaabbbabbabaaabbbbbaaabaaabab
baabbabababaabbbabbabbbaabaabaabaabbbbaabbabbabbabbbaaaabaaaaabaabbbaaba
ababbabbbbbaaabbbbbbaaaa
aaaaaabbababbbabbaababbb
ababbabbaaabaababaababaabaababaaababbababaaaabaa
baaaababaabaaaaabaabaaba
bbabbbbaabbbaabbbabbaaabbababaababbbbbabbbabbbbb
bbbababbbaabbbaaabbbbabb
bbbababbbbbbbaababbbaabbbababbbabbabbabb
abaaaaaaaaababbbaaaabaaa
baaaababbbababbaaaabaaab
babaaabbbbbabbaaaaababbbabbbabaaabbabbaa
bbaaaabbbaaabaaaabababbbbaabaaabbbbbbbbabaaaaabbababaaaaaaaabbabbbaaabaababbbaab
aabaaaabbbabbbaaaaaaabaa
ababaaabaabbbbabbbbbaabbaabbabbababbbbbbaabbbbbb
bababaabbbbabaabbababbba
bbbbbbabababbabbbbaaaaaabaabaaaaaababaaabbbbbbaabbbabbbaaaaaabaa
abbbbaaaababaaabaaabaabaabbbbbbbbabbbaaa
abaabaabbabbaabbbabaabaabbbabbbbabbbaaabaabbabaaabbabbaabbaaabba
abbbbbaaababbaaaabbaabaabbabbaaabbababbbaaaaabaaababaabb
abbaaababbbabbbbabbbbababaabababbbbbbbabababbababbbbabbb
aababaaaaabaaaababbbaaabbbabbaabababbabababbabbb
bbbababaaabababbabaabaaabbabbbab
bbabababbbaabbababbababaabbaaaaaaaabbaba
aaabaabbbbaaabbbabababbb
abababababbbaaaaabbababbaabaaaaabbaaababaabbbababbabbbabaaaaabaa
bbbbabaaabaabaabbbaaaabaaaababbbbbaababababababa
aaaabbaaabaababbbaaabbbb
baaabbabbabbababaaaabbabaabaaaabbbbaabbbabaaaabb
aabaaaaaaaababbbabbbaabaabbbbaabbbbbbbabaababababaababaa
babaabaaaaaaabababbaaabbbbbaabaabbababab
aababbbbbbbabaaaaaabaabbbbbabbaabbabbababbbbaaba
bbbabbaababbbaabaabbaaaa
abbbaabbbbbabaaaaaababab
babbababbbbabbbbaabaaabaabbaabbaabbabaab
abbaaaabbbabbbaaabbbbbab
aabbabbbbabababbaaabbbbaaababaabbabbbbbbbbaabbbaabbbabaababbbaabbbaabbaabbbaabbb
bbabaabaabaabaaaabbababaaabaabaa
bbbbbaabaaaaaabbaabbbaababaabaaabbabaaabbbabbaaaabaaaabb
aababbababaaaaaaabbbbbbbbaabaaab
aaabbbaabbbaabbababaabbabbbbabaabbaabbaaaabababbabbbbbba
bbbbbababbabbaaabbbabaabaabbbbbb
aababaabaaaaaaabaabbaabaaaabbaaaaababbbbabbbabbbbaaabbab
baabbaaabbaaaabbaaabbbbbabaabbabbbbabbba
bababaabbabbbbbabaabbbbabbbaaaab
ababbaaabbbaabbababbbbab
babaaaababbbbbbbaaaaaababaabbbba
aaaabbabbaaabbaabaabbaba
bbbbaabbbbbbbbababababbabababbaa
baaabbaaabbaaaaababababa
aaabaaaabbbbbaababbbbababbabbbaaaabbabbaababaabbbaaabaabababaababbabaabb
babaabbababaaabbbababbbb
baabababbbaaaabbbbabbaaaabbabbaabbabbbbb
babbbbababaaaabaabbbbbaaababbaabaabbbbbabbaabaaaaabababb
babbbaaabaabaaabaabaaabb
aaabbbbbbbaaabbbbaaaaaba
baaaaaabaabbbbbbabaababa
ababaaabbbbaaabbababaaaaababbaababbbbaaaaababaaabbabbbaababababbabaabaabbabbabbbbaabaabb
abaaaaaaabbaababbbaababbbbbaabbbbbaabbaa
ababbbabbabbbaabbbbbbbbb
abbaaaabbaabbbababaaaabb
bbababbbababbbababbabbbb
baabaaaababbabaaababaaabbbbaaabbbbbbbbbaaabbaaaaaaabbbba
baaabbabbaaaaaaababaaaabbaabbbba
abaaabbbbaabbaababababbaaabbbaaabaababab
bbbaabbaaabbabaababbababaabbabbbbabbaabaaaabbaabaabaabaabaaaabbb
aabbaabababaababaaababbbbabaabbb
abbaabbabaaabbabbaabaaab
bbbbabaababbbabaabaabbbb
baabaaaaababbbabbbbaaaaabbbabababaababaa
baaaababbbaaababbbabbaabaaabbaaa
babbabaabbaabbabbbabbabaabaaabab
aababaabbabaabbabbbabbba
aaaaaaaaabbaabaaaabaabbbabbabbab
babbbaabbbabbaaabbabbbbabaaabbbb
abbaaaaaabbbabbababbbbbb
babbabbabaababbaabbbabbbaaababaa
bbabbbaaaabaabbbaababaabaababaabaaaaabba
babbabaaaaabbbbbbbbabbba
baaaaaaabbbbbababbbbbbba
bbbbabaaaaaaabbbababbbba
aababbabbabaababbaaaabbbbaaabaaa
babaabbabbaaaabbbaabaaba
abbbaaabababababbbabbbbb
bbbbaabbababbabbababababbbbaaababbbaaaba
aabaaabaabbabababbaaaabbababaabbbbaabbba
bbbaabbabababbabbbbbbbbb
abbababbbbbbbaabbaaabbababbbbaabaabbaaaaabbbbbab
ababbabbbbaaabbbababbabbaaaaaaba
bbabaabababbbbabbababaabaabaabbaaabaabab
bbaaabbbbabaabbaaabbbaba
baaaabbbbaabbaaaabaaabaabaababaabbbaabaa
aababaababbaaaaaabaaaabb
bbbbabaababaababaaaaababbbbbabaababaababbbbaaaab
abababbbbababbbbbaaaabbbaabaaaaaababbabababbbbbbbbaabbba
bbaaaaaaabbbbaaabaaaaabb
bbabaaaaabbabaaababaaaabaaabbaab
bbbbbababaabbaaaaaaaaaaaabaaaabaabaabaabbaabaaab
baabbbabaaaaaaaabbbabaaaababbabbaaababab
aabbaabaabbabaaaaabbbbaabaaabbababbabbba
aaaabaababaaabaabbaaaaab
abaabbabababbbbbabbbabbabaabbaababababaa
bbbbaabbbbbbaabbbaabbbaaaabbbaabbaabbbababbbabababbaabbb
bbaabbaababbaabaabaaaabaaaabbaaabbababaabbaabbbbbabbaaaabbbbbbababbbababaabbaaaabbaaabbb
aabbbbbaaabaaaaabbaaaaaabbabaabbabbaaaabbbbbbbbbbbababbbbbababab
bbbbaabbbbbaaabaaabbabbabbababbaababaabb
abaaaabbaaaaaaabbbbaababbabbbbaabbababaaaabbabbb
bbaabaabaabbabbababbabaaababaababaaaaaba
bababbaaabaabbabaaababaaaabbaababaabbaabaabbabbababaabbabaaabaaaaababbabaabaaabb
bbbaaabaaaababbbbbaabaabbaabaaba
abbabaaabbaaaaaabaaaabaa
bbaababbbbaaababbabaaaaaaabababbaaabbabb
abaabaaaaaabbbbbabbabaab
abbbaabbaabaabbbbaaaaabb
abbaaaabaaaaababbaaaabbbababaaabbaaabaaa
bbbaaabbbbaabaabbaaaaaab
aabbbbaababbbabaabaabbba
aababbbbbaabbbaaaaaabbabaababbba
abaaaaaaaabaaaabbabaababbbababbaaabbbaabaaaababbbbbabbba
bbaaaabaabbbbaabaaababaababbaabbbabbbaaa
aabaabbbbaaaabbbaabaabbbbbabaaabbbabbbbaaabbbababababbbbbaabbbbb
aabbaabaabbaaabaaabaaaab
bbbaabbbabaaaaabaaaababb
babaaaabbbbabbaaaaaabaabaaaababa
baaaabbbbbaababbbbaabbab
bbabbbbabbabbbbaabbbbabb
baaabbababbbaaaabaabbabbaabbabbb
abaabaaababbbababbabbaabaababaaaaaabbbbabbbaabaaaaabbaaaababbababbbbbbaa
aabbbaabbabbabaaabbaaaaaababbaaaababaabaabababbbaaabbbbaaabbabab
babbaaabbaaabbababaaaaab
abbaaabaabbaaaabaabaaabaababbaba
bbaabbbbaabbaabbbaaababa
aabaabbabababbbbabbabbabaaabaaab
ababaabbbbbbbaaaababbaba
abbbbaaaabaabbabbaabbabbaabbbabb
babbabaaaabaaaabbbbbabab
bbaaaaaaaabaaaaaababaaaa
aaabaabbaaabaabbbbaaababaaababbbaaabaaabbababaaa
bbbaaabababaaaabbabaabaabbaabaabbbbbaaaa
aaaabbbbabbaabbaaabbbbbb
abbabaaabaabbbababbbaabbbabaaaaaaaabaabbbbbbbabb
bababaabbaabbaaaaababbbbaaababababababbb
bbbbaabbabbbbaabbbaaaaaaaabbbbaababaabaaaabbaaaabbbaabbb
aaaaaaabbbbbaaabbabbaabaababbababababbbaaabbabbbbaaaabaa
babbababbabaabbabababaaa
aaaabaabbabbbbaabbbbbaabbaaaaaabbbaaaaabaabaabbbbabbbabbabbaabba
aaaabbabaabaaaaabaabaaaaaaabaababbbaabaa
aababbaaabababbaaabbaaaa
baabaaaabaaabbbaabbbaabbbbbaaaab
baabbbabaaaabaabbabbababbabaaaabaabbbabaaaabaaabbbbbbabb
ababababbbaaaaaaababbbbbbbbabbab
aabbbaabbaaabbaabaabbaaaabbabaaa
bbbaabaabaabbabbaabaaabbbbbaabaabaabaabbbbabbbaabaabbbbbbbbbbaaaabbbabab
bbaaababaaaaaaaabbbaabbb
abbbbbaababbbbabaabaaabaaabbbbaaaabbaabababbaaaaabaaaabbbbbababa
abbaaabababaababaabbbbaaaabbbbaaababaaaa
abaaaabaabbaaabababababa
abbaababbaaabbbaababababaabbaabbbbaaabaa
abbaabaabaaaabbbbbbbaabbaaababbbababaaba
abbbbbaabaabbbaaaaaaababbaaaaabb
abaabaabbbaabaabaabaabab
aabaabbbabbaaaabaabbbaba
bbbbbbababbbbbbbbbababab
babbbbabbabbbbabbbbbaabbbbbbaabbaaaaaabbbbbaabaa
bbabbabbbbbbbabaabbaaaababbabbababaabbaabbbbbbaaabbbbbbaabbabababbabaababbaaaaba
abaaaabaaaababbbaaabbbbbabbbabbaaaababaa
aababaaabaaabbababaaabba
abbaabbabbabbbaabaaaaabb
aababaabbbaaaaaabaabbbaabbaabbbbabbbbaaaaaaababb
abaabbbbaabbabaabaaabbaaababaabaabbabaab
bbbbaaabbabababbbbbabbaabbbbbabbababaaaa
bbbbaabbaaabaabbbbbbbabb
abbbaaabbaabababbabbbaaa
abbaabababbbabbbbbaaabbbaabaaaabbbbaaababbbbabba
bbbababbabbbbaabbabaabababbbaabaaabbaaab
bbabbbbbabaaabbabbbaaabbbbbaaababbbaababaabaabbaaabbaaabbabaaabbbbbbabbaaabbbaab
aabbbaababbababababbabaabaabababbbaaaaab
babbaaababababbabbbbbbba
baabbaaabaaaababbbabbaabbbabaababbbbbbaaaaaaabaa
abaabaabbbaabaabbaaabbabaabbbbaabaaabaab
babbbbababbbbbbbaaaaabaa
babaabbaabaaaaaabababbaa
aabbbbaabbabbbbaabbbbbaabbbbbababaabbbabbaabaaabbbaabaaa
abbabbaaaabaaaaaababbaaaabababbbaaaabababaaabbaa
baaaaaaabbaababbbbabaabaababbaabbbaaaabaaaababab
bababbabaabaaababbbaabab
aaababbbaaabbbaaaaabbbab
aabaaaaabbbabaababaaaaab
aabbbbababbbbaabababbbabbaabaabb
bbaababbbbababbaaaababaa
baaaaaaabbaabbbbbaabaaba
aabbabaabaabbaabbbbabbbbaaabbaababbabbbb
bbbbbaabbabaaaaaabbabbab
bbaaaabbaaaabbbbbbbbbbbbbabababa
baaabbaabbabbbbaaabaaababbbbaaabbabbabababaaabab
bbbababbabbbabbbabbaabbababaabbb
bbabaababbbbbabaabaaaabaabaababa
bbaababbbbbbbbbabbabaabbbbaababa
abbababbabaabaabbaaabbabbbbababababaabbb
aabaabaaaabaaaaaaaaabbabaaababbbaaabbbbaabaaaaab
babbbbabababbbaabbaabbbaabbaababaabbbbbaabbbbbbabbaaaaaaaaaaaabbabababbb
bbabaaabbaabbaaaaabbbaba
ababbbbbbbababbbbbaaabbbaaababba
bbbbbbabaaaaabababbbbabb
bbbababbabbbbaabaaaaaabbaaaabbbbaaaaaababbaabbab
bbabbaaaaaaabaaaaabbabbb
babbaaabbbbaaaabbaababbbabbbabaababbbbbabbbabbbaaabbbbaaaaabaaaabaaabbbb
bbabbaababbaabbabaabbaaaaabbbbbbbbbabababbabbbababababaa
abbaaababababaabaaaababa
aaabbbbbabaabbababaaaabb
ababaaababaaaaaaaabbabaabbabbbbbbabbbaaa
aabababbbbaaabbaaaababababababbb
baaabbbaabbbbaabbbabbbbababaaaaaabaabaabbbaaabbaabbabbba
aaaabbababbbaaabababbbabbbabbaba
bbaabababbbaabaaaaaaaaaababbaaabbbbababbabbaaaabababbaaababaaabbaababaababaaaabaaaaabbaa
aabbaababababbabbaabbaba
aabbaabbaabaaabababbbbabaababbabbbaababbbabbbbaa
ababababaabbbbbbbaaabaaabababababaaababbaaaaabbababaabaaaaaaaabaaababaab
baabaaaabaaaabbbabbbbbbbabbabbaabbbaabab
abababbabbaaaaaaaabbabbabaabaaba
baabbbaababaaaabbbaababa
abbbabbaababaaababbbbbab
bbaaaabaabbaaabbbbabaaabbabbbbbbbbbabbabbbaabaaa
baaabbaaabaaaaaababaabbb
baaaaaaaaaabaabbaabbbbba
bbbbbbabaaaabbbbbbbaabbabbaabbba
bbbbbababaaababbabbbbaabbabbabbbaabbaaaabaaaabaaaaaabababbbababa
aaaaaabbbabaaaabbabbaaba
aabaaaaaababbbbbaababaabbbbabaabaabbbbaa
bbaabaabababbbabbabbabbababbabababaaabab
baabbbaababaabaabaaabbaaaabaabbababaabaaabbbabaa
bbbababbbabbaaaabbabbaaaaabbbbaababababbaaaababb
ababaaabaabaabbbbaaaabba
abaaaaaabbbababbbaaaabba
aaaabbababbbaaaabbabbaabbbaaabbbabbbbababbbaaaab
babaabbaabbbbaabbbbaabbb
bbaaaabaabbbbaabbbababbbaaaabbabbbaabbab
aababaabaabbbaabaabbaaaa
aaaabbbbbabbabaabaaaaaab
aabbabbabbbbbbabaaaababa
bbabbbbaabbbabbbabaabaabababbbbbabbabbbb
bbbaabbababbabbaababbaabbbbbabaaabbaaabbbaabababaabbababbbbabbbabbaabaaabbbbaaba
bbbabbaabbaababbbabbbbabaaaabbbbababbaaababaabbb
aaaabbabbaaaababaabbbabb
abaabaaababaabbaabababbaababbaaabbbaabbaabaaaabbbaaaaabbbbbaabbbaaaabaaa
bbababbabbbbaaabbabbbbabbbabaaabaaababaa
baabbaaabbbbabaabaaaaabb
aababbaaababbbbbbaaabbbaabbbabab
aaaabaabbbabaaaabbabababbbaabbbbbabbaaaabaaaaaab
babaabbaaababbaaabaabbaa
abaaabaaabaaabaaaababaaaaaaaabbb
bbbbaabbaabbbbaabbbababa
bbaaaabbaabbaabbbbbabbba
aabaaaababbabaaaabaabbabaaaaaababbbbbbbb
aababaabaabaabaaababbaba
bbaaaabababbabaaaaaabbbb
babbbaabbbbababbbbabbaabaababaaa
baaabbbaaaabbbaabbaababa
abbbbbbbbbbabaabbabbabbb
aabaabbbaabbabbababbaaabaabbabbbabbabaab
aaabaabbaabbbbaaabaababa
abbababbaabbbbaaaaaaaaaaaaabbbbbbabaabbb
aababaaaaabbbaabaaaaabbb
aaaabbbbbbbbaabaaabababaababbbaa
aabaabaaabbaaaababbabbab
aaabbbaabbbbabaaabaabbabbabbaaaaababaaabaaabaabbbaaabaab
bbaaabaaaabbabbbaabaaaaababbababbbabbbaa
bbaabbbbaabaabbaabbbbbab
baabbbaabbaaaabaaaaababa
aaaaaaaaabaabaababbaabbb
abbbbababbaababbbaababbaabaabbabbabaabbabaaaaaab
aabbbaabbbabbbaaaababbba
ababbaaaaabaabbbabababbb
aabbbaababbbabbbaababaaaabbbbababbbaabaaabaaabbbbbaabbaa
bbbaaabbaababaabaabbabbb
baaaaaababababbaaaabbbbaaabaabaa
abbaaabababbbbabbbbaabbaabaabaabaaaaaaabbaaabbbb
baaaabaaaabaabaabaaabbaabaababbaabbbbbabaabaaababbbabaabaaaababb
ababbabbbbbabbbbaababaaa
bbbaaabbbababbabbaabaabb
babbbaabbbababbbbbbabaababbbbabbbbbbabbabbaaaabaabababbabbbbbbbbabbbaaabaaabbbab
bbbaabbababaababbaabbbba
aabaaabbbbabbbbbbaabbbaababbaaabbaaaaabaaaaaabbbbbaaaabbbaabababbabbaabaabbabaaaaabbabab
aababbbbabaababbbbaababaaabbaaab
bbaaabaaabababbaaabbababaaaabaaabaabbaaabbaababaaaaababababababbbaaaabbabaaabaaaabbaabba
abbaababbaaababbbbbaaaababbabbbbbbabbaba
aaaabbaaaababaaabaaabbbabbabaabababaabbb
baabaaaababbabaaaaabaabbbaaaaababbbbabba
babbababbbbabbbbbabaaaaabaabbbaaaaaabaabaabbbbabbbaaabaa
babbbbabbbbbbbabaabbbaaa
abbaaaababababbaababaaabbaabbbabbabbabaabbaabbabbbbbabbb
bababaababbbaaabbabbaaba
bbabbbbaababaaabbaabbbaabbbaabbbbbbaabaa
abbaaaababbaaaabbabaaabbbbabbaaabaaaabababbbbbbaaaababaaabaabbaabababaaa
babaaaabaaaabbbbbaabbbabababbaba
abbaaaaaaabaaaaaaaababaa
aabbbaabaaaaabababaaaaab
baaabbbababaaaabbbbbabab
babbbabaaababaaaaabbbabb
bbabbaabbbaaaabaabbaababbbbbabba
abaabaabbababaabbababbabbbabbaaabbaabaaa
aabbaabaaababaaabbababab
bbababbaaaabaaaaaaaabbbbbbbaaaabbbaabbab
bbaababbbabbaaaaababbbabbbaaabba
bbbaaaaabbbabaabaabaaaaaabaabbbaaabbaaab
babbbababababbabbabbbabb
bbbbbbabbbaaabbbbabaabaa
bbaabbbbbbabababbbbabbabbaabbbbaaabaabbbbbabbbbbbaabaaaabababbbaaabbbaaa
bbbbbababbbabbbbabbbbbaaabbaabaaabbbabaaabababbb
aaaabbabaabbaaabbaaabbbabbabbabaababaaabaaabbaabbabbbbbabaabbabb
babbaaabbbabbbbbbbbabbbbbbbaabbaaabaabbabbababaaaaaabbaa
abbaababababaaababaaabaaabaabaabbbababbabbbbbaaaaaaabbba
bbbbbbabbabababbabbbaabbaababababbaabbababbbbbab
baaaabababbaaabbbaabbaba
aababbbbbaabbbabbaaaaaba
abbbbaaaababbabbabbaabbaabaabbba
bbbbbaabbabaaabbbbaaabba
babaabbabaaabbabbbaaaaaaabaaaababaaabbba
bbbaabaaaabbbaaabbabaabb
aaaabbabaabaabbaabaaabba
bbbabbaaaabbaababaabaaba
bbabbbbaabbbbbbbabababbabbbababa
baabbbabbabbaaabbbbaabab
abbaaaaababababbabaaaabaaabbbabaababbbba
aaabbbaabababaaaaabaabab
baaabbaabababbabbaababbb
abbaabbaaabbbaabbaaabaaa
ababaaabbabaaaaaabbaaaaabbaabaaa
ababababbbaabaababbbbbba
bbbbaaabbbabbaaabbbaaababbabbaaabaabbabbabbbabab
ababbaaabababaabbaababbaaaabbbab
abbbabbbaabbabaaaaaabaabbbbbbabb
aababaabbbaaaabbabbaabaababbbbbbbbbbbbba
bbbaaabbbbbaaabbabbbabaa
abbabaaaababbaaabababbaa
babbbabababaaabbbbbaabab
bbbabbbbbabaabaaabbbabab
aababbabbabbaaabbbbabbaaaaabbbba
aabababbbbbbaaabababaababbbaabbabbbababbabbabaabaabbbabbabbbabbb
aababbabbbabbaaaaabbaaaa
bbbabbaabbbbbabbaababababaabaabb
baaaababaabbaabbabbaaabbbaababbabbbbabab
aababbaaabbbbababbaababa
bbabaaabababbbabbaabaaaababbaabb
abbaaaabaaaaaabbaabbabbb
babaaabbbaabbbabbbabaaaabaaaaaaaabbbabaa
aabaabbbbbaabaabbbabaaaabababbba
abbbbababaabaababbbbabbbabaaabbbaaaaabbbabababaabbbaabaa
baaabbbabbaabaabababbbba
bbbaaaaaabbbbbaabbabaaabbbbaaaab
aababaabaabbbbaaaabaaabb
aabaabbbbabaababbabbbabaabababbb
bbabaaabbaaaaaaaaaaabbbbaaaaabaa
baaabbabbbbaaababbaaabbbababbaba
abaabbabbabbabbababaababbabbbabbbbbbbbbb
bbaaaaaabbbbaabbbbbbaaaabbaabbaa
aabbabaabbababbabbbaaaab
baaabbbbaaababaabababbba
bbababbabbbabbaabbaabbbbabbaabbbbbaaabba
baababbaaabbaababaaaabbbbaabbbba
baababbababbbaababbbaabbbbabbaababaabababbbabbba
baaabbbababbaaabaabaaabb
babbabbaaabbbbbbabaaabbb
bbbaaababbbabaaaababbbbbbaababaa
aaababbbaaabbbbbbbabaaabaaabbbaabbaabbbaaaaabbbabbababaa
bbababbababababbbbaaabaa
babaabbaaaabbabbbaababbbaaababab
baaabbbaabbaaababbbbbabb
bbaaabbbbaabbbabbaababbababaaaabbaaaaababbaaabaabababbba
aabaaaababaaabaababaaaabaaaaaaba
aabbbbaaabaabaabababbabbbaabbbaabaaabaabaaaaaabaaababbba
bbabbaabbbbabaaabbbaaababbbaaaabbbababab
aababbbbababaaaababbabba
babbaaaabbbbabaabaababbbababaaabaaaabaabbababbaabbbabbaa
bbabbaaabbabbbbabaabbaaa
bbabbbaabbaaaabbaaaababb
bbabbbbaabbbbababaaaaaaaabbaabbb
abaabaaaaaaaaabbabbabbbb
aabaaabaabababababaaaababbbbbbababaabbbbbbbbbbbbbaaabbbb
babababbbbaabaaababbaaababaababa
abbbbaaaaabaabaabaababbaababbbbabbabbbab
aabaabaaabbbbaaaaaaaaaaaaababaaabbabaaabababaaaaababbaba
aaaabaabababbabbaaabaabbabaababbbaaaabbbbbbababa
bbbaabbabaaabbabbababbba
ababbbabaababbbbbabbbbba
abbaaaaabaabbaaababbbbabbbbbaaababaaaabbaabbabab
baabbaabbbabbaaaabababbb
abbbaaababbabaaababaabaabaaaabba
ababbaaaabbaaaaabbbbaabbaaabaaaabaaaaaabaaaabaaaaabbaaaababbbbaa
abaaaaaabbaaaababababbabababbabbbbaaabaabbbaabaa
aabbbbabababbbbbbaabbaba
bbbababbbaaabbaaabaabbba
abbaabaaababbaaaaaabaabbbbaaaabaabbbaabaaabaabab
bbabbbaabaaabbabaaabaabbbbabbbaabbbaababbaaaaabbaabbbbba"""

@attr.s(frozen=True)
class Rule(object):
    is_match = attr.ib()
    options = attr.ib()
    char = attr.ib()
    is_recursive = attr.ib()


def solve(text):
    rules = {}
    messages = []

    parsing_rules = True

    for line in text.split("\n"):
        if not line:
            parsing_rules = False
            continue

        if parsing_rules:
            rule_name, rule = line.split(": ")
            match = None
            options = tuple()
            if rule[0] == '"':
                match = rule[1]
            else:
                options = tuple(tuple(map(int, o.split(" "))) for o in rule.split(" | "))
            rules[int(rule_name)] = Rule(
                is_match=match is not None,
                char=match,
                options=options,
                is_recursive=any(int(rule_name) in o for o in options)
            )
        else:
            messages.append(line)

    completely_matched = 0
    for message in messages:
        print("check message", message)
        answers = completely_matches_rule(message, rules, rules[0], is_last=True)
        print(f"{answers=}")
        if answers == [(True, True, "")]:
            completely_matched += 1
    return completely_matched

def completely_matches_rule(message, rules, rule, is_last, d=0):
    if not message:
        return [(False, False, message)]

    if rule.is_match:
        # print(f"{d*2*' '} match {message} against char {rule.char}")
        if message[0] == rule.char:
            return [(len(message) == 1 and is_last, True, message[1:])]
        return [(False, False, message)]

    partial_match_states = set()

    for composition in rule.options:

        # print(f"{d*2*' '} match {message} against {composition=}")

        remaining_messages = [message]
        new_remaining_messages = []

        for i, r in enumerate(composition):
            new_remaining_messages = []
            for remaining_message in remaining_messages:
                for fully_consumed, partial_match, new_remaining_message in completely_matches_rule(
                    remaining_message,
                    rules,
                    rules[r],
                    is_last and i == len(composition) - 1,
                    d+1
                ):
                    if fully_consumed:
                        return [(True, True, "")]

                    if partial_match:
                        new_remaining_messages.append(new_remaining_message)

            remaining_messages = new_remaining_messages

        for new_remaining_message in new_remaining_messages:
                partial_match_states.add((False, True, new_remaining_message))

    if partial_match_states:
        return list(partial_match_states)

    return [(False, False, message)]

if __name__ == "__main__":
    answer = solve(TEST_INPUT)
    assert answer == 12, f"got {answer}"
    print(solve(PUZZLE_INPUT))
