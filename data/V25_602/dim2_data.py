raw = """(-2.60; -2.60) (-0.75; -4.33) (-4.08; -5.00) (-0.07; -4.52) (-1.33; -1.52) ( 1.43; -4.77) ( 2.35; 2.67) (-0.08; -6.37)
(-0.32; -1.47) (-1.08; -3.08) ( 5.18; 0.35) ( 0.21; -3.57) (-0.88; -2.14) (-3.47; -9.42) ( 4.63; 1.42) (-4.75; -3.95)
(-7.28; -6.12) (-3.14; -7.63) (-7.94; -5.55) ( 0.29; 2.37) ( 5.53; 3.60) (-2.71; -2.28) (-1.34; -3.01) (-0.79; -4.76)
(-3.24; -4.93) ( 1.76; 2.25) ( 5.86; 5.94) (-2.48; 4.96) ( 0.33; -4.32) (-1.66; 4.70) (-6.16; -2.22) ( 0.58; -0.45)
(-0.74; -0.20) ( 7.33; 5.11) ( 0.29; -0.78) (-1.87; -5.65) (-3.76; -7.30) ( 0.33; -3.36) ( 2.34; 2.03) (-3.22; -1.18)
(-1.76; -4.04) (-4.12; -3.00) ( 5.30; 1.10) ( 0.02; 0.07)
(-3.48; -6.16) (-1.73; 0.50) ( 0.02; 4.93) ( 5.75; 5.23)
( 0.17; 0.33) (-3.67; -0.62)"""
str_dim2 = raw.replace("\n", " ").replace("  ", " ").replace("( ", "(").replace(") ", "), ")
dim2 = [eval(el) for el in str_dim2.replace("), ", ") ").replace("; ", ",").split()]