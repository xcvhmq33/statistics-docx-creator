raw = """( -11.71; -13.63)  ( 1.31; -3.47)  (  -1.42; -4.09)  ( -3.09; -6.19)  ( -7.29; -8.45)  ( -11.21; -15.55)  ( -4.74; -5.35)  ( -3.25; -3.59)  
( -11.48; 14.78)  ( -6.80; -5.40)  ( -5.72; -10.78)  (  -6.18;  -11.41)  ( -8.63; -2.63)  ( 0.80; -3.09)  ( -6.18; -8.30)  ( -9.13; -10.71)  
(  0.38;  -3.14)  ( -1.65; -4.62)  ( 0.55; -9.86)  ( -2.35; -2.28)  ( -5.99; -5.08)  ( -5.76; -9.90)  ( -3.83; -6.57)  (-8.29; -8.22)  
( -5.46;  -5.69)  (  -1.03; -7.10)  ( 1.07;  -4.24)  ( -11.07; -8.86)  ( -3.20; -4.83)  ( -5.27; 2.34)  (  -2.95; 0.81)  (  -9.58; -8.01)  
( -3.39; -4.16)  ( -16.48; -8.14)  (  -0.73; -5.14)  (  0.01; -5.60)  ( -2.62; -3.99)  ( -1.15; -6.20)  ( -5.37; -6.65)  ( -5.55; 0.57)  
(  -4.63; -10.05)  ( 0.57; -4.31)  ( -5.73; -12.26)  ( -0.55; -10.58)  ( 3.84; 1.45)  (  1.10; -3.65)  ( -5.31; -5.04)  (  -6.20; -11.62)  
( -6.19; -2.36)  ( -1.09; -2.79)"""
str_dim2 = raw.replace("\n", " ").replace("  ", " ").replace("( ", "(").replace(") ", "), ")
dim2 = [eval(el) for el in str_dim2.replace("), ", ") ").replace("; ", ",").split()]