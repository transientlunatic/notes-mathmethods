# the following block is required only for the pseudo-data
set xrange[0:20]
unset key
set terminal tikz
set output "../figures/bessel.tex"

fac(n) = (int(n)==0) ? 1.0 : int(n) * fac(int(n)-1.0)
besj_eps = 0.1
besj(n,x) = (n==0) ? besj0(x) : (n==1) ? besj1(x) : (abs(x)<besj_eps*(n+1)) \
? (x/2.0)**n/fac(n) : 2*(n-1)/x*besj(n-1,x) - besj(n-2,x) 

plot besj0(x), \
     besj1(x), \
     besj(2,x), \
     besj(3, x)
