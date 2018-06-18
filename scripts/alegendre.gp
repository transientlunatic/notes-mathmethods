#set dummy u,v;
# the following block is required only for the pseudo-data
set xrange[-1:1]
unset key
#set terminal tikz
#set output "../figures/bessel.tex"

aleg(l,m,x) = (l==0 && m==0) ? 1 : (l==1, m==0) ? x : (l=1, m=-1) ? -0.5*aleg(1,1,x): (l=1, m=1) ? - sqrt(1-x**2) : ( -2*(m-1)*x / sqrt(1-x**2) )*( aleg(l, m-1, x) ) - (l+(m-1))*(l-m)*aleg(l, m-2, x)


plot aleg(0,2,x)