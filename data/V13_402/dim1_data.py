raw = """-0.82 -3.06  0.17 -5.25 -8.36 -4.22 -4.52 -5.14 -13.41  1.41 -5.52  5.00 -2.12  1.51 -2.76 -1.25 -3.22 -1.03 -1.98 -5.61 -1.09  1.71  2.40  3.00 -4.57
 -3.33  1.29 -2.51 -1.75 -1.21 -6.35 -5.91 -5.06  1.12 -3.66  0.73 -5.06 -9.61  1.19  1.60 -7.09  2.20 -2.36 -9.17  4.48 -1.56 -3.22 -7.28 -8.66 -8.74
  2.67 -4.21 -1.42  1.56 -0.37  1.17 -2.79 -4.53  1.20  0.94 -4.36 -5.08 -10.06 -4.29 -4.46  0.07  3.85 -4.76 -2.11 -7.34 -0.27  0.96 -1.11 -4.47 -2.33
 -9.26  0.33 -6.17 -2.60 -3.53 -0.80 -7.15  3.48 -7.46 -6.41 -6.39 -1.43  5.59 -2.42 -3.00 -2.94  1.14 -0.95  0.65  0.75 -6.13  1.76  2.35 -0.08  5.27"""
str_dim1 = raw.replace("\n", " ").replace("  ", " ").replace(" ", ", ")
dim1 = [float(el) for el in raw.split()]