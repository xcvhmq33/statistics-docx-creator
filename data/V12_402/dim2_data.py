raw = """( -4.68;  3.81)  (  2.75; -3.75)  ( -6.13;  2.48)  ( -7.89;  3.23)  ( -7.73;  7.89)  ( -0.56; -1.20)  ( -4.85;  3.75)  ( -4.27; -0.60)  
( -3.57; -2.08)  ( -1.68; -0.94)  ( -1.19; -1.98)  ( -0.83;  0.31)  ( -5.83;  3.12)  ( -5.11;  4.48)  ( -4.08;  0.85)  ( -1.73; -1.35)  
(  0.17; -1.38)  ( -0.96; -1.24)  ( -3.37;  1.57)  (  0.02;  0.02)  ( -3.59;  1.61)  (  5.70; -3.42)  ( -5.36; -0.70)  ( -2.81;  0.20)  
( -0.51;  2.24)  ( -0.94; -0.07)  ( -6.60;  2.28)  ( -1.34;  1.26)  (  2.25; -4.85)  ( -2.01; -1.37)  ( -4.17;  3.06)  ( -2.84; -1.11)  
( -2.45; -0.57)  ( -0.45; -4.89)  ( -8.31;  5.01)  ( -6.01;  4.34)  ( -1.76;  0.84)  ( -2.82; -0.18)  (  3.50; -1.64)  ( -1.82; -1.74)  
( -1.24;  1.43)  (  1.92; -0.29)  ( -0.97;  3.22)  (  2.44; -1.95)  (  1.12;  0.91)  ( -0.85;  0.42)  (  0.19; -2.60)  ( -0.92;  2.73)  
(  0.17;  0.26)  ( -0.97; -1.20)"""
str_dim2 = raw.replace("\n", " ").replace("  ", " ").replace("( ", "(").replace(") ", "), ")
dim2 = [eval(el) for el in str_dim2.replace("), ", ") ").replace("; ", ",").split()]