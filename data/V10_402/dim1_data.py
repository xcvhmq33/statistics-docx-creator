raw = """0.54  0.43  0.41  1.40  0.17  0.50  0.25  0.24  0.21  0.03  0.71  0.63  0.27  0.59  1.03  0.25  2.02  0.60  2.35  0.10  0.32  3.14  1.75  0.47  1.28
  1.67  0.01  0.04  1.39  0.86  1.01  0.34  1.30  0.02  0.13  0.86  0.76  0.18  0.74  2.10  0.94  0.19  0.67  0.61  0.33  1.48  1.08  1.13  0.39  1.42
  0.26  0.26  0.31  0.14  0.11  0.31  1.07  0.08  2.22  3.50  0.69  1.56  0.64  0.63  0.52  0.19  0.19  0.02  0.29  1.04  0.05  0.11  0.77  1.53  0.20
  0.94  0.81  0.49  1.23  0.18  0.01  0.63  0.92  3.57  0.81  1.77  2.05  1.42  0.61  0.40  1.47  1.13  1.02  1.36  0.12  0.86  2.25  0.57  0.34  0.20"""
str_dim1 = raw.replace("\n", " ").replace("  ", " ").replace(" ", ", ")
dim1 = [float(el) for el in raw.split()]