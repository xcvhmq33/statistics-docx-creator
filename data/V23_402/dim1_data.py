raw = """0.38  0.45  3.88  4.04  0.44  3.14  0.89  4.67  1.97  1.21  0.77  2.76  1.36  3.67  2.43  0.09  0.07  1.47  0.44  0.40  1.85  7.35  0.30  1.17  0.47
  1.13  0.34  4.25  0.11  0.02  2.91  2.05  6.65  2.57  2.33  0.79  0.40  2.50  6.49  2.08  5.31  0.43  2.72  0.79  0.37  0.26  1.01  0.18  0.64  2.67
  1.91  1.54  0.77  1.06  2.70  1.81  0.18  0.10  3.34  8.80  0.22  0.65  0.02  4.14  2.59  2.47  0.37  3.66  1.96  1.37  2.49  0.92  3.31  3.47  1.98
  0.01  0.03  1.85  0.57  4.20  1.15  2.26  3.56  0.44  2.07  1.06  1.89  0.48  0.49  2.49  2.20  0.42  0.03  0.14  4.12  0.24  3.42  0.60  0.26  2.79"""
str_dim1 = raw.replace("\n", " ").replace("  ", " ").replace(" ", ", ")
dim1 = [float(el) for el in raw.split()]