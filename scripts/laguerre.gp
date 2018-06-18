# the following block is required only for the pseudo-data
set xrange[-1:5]
set yrange[-4:4]
unset key


lag(n,x) = (n==0) ? 1 : (n==1) ? 1-x : ((2*n-1-x)*lag(n-1,x)-(n-1)*lag(n-2,x))/(n)

plot lag(0,x), \
     lag(1,x), \
     lag(2,x), \
     lag(3,x), \
     lag(4, x)
