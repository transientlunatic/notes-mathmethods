#set dummy u,v;
# the following block is required only for the pseudo-data
set xrange[-1:1]
unset key
#set terminal tikz
#set output "../figures/bessel.tex"

leg(n,x) = (n==0) ? 1 : (n==1) ? x : ((2*n+1)*x*leg(n-1, x) - n*leg(n-2, x))/(n+1)

#u(x,y) = sqrt(x**2 + y**2)
Y(l, u, v) = sqrt( (2*l+1)/(4*pi) ) * leg(l, cos(u)) * real( exp({0.0, 1.0}*v) )

theta(z,r) = acos(z/r)
phi(y,x) = atan(y/x)

#plot leg(0, x), leg(1,x), leg(2,x), leg(3,x), leg(4, x)

set mapping spherical
set parametric
#splot Y(1, u, v)
#set mapping cylindrical
#splot Y(1, x, y)