raw = """-2.18 -0.15 1.70 -0.36 -0.64 -2.32 -2.31 -3.35 -0.40 -0.56 0.89 -2.53 0.02 -0.56 1.80 0.40 -0.33 -2.40 -2.42 0.65 -4.17 -1.86 2.59 -4.72 -1.55
-0.94 -2.59 2.53 -1.47 2.33 -3.26 0.58 -2.75 -2.07 2.58 -0.82 0.45 2.66 -4.31 -3.82 2.98 0.96 2.33 -3.02 -2.91 -1.79 0.79 2.07 1.83 -1.75
-0.71 -4.67 2.33 1.90 -1.58 -0.58 -3.68 -0.77 1.06 -0.86 1.28 1.09 -1.07 -0.70 -4.25 0.45 0.40 -1.48 -2.14 -0.77 1.37 0.04 -0.82 2.93 -0.87
2.01 0.11 -2.85 1.97 -1.91 2.59 0.54 -2.78 -2.47 -1.98 0.33 -0.87 -2.65 -1.39 2.28 1.96 -1.65 -3.04 -2.73 2.87 1.41 0.28 1.96 2.33 1.21"""
str_dim1 = raw.replace("\n", " ").replace("  ", " ").replace(" ", ", ")
dim1 = [float(el) for el in raw.split()]