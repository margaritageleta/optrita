# optrita 
Optimization algorithms by Rita ♥️

*pip3 install* with `! pip3 install -i https://test.pypi.org/simple/ optrita==0.0.3` 
<hr>

## Table of Contents
- [**Non-linear Optimization**](#non-linear-optimization)
    - [Parameters](#parameters)
    - [Linesearch](#linesearch-bls)
    - [Unconstrained optimization](#uncontrained-optimization)
        - [First derivative methods](#first-derivative-methods)
            - [Gradient Method](#gradient-method-gm)
            - [Conjugate Gradient Method](#conjugate-gradient-method-cgm)
            - [Broyden-Fletcher-Goldfarb-Shanno (BFGS) Method](#broyden-fletcher-goldfarb-shanno-bfgs-method-bfgs)
        - [Second derivative methods](#second-deriavtive-methods)
            - [Newton Method](#newton-method-newton)
            - [Modified Newton](#modified-newton)
                - [Modified Newton's method based on Spectral Decomposition](#modified-newtons-method-based-on-spectral-decomposition-mnsd)
                - [Modified Newton's method based on the Cholesky factorization](#modified-newtons-method-based-on-the-cholesky-factorization-mncf)
<hr>

## Non-linear Optimization

### Parameters

### Linesearch `BLS`

### Unconstrained Optimization
<hr>

#### ~ First derivative methods ~
<hr>

### Gradient Method `GM`

### Conjugate Gradient Method `CGM`

### Broyden-Fletcher-Goldfarb-Shanno (BFGS) Method `BFGS`
<hr>

#### ~ Second derivative methods ~
<hr>

### Newton Method `newton`
The rationale behind the Newton’s method is to subtitute, at each iterate <a href="https://www.codecogs.com/eqnedit.php?latex=x^k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^k" title="x^k" /></a>, the true function <a href="https://www.codecogs.com/eqnedit.php?latex=f" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f" title="f" /></a> by the quadratic approximation <a href="https://www.codecogs.com/eqnedit.php?latex=f^k_Q" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f^k_Q" title="f^k_Q" /></a> around <a href="https://www.codecogs.com/eqnedit.php?latex=x_k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_k" title="x_k" /></a>:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(x^k&plus;p)&space;\approx&space;f^k_Q(p)&space;=&space;f^k&space;&plus;&space;\nabla&space;f^{k^T}\cdot&space;p&space;&plus;&space;\frac{1}{2}p^T&space;\cdot&space;\nabla^2&space;f^k&space;\cdot&space;p" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x^k&plus;p)&space;\approx&space;f^k_Q(p)&space;=&space;f^k&space;&plus;&space;\nabla&space;f^{k^T}\cdot&space;p&space;&plus;&space;\frac{1}{2}p^T&space;\cdot&space;\nabla^2&space;f^k&space;\cdot&space;p" title="f(x^k+p) \approx f^k_Q(p) = f^k + \nabla f^{k^T}\cdot p + \frac{1}{2}p^T \cdot \nabla^2 f^k \cdot p" /></a>

and then, to define the next iterate <a href="https://www.codecogs.com/eqnedit.php?latex=x^{k&plus;1}$&space;as&space;$x^{k&plus;1}&space;=&space;x^k&space;&plus;p^k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^{k&plus;1}$&space;as&space;$x^{k&plus;1}&space;=&space;x^k&space;&plus;p^k" title="x^{k+1}$ as $x^{k+1} = x^k +p^k" /></a> with <a href="https://www.codecogs.com/eqnedit.php?latex=p^k_N&space;:=&space;\arg&space;\min&space;{f^k_Q(p)}&space;=&space;-&space;\nabla^2f^{k^{-1}}&space;\cdot&space;\nabla&space;f^k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p^k_N&space;:=&space;\arg&space;\min&space;{f^k_Q(p)}&space;=&space;-&space;\nabla^2f^{k^{-1}}&space;\cdot&space;\nabla&space;f^k" title="p^k_N := \arg \min {f^k_Q(p)} = - \nabla^2f^{k^{-1}} \cdot \nabla f^k" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=x^{k&plus;1}&space;\leftarrow&space;x^k&space;-&space;\nabla^2f^{k^{-1}}&space;\cdot&space;\nabla&space;f^k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^{k&plus;1}&space;\leftarrow&space;x^k&space;-&space;\nabla^2f^{k^{-1}}&space;\cdot&space;\nabla&space;f^k" title="x^{k+1} \leftarrow x^k - \nabla^2f^{k^{-1}} \cdot \nabla f^k" /></a>

#### ~ Global Convergence ~

No guarantees! If <a href="https://www.codecogs.com/eqnedit.php?latex=x^0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^0" title="x^0" /></a> is far from a strict minimizer <a href="https://www.codecogs.com/eqnedit.php?latex=x^*$,&space;$p^k_N" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^*$,&space;$p^k_N" title="x^*$, $p^k_N" /></a> may not be a descent direction.

#### ~ Local Convergence ~
if the starting point <a href="https://www.codecogs.com/eqnedit.php?latex=x^0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^0" title="x^0" /></a> is sufficiently close to <a href="https://www.codecogs.com/eqnedit.php?latex=x^*" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^*" title="x^*" /></a> then:
+ <a href="https://www.codecogs.com/eqnedit.php?latex=\{x^k\}&space;\rightarrow&space;x^*" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\{x^k\}&space;\rightarrow&space;x^*" title="\{x^k\} \rightarrow x^*" /></a>
+ The order of convergence of <a href="https://www.codecogs.com/eqnedit.php?latex=\{x^k\}^\infty_{k=0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\{x^k\}^\infty_{k=0}" title="\{x^k\}^\infty_{k=0}" /></a> is quadratic.
+ The sequence of gradient norms <a href="https://www.codecogs.com/eqnedit.php?latex=\{\|&space;\nabla&space;f^k&space;\|\}^\infty_{k=0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\{\|&space;\nabla&space;f^k&space;\|\}^\infty_{k=0}" title="\{\| \nabla f^k \|\}^\infty_{k=0}" /></a> converges quadratically to zero.
<hr>
    
### Modified Newton
Modified Newton’s method where a positive definite approximation to the true hessian <a href="https://www.codecogs.com/eqnedit.php?latex=\nabla^2f^{k}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\nabla^2f^{k}" title="\nabla^2f^{k}" /></a> is used at each iteration, so as to make <a href="https://www.codecogs.com/eqnedit.php?latex=d^k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?d^k" title="d^k" /></a> a descent direction:

<a href="https://www.codecogs.com/eqnedit.php?latex=B^k&space;=&space;\nabla^2f^{k}&space;&plus;&space;E^k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B^k&space;=&space;\nabla^2f^{k}&space;&plus;&space;E^k" title="B^k = \nabla^2f^{k} + E^k" /></a>

Near the optimizer <a href="https://www.codecogs.com/eqnedit.php?latex=x^*" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^*" title="x^*" /></a> we want the <a href="https://www.codecogs.com/eqnedit.php?latex=E^k=0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E^k=0" title="E^k=0" /></a> and the step length <a href="https://www.codecogs.com/eqnedit.php?latex=\alpha=1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha=1" title="\alpha=1" /></a> to exhibit Newton's quadratic convergence.

#### ~ Global convergence ~
If we start at <a href="https://www.codecogs.com/eqnedit.php?latex=x^0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^0" title="x^0" /></a> and the bounded modified condition holds:

<a href="https://www.codecogs.com/eqnedit.php?latex=\kappa(B^k)&space;\leq&space;C,&space;\space&space;C>0,&space;\forall&space;k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\kappa(B^k)&space;\leq&space;C,&space;\space&space;C>0,&space;\forall&space;k" title="\kappa(B^k) \leq C, \space C>0, \forall k" /></a>

the algorithm converges to a stationary point.

#### ~ Local convergence ~
Given that
+ The SOSC are satisfied at <a href="https://www.codecogs.com/eqnedit.php?latex=x^*" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^*" title="x^*" /></a>.
+ The Hessian <a href="https://www.codecogs.com/eqnedit.php?latex=\nabla^2&space;f" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\nabla^2&space;f" title="\nabla^2 f" /></a> is Lipschitz continuous in a neighborhood of <a href="https://www.codecogs.com/eqnedit.php?latex=x^*" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^*" title="x^*" /></a>.
+ <a href="https://www.codecogs.com/eqnedit.php?latex=E^k&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E^k&space;=&space;0" title="E^k = 0" /></a> for <a href="https://www.codecogs.com/eqnedit.php?latex=k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k" title="k" /></a> large enough.

Then the order of convergence is quadratic. 

If <a href="https://www.codecogs.com/eqnedit.php?latex=\nabla^2&space;f^*" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\nabla^2&space;f^*" title="\nabla^2 f^*" /></a> is close to singular, the first point may not hold and then the convergence might be only linear.
<hr>

### Modified Newton's method based on Spectral Decomposition `MNSD`
The following function positifies any Hessian by decomposing it in the spectral decomposition and applying:

<a href="https://www.codecogs.com/eqnedit.php?latex=B^k_{MN-SD}&space;=&space;Q&space;\cdot&space;diag&space;(\max(\delta,&space;\lambda_i))&space;\cdot&space;Q^T" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B^k_{MN-SD}&space;=&space;Q&space;\cdot&space;diag&space;(\max(\delta,&space;\lambda_i))&space;\cdot&space;Q^T" title="B^k_{MN-SD} = Q \cdot diag (\max(\delta, \lambda_i)) \cdot Q^T" /></a>

It assures that the direction <a href="https://www.codecogs.com/eqnedit.php?latex=d^k_{MN-SD}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?d^k_{MN-SD}" title="d^k_{MN-SD}" /></a> is a descent direction.
<hr>

### Modified Newton's method based on the Cholesky factorization `MNCF`
Cholesky factorization <a href="https://www.codecogs.com/eqnedit.php?latex=A&space;=&space;R^T&space;\cdot&space;R" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A&space;=&space;R^T&space;\cdot&space;R" title="A = R^T \cdot R" /></a> exists if <a href="https://www.codecogs.com/eqnedit.php?latex=A" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A" title="A" /></a> is a symmetric and definite positive. The following method is based on an iterative modification <a href="https://www.codecogs.com/eqnedit.php?latex=\nabla^2&space;f^k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\nabla^2&space;f^k" title="\nabla^2 f^k" /></a> that guarantees the positive definiteness of <a href="https://www.codecogs.com/eqnedit.php?latex=B^k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B^k" title="B^k" /></a>:

<a href="https://www.codecogs.com/eqnedit.php?latex=B^k&space;=&space;\nabla^2&space;f^k&space;&plus;&space;\tau&space;\cdot&space;I" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B^k&space;=&space;\nabla^2&space;f^k&space;&plus;&space;\tau&space;\cdot&space;I" title="B^k = \nabla^2 f^k + \tau \cdot I" /></a>

With strictly increasingly <a href="https://www.codecogs.com/eqnedit.php?latex=\tau&space;\geq&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\tau&space;\geq&space;0" title="\tau \geq 0" /></a> is going to be tried until the factorization succeeds for some <a href="https://www.codecogs.com/eqnedit.php?latex=\tau" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\tau" title="\tau" /></a>.
<hr>

## License

MIT © `3omni`
