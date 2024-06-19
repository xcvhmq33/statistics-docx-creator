raw = """1.78  1.23  5.46  0.86  2.94  1.50  2.67  3.50  1.87  2.35  2.16  3.63  6.72  1.64  5.79  4.24  0.85  1.62  5.27 -0.91 -0.23  8.44  6.28  6.46  4.22
  4.07  4.47  6.44  2.75  0.53  3.21  2.07  3.46  4.03  5.68  0.29  1.54  5.32  0.44  3.52  6.53  1.78  3.48  7.55  0.33  4.56  0.65  6.00  1.33  1.18
  4.65  2.96  4.88  3.18  4.63  1.63  1.23  0.87  4.22  1.77  2.44  6.36  1.96  3.12  5.58  4.48  2.42  3.60  1.14 -0.61  2.63  4.21 -0.65  6.87  2.28
  0.06  1.22  3.48  0.72  1.78  5.10  2.97  0.72  6.22  5.80  3.38  4.41  5.43  3.17 -0.99  1.84 -1.63  3.01  3.14  3.59  0.51 -5.18  3.46  0.44  9.97"""
str_dim1 = raw.replace("\n", " ").replace("  ", " ").replace(" ", ", ")
dim1 = [float(el) for el in raw.split()]