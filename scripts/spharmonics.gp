set terminal postscript
set output "spharm.ps"
set pm3d depthorder
set style fill transparent solid 0.65
unset colorbox
set style line 1 lc rgb '#157545' lt 1 lw 1 # --- green
set size square
set view equal xyz
set view 45,45,15,15
set mapping spherical
unset tics
unset border
set hidden
set xrange [-1.2*pi : 1.2*pi]
set yrange [-pi: pi]
set iso 100
unset key

set multiplot layout 1,5

leg(n,x) = (n==0) ? 1 : (n==1) ? x : ((2*n+1)*x*leg(n-1, x) - n*leg(n-2, x))/(n+1)
Y(l, u, v) = sqrt( (2*l+1)/(4*pi) ) * leg(l, cos(u)) * exp({0.0, 1.0}*v);

n = 0
unset key
#set title "$l=0$"
splot  '++' using ($1-pi):2:(Y(n, $1, $2)) w pm3d, \
       '++' using ($1+pi):2:(-Y(n, $1, $2)) w pm3d;

n = 1
unset key
#set title "$l=1$
splot  '++' using ($1-pi):2:(Y(n, $1, $2)) w pm3d, \
       '++' using ($1+pi):2:(-Y(n, $1, $2)) w pm3d;

n = 2
#set title "$l=2$
splot  '++' using ($1-pi):2:(Y(n, $1, $2)) w pm3d, \
       '++' using ($1+pi):2:(-Y(n, $1, $2)) w pm3d;

n = 3
#set title "$l=3$"
splot  '++' using ($1-pi):2:(Y(n, $1, $2)) w pm3d, \
       '++' using ($1+pi):2:(-Y(n, $1, $2)) w pm3d;

n = 4
#set title"$l=4$"
splot  '++' using ($1-pi):2:(Y(n, $1, $2)) w pm3d, \
       '++' using ($1+pi):2:(-Y(n, $1, $2)) w pm3d;

unset multiplot