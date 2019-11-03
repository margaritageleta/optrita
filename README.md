# optrita 
Optimization algorithms by Rita ♥️

*pip3 install* with `! pip3 install -i https://test.pypi.org/simple/ optrita==0.0.3` 
<hr>

## Table of Contents
- [**Non-linear Optimization**](#non-linear-optimization)
    - [Parameters](#parameters)
    - [Linesearch](#linesearch)
    - [Unconstrained optimization](#uncontrained-optimization)
        - [First derivative methods](#first-derivative-methods)
            - [Gradient Method](#gradient-method)
            - [Conjugate Gradient Method](#conjugate-gradient-method)
            - [Broyden-Fletcher-Goldfarb-Shanno (BFGS) Method](#broyden-fletcher-goldfarb-shanno-bfgs-method)
        - [Second derivative methods](#second-deriavtive-methods)
            - [Newton Method](#newton-method)
            - [Modified Newton](#modified-newton)
                - [Modified Newton's method based on Spectral Decomposition](#modified-newtons-method-based-on-spectral-decomposition)
                - [Modified Newton's method based on the Cholesky factorization](#modified-newtons-method-based-on-the-cholesky-factorization)
<hr>

## Non-linear Optimization

### Parameters

### Linesearch

### Unconstrained Optimization

#### First derivative methods

##### Gradient Method 

##### Conjugate Gradient Method

##### Broyden-Fletcher-Goldfarb-Shanno (BFGS) Method

#### Second derivative methods

##### Newton Method
The rationale behind the Newton’s method is to subtitute, at each iterate $x^k$, the true function $f$ by the quadratic approximation <a href="https://www.codecogs.com/eqnedit.php?latex=f^k_Q" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f^k_Q" title="f^k_Q" /></a> around <a href="https://www.codecogs.com/eqnedit.php?latex=x_k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_k" title="x_k" /></a>:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(x^k&plus;p)&space;\approx&space;f^k_Q(p)&space;=&space;f^k&space;&plus;&space;\nabla&space;f^{k^T}\cdot&space;p&space;&plus;&space;\frac{1}{2}p^T&space;\cdot&space;\nabla^2&space;f^k&space;\cdot&space;p" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x^k&plus;p)&space;\approx&space;f^k_Q(p)&space;=&space;f^k&space;&plus;&space;\nabla&space;f^{k^T}\cdot&space;p&space;&plus;&space;\frac{1}{2}p^T&space;\cdot&space;\nabla^2&space;f^k&space;\cdot&space;p" title="f(x^k+p) \approx f^k_Q(p) = f^k + \nabla f^{k^T}\cdot p + \frac{1}{2}p^T \cdot \nabla^2 f^k \cdot p" /></a>

and then, to define the next iterate <a href="https://www.codecogs.com/eqnedit.php?latex=x^{k&plus;1}$&space;as&space;$x^{k&plus;1}&space;=&space;x^k&space;&plus;p^k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^{k&plus;1}$&space;as&space;$x^{k&plus;1}&space;=&space;x^k&space;&plus;p^k" title="x^{k+1}$ as $x^{k+1} = x^k +p^k" /></a> with <a href="https://www.codecogs.com/eqnedit.php?latex=p^k_N&space;:=&space;\arg&space;\min&space;{f^k_Q(p)}&space;=&space;-&space;\nabla^2f^{k^{-1}}&space;\cdot&space;\nabla&space;f^k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p^k_N&space;:=&space;\arg&space;\min&space;{f^k_Q(p)}&space;=&space;-&space;\nabla^2f^{k^{-1}}&space;\cdot&space;\nabla&space;f^k" title="p^k_N := \arg \min {f^k_Q(p)} = - \nabla^2f^{k^{-1}} \cdot \nabla f^k" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=x^{k&plus;1}&space;\leftarrow&space;x^k&space;-&space;\nabla^2f^{k^{-1}}&space;\cdot&space;\nabla&space;f^k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^{k&plus;1}&space;\leftarrow&space;x^k&space;-&space;\nabla^2f^{k^{-1}}&space;\cdot&space;\nabla&space;f^k" title="x^{k+1} \leftarrow x^k - \nabla^2f^{k^{-1}} \cdot \nabla f^k" /></a>

###### Global Convergence:

No guarantees! If <a href="https://www.codecogs.com/eqnedit.php?latex=x^0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^0" title="x^0" /></a> is far from a strict minimizer <a href="https://www.codecogs.com/eqnedit.php?latex=x^*$,&space;$p^k_N" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^*$,&space;$p^k_N" title="x^*$, $p^k_N" /></a> may not be a descent direction.

###### Local Convergence:
if the starting point <a href="https://www.codecogs.com/eqnedit.php?latex=x^0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^0" title="x^0" /></a> is sufficiently close to <a href="https://www.codecogs.com/eqnedit.php?latex=x^*" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^*" title="x^*" /></a> then:
+ $\{x^k\} \rightarrow x^*$
+ The order of convergence of $\{x^k\}^\infty_{k=0}$ is quadratic.
+ The sequence of gradient norms $\{\| \nabla f^k \|\}^\infty_{k=0}$ converges quadratically to zero.

##### Modified Newton
Modified Newton’s method where a positive definite approximation to the true hessian $\nabla^2f^{k}$ is used at each iteration, so as to make $d^k$ a descent direction:
$$
B^k = \nabla^2f^{k} + E^k
$$
Near the optimizer $x^*$ we want the $E^k=0$ and the step length $\alpha=1$ to exhibit Newton's quadratic convergence.

###### Global convergence
If we start at $x^0$ and the bounded modified condition holds:
$$
\kappa(B^k) \leq C, \space C>0, \forall k
$$
the algorithm converges to a stationary point.

###### Local convergence
Given that
+ The SOSC are satisfied at $x^*$.
+ The Hessian $\nabla^2 f$ is Lipschitz continuous in a neighborhood of $x^*$.
+ $E^k = 0$ for $k$ large enough.

Then the order of convergence is quadratic. 

If $\nabla^2 f^*$ is close to singular, the first point may not hold and then the convergence might be only linear.

##### Modified Newton's method based on Spectral Decomposition
The following function positifies any Hessian by decomposing it in the spectral decomposition and applying:
$$
B^k_{MN-SD} = Q \cdot diag (\max(\delta, \lambda_i)) \cdot Q^T
$$
It assures that the direction $d^k_{MN-SD}$ is a descent direction.

##### Modified Newton's method based on the Cholesky factorization
Cholesky factorization $A = R^T \cdot R$ exists if $A$ is a symmetric and definite positive. The following method is based on an iterative modification $\nabla^2 f^k$ that guarantees the positive definiteness of $B^k$:
$$
B^k = \nabla^2 f^k + \tau \cdot I
$$
With strictly increasingly $\tau \geq 0$ is going to be tried until the factorization succeeds for some $\tau$.

## License

MIT © `3omni`
