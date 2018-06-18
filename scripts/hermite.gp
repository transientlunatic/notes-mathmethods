# the following block is required only for the pseudo-data
set xrange[-3:3]
set yrange[-40:50]
unset key
#set terminal tikz
#set output "../figures/bessel.tex"


herm(n,x) = (n==0) ? 1 : (n==1) ? 2*x : 2*x*herm(n-1,x)-2*n*herm(n-2,x)

plot herm(0,x), \
     herm(1,x), \
     herm(2,x), \
     herm(3,x), \
     herm(4, x)
