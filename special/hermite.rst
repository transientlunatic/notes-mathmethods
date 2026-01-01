Hermite Polynomials
===================

Hermite polynomials are the solutions to the hermite equation,

.. math::

   \label{eq:hermitede}
     \dv[2]{y}{x} - 2x \dv{y}{x} + 2n y = 0

 Hermite polynomials are solutions to the radial part of the Schrodinger
equation for the simple harmonic oscillator. Just like Legendre
polynomials and Bessel functions we can define Hermite polynomials,
:math:`H_n (x)` via a generating function:

.. math::

   \label{eq:hermite}
     g(x,t) = e^{-t^2 + 2tx} = \sum^\infty_{n=0} H_n(x) \frac{t^n}{n!}

Recurrence Relations for Hermite polynomials
--------------------------------------------

First we diferentiate with respect to :math:`t`,

.. math::

   \frac{\partial}{\partial t} g(x,t) = (-2t+2x) e^{-t^2+2tx} =
   \sum^{\infty}_{n=1} H_n(x) \frac{t^{n-1}}{n!}

Expanding, and putting into the generating function again,

.. math::

   -2 \sum^{\infty}_{n=0} H_n(x) \frac{t^{n+1}}{n!} + 2x
   \sum^{\infty}_{n=0} H_n(x) \frac{t^n}{n!} = \sum^{\infty}_{n=1}
   H_n(x)\frac{t^{n-1}}{(n-1)!}

 Relabelling the indices,

.. math::

   -2 \sum^{\infty}_{n=1} nH_{n-1}(x) \frac{t^{n}}{n!} + 2x
   \sum^{\infty}_{n=0} H_n(x) \frac{t^n}{n!} = \sum^{\infty}_{n=1}
   H_{n+1}(x)\frac{t^n}{n!}

 and finally equating coefficients of :math:`t^n`,

.. math::

   \label{eq:recurrencehermite}
     H_{n+1}(x) = 2x H_n(x) - 2n H_{n-1}(x) \qquad (n \ge 1)

 If we instead differentiate with respect to :math:`x`,

.. math:: \pdv{x}g(x,t) = 2t e^{-t^2+2tx} = \sum_{n=0}^{\infty} H^{\prime}_n(x) \frac{t^n}{n!}

 and substitute in :math:`g`,

.. math:: 2 \sum_{n=0}^{\infty} H_n(x) \frac{t^{n+1}}{n!} = \sum_{n=1}^{\infty} H^{\prime}_n(x) \frac{t^n}{n!}

 and relabelling,

.. math:: 2 \sum_{n=1}^{\infty} H_{n-1}(x) \frac{t^{n}}{(n-1)!} = \sum_{n=1}^{\infty} H^{\prime}_n(x) \frac{t^n}{n!}

 and then equating coeffients of :math:`t^n`,

.. math::

   \label{eq:recurrencehermite2}
     H_n^{\prime}(x) = 2n H_{n-1}(x)

 These can be used to derive the ordinary differential equation which
motivates these polynomials, from the previous results we can find

.. math:: H_{n+1}(x) = 2x H_n(x) - H^{\prime}_n(x)

 and then differentiate with respect to :math:`x`,

.. math::

   \begin{aligned}
     H^{\prime}_{n+1}(x) &= 2 H_n(x) + 2x H^{\prime}_n(x) - H^{\prime \prime}_n(x) \\
     2(n+1)H_{n}(x) &= 2 H_n(x) + 2x H^{\prime}_n(x) - H^{\prime \prime}_n(x) \end{aligned}

 and so

.. math:: \dv[2]{H_n(x)}{x} - 2x \dv{H_n(x)} + 2n H_n(x) = 0

It is possible to use the recurrence relations to find the Hermite
polynomials, so

.. math::

   \begin{aligned}
     H_0(x) &=  1 \\
     H_1(x) &=  2x \\
     H_2(x) &=  4x^2 - 2 \\
     H_3(x) &=  8x^3 - 12x \\
     H_4(x) &=  16x^4 - 48x^2 + 12\end{aligned}

.. plot::
   :caption: The Hermite polynomials of degrees 0 to 4.

   import matplotlib.pyplot as plt
   import numpy as np
   from scipy.special import hermite

   x = np.linspace(-3, 3, 601)

   for n in [0, 1, 2, 3, 4]:
      plt.plot(x, hermite(n)(x), label=f'$H_{n}(x)$')
   plt.ylim([-40, 50])
   plt.legend()
   plt.tight_layout()

Properties of the Hermite Polynomials
-------------------------------------

The Hermite polynomials are symmetric about :math:`x=0`, so

.. math::

   \label{eq:parityhermite}
     H_n(-x) = (-1)^n H_n(x)

The Hermite polynomials can be described by a specific series of the
form

.. math::

   \label{eq:hermiteseriesspef}
     H_n(x) = \sum_{m=0}^{\frac{n}{2}}(-1)^m (2x)^{n-2m} \frac{n!}{(n-2m)!m!}

And Rodrigues’s equation for Hermite polynomials also exists *proof is
an exercise*

.. math::

   \label{eq:rodrigueshermite}
     H_n(x) = (-1)^n e^{x^2} \dv[n]{x} \qty(e^{-x^2})

Orthogonality of Hermite Polynomials
------------------------------------

It is possible to show the orthogonality of the Hermite polynomials.
Starting at Hermite’s equation,

.. math::

   \begin{aligned}
     H_n^{\prime \prime}(x) - 2x H^\prime_n (x) + 2n H_n (x) &= 0 \\
   \dv{x} \qty( e^{-x^2} \dv{x} H_n (x) ) + 2n e^{-x^2} H_n(x) &=0 \end{aligned}

 then, proceeding in much the same way as with Legendre polynomials in
section [sec:orthogonallegendre],

.. math::

   \begin{aligned}
   \begin{split}
     H_m(x) \dv{x} \qty[ e^{-x^2} \dv{x} H_n(x) ] - H_n(x) \dv{x} \qty[ e^{-x^2} \dv{x} H_m(x)] \\= -H_m(x) \cdot 2 n e^{-x^2} H_n(x) + H_n(x) \cdot 2 m e^{-x^2} H_m(x) 
   \end{split}\end{aligned}

.. math::

   \begin{aligned}
   \begin{split}
   \int_{-\infty}^{\infty} H_m(x) \dv{x} \qty[ e^{-x^2} \dv{x} H_n(x)] \dd{x} \\= \qty[ H_m(x) e^{-x^2} \dv{x} H_n(x)]_{-\infty}^{\infty} - \int_{-\infty}^{\infty} \qty[ \dv{x} H_m(x)] e^{-x^2} \dv{x} H_n(x) \dd{x}
   \end{split}\end{aligned}

.. math::

   \begin{aligned}
     2(m-n) \int_{-\infty}^{\infty} H_n(x) H_m(x) e^{-x^2} \dd{x} &= 0 \\
   \therefore \int_{-\infty}^{\infty} H_n(x) H_m(x) e^{-x^2} \dd{x} &= 0 \text{ iff } n \neq m\end{aligned}

 Hermite polynomials are orthogonal on the interval
:math:`[-\infty, \infty]` with a weighting of :math:`\exp(-x^2)`.

.. math::

   \begin{aligned}
     \int_{-\infty}^{\infty} g^2(x,t) e^{(-x^2)} \dd{x} &= \int_{-\infty}^{\infty} \exp(-2t^2+4tx-x^2) \dd{x} \\
   &= \sum_{n=0}^{\infty} \sum_{m=0}^{\infty} \frac{t^{n+m}}{n! m!} \int_{-\infty}^{\infty} H_n(x) H_m(x) e^{(-x^2)} \dd{x} \\
   &= e^{2t^2}\int_{-\infty}^{\infty} e^{-x^2} \dd{x}\\
   &= e^{2t^2} \sqrt{\pi} \\
   &= \sqrt{\pi} \sum_{n=0}^{\infty} \frac{2^n}{n!} t^{2n}\end{aligned}

 Finally, equating powers of :math:`t^{2n}` gives

.. math:: \int_{-\infty}^{\infty} \qty[ H_n(x)]^2 \exp(-x^2) = 2^n \sqrt{\pi} n!

 so,

.. math::

   \label{eq:hermiteorthoweight}
   \int_{-\infty}^{\infty} H_n(x) H_m(x) \exp(-x^2) \dd{x} = 2^n \sqrt{\pi} n! \delta_{nm}

 it is also possible to remove the weighting by redefining the
polynomial as

.. math:: \phi_n(x) := \exp(-x^2) H_n(x)

 in this case

.. math::

   \label{eq:hermiteorthonoweight}
     \int_{-\infty}^{\infty} \phi_n(x) \phi_m(x) \dd{x} = 2^n \sqrt{\pi} n! \delta_{nm}

 these, however, are solutions not of Hermite’s equation, but of a
slightly variant equation,

.. math::

   \label{eq:modhermiteequation}
     \phi^{\prime \prime}_n(x) + (1-x^2+2n) \phi_n(x) = 0

The Quantum Harmonic Oscillator
-------------------------------

Returning to the one-dimensional time-independent Schrödinger equation,

.. math::

   \label{eq:1}
     - \frac{\hbar^2}{2m} \dv[2]{x} \psi(x) + V(x) \psi(x) = E \psi(x)

 with :math:`m` the mass of the particle, and :math:`E` its energy. For
the simple harmonic oscillator,

.. math:: V(x) \half m \omega^2 x^2

 so

.. math::

   \psi^{\prime \prime} (x) + \qty( - \frac{m^2 \omega^2}{\hbar^2} x^2
   + \frac{2m E}{\hbar^2} ) \psi(x) = 0

 which has a form very similar to the modified Hermite equation of the
previous section, and these describe the quantum harmonic oscillator.

Let :math:`y = ax` with :math:`a = \sqrt{\frac{m \omega}{\hbar}}`, so

.. math::

   \dv[2]{\psi}{y} + \qty( -y^2 + \frac{2mE}{\hbar^2 a^2} ) \psi =
   0

 Comparing the two equations, we get the solutions

.. math::

   \label{eq:2}
     \psi_n (x) = \sqrt{\frac{a}{2^n \sqrt{\pi} n!}} \exp( - \frac{a^2 x^2}{2} ) H_n(ax)

 which includes a normalisation constant. The energy is then given by
the equation

.. math::

   \begin{aligned}
     \frac{2 m E}{\hbar^2 a^2} &= 1 + 2n \nonumber\\
   \frac{2E}{\hbar \omega} &= 1 + 2n \nonumber\\
   E &= \hbar \omega \qty(n + \half)\end{aligned}

 but why does :math:`n` need to be an integer? The oscillator must have
:math:`\Psi
\to 0` as :math:`x \to \infty`. Taking solutions of the form

.. math:: \Psi \approx \exp( - \frac{x^2}{2} ) H_n(x)

 only guarantees this if :math:`n` is an integer; this can be
demonstrated by returning to Hermite’s equation, equation
([eq:hermitede]), and letting :math:`y =
\sum_{k=0}^{\infty} c_k x^k`, so that

.. math:: \sum_k c_k \qty( k(k-1) x^{k-2} - 2kx^k + 2nx^k ) = 0

 This must be true for each power of :math:`x` individually, so

.. math:: c_{k+2} (k+2) (k+1) - c_k(2k-2n)=0

 and if the series in :math:`k` goes on *ad infinitum*, we have the
behaviour

.. math:: \frac{c_{k+2}}{c_k} = \frac{2k - 2n}{(k+1)(k+2)} \to \frac{2}{k} \quad \text{as} \quad k \to \infty

 This has the power series behaviour of :math:`\exp(x^2)`, which would
imply that :math:`\Psi \approx e^{x^2} e^{-\frac{x^2}{2}} \approx
e^{\frac{x^2}{2}}`, giving “bad” behaviour as :math:`x \to \infty`. If
the series truncates this behaviour will not occur. This happens if
:math:`2n=2k` for some :math:`k`, that is, for :math:`n \in \mathbb{Z}`.
The solution of Hermite’s equation is a finite polynomial, and the
solution for :math:`\Psi` must be physical, so this forces :math:`n` to
be an integer.

The harmonic oscillator can also be solved using ladder operators, these
work due to the recurrence relation in equation
([eq:recurrencehermite2]). Writing

.. math:: \psi_n(x) = \sqrt{\frac{1}{2^n \sqrt{\pi} n!}} \exp( - \frac{x^2}{2} ) H_n(x)

 and, for simplicity, letting :math:`a=1`, then

.. math::

   \begin{aligned}
    \frac{1}{\sqrt{2}} \qty(x + \dv{x}) \psi_n(x) &= \sqrt{\frac{1}{2^{n+1} \sqrt{\pi} n!}} \qty( x+ \dv{x}) \exp(- \frac{x^2}{2}) H_n(x) \\
   %&= \sqrt{\frac{1}{2^{n+1} \sqrt{\pi} n!}} \qty( x \exp( - \frac{x^2}{2} ) H_n(x) - x \exp( - \frac{x^2}{2} ) H_n(x) + \exp( - \frac{x^2}{2}) H^{\prime}_n(x) ) 
   \\ & = \sqrt{n} \psi_{n-1}(x)\end{aligned}

 This is a lowering operator, it is also possible, using either
recurrence relations or the Rodrigues’ formula, that

.. math:: \frac{1}{\sqrt{2}} \qty( x - \dv{x} )

 is a raising operator.
