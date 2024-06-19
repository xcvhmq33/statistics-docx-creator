raw = """4.52  7.94  6.50  0.76  0.59 10.46  1.54  2.76  5.12  2.65  2.05  1.73  2.47  3.31  2.13  0.97  0.82  0.33  3.42  0.07  1.82  3.46  0.52 12.42  0.90
  2.63  2.79  3.48  2.45  5.17  1.48  0.07  3.24  6.62  1.52  1.33  0.73  3.34  1.25 12.03  0.38  4.06  0.99  3.64  3.98  6.41  0.54  0.38  0.42  1.91
  0.32  5.00  5.15  1.12  1.77  1.23  0.45  1.68  0.29  0.36  1.84  2.00  0.21  4.45  0.44  3.28  0.13  7.68  8.42  0.01  9.54  5.71  0.74  2.90  3.00
  3.59  1.53  4.67  3.32 11.41 11.69  5.96  1.37  3.39  2.20  0.12  0.01  3.68  2.38  6.03  1.33  0.38  3.55  1.12  3.39  4.07  4.70  9.65  6.93  0.30"""
str_dim1 = raw.replace("\n", " ").replace("  ", " ").replace(" ", ", ")
dim1 = [float(el) for el in raw.split()]