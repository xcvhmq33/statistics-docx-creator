raw = """( -3.25; -5.51)  ( -3.91; -3.09)  (  0.42; -4.46)  ( -5.82; -9.65)  ( -1.13; -2.29)  ( -6.23; -1.06)  ( -3.30; -3.03)  ( -8.92; -4.81)  
( -3.46; -5.79)  ( -6.82; -6.61)  ( -1.97; -5.08)  (  1.97;  0.21)  ( -3.08; -0.23)  ( -6.29; -4.60)  ( -0.41; -6.02)  (  3.79; -4.28)  
(  3.00;  1.50)  (  2.68; -4.48)  ( -5.76; -7.58)  ( -8.35; -2.68)  ( -3.20; -1.25)  ( -0.36; -0.02)  ( -5.26; -6.57)  (-10.28; -11.15)  
( -2.31;  0.76)  (  0.83; -6.90)  ( -3.42;  2.03)  ( -6.05; -1.67)  (  1.49; -2.38)  ( -4.00; -7.21)  (  4.22; -2.52)  (  0.46; -2.36)  
( -1.24; -2.93)  ( -7.99; -10.94)  (  0.55; -1.47)  (  1.26; -3.77)  ( -2.71; -0.45)  ( -2.78; -1.32)  ( -3.66; -11.99)  ( -2.40; -0.19)  
(  0.25; -1.28)  ( -4.08; -10.86)  ( -3.07; -3.10)  ( -1.55; -3.33)  ( -2.12; -1.42)  (  2.66; -4.86)  ( -5.52; -6.19)  (  0.25; -3.70)  
( -2.77; -6.50)  ( -1.91; -6.46)"""
str_dim2 = raw.replace("\n", " ").replace("  ", " ").replace("( ", "(").replace(") ", "), ")
dim2 = [eval(el) for el in str_dim2.replace("), ", ") ").replace("; ", ",").split()]