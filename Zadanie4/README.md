<b> Assignment 4</b>

Implementation of numerical integration using the Newton-Cotes and Gaussian methods.

Functionality guidelines:
- Newton-Cotes complex quadratures are calculated with the accuracy specified by the user.
- This is done iteratively.
- In each iteration, the number of subintervals into which the integration interval is divided is increased, and the integration result obtained is compared with the result from the previous iteration.
- If the result has changed by less than the accuracy specified by the user, it means that the accuracy of the integral on the specified interval has been calculated with the specified accuracy.
- Gaussian quadratures are calculated for 2, 3, 4 and 5 nodes.
- It is necessary to scale the function and integration limits to the interval [−1, 1).
- The report should compare the results obtained using both integration methods.
- It should be remembered that the integrated functions are of the form w(x) · f(x), where w(x) is the weighting function, where in Gaussian quadratures the weighting function is immediately included in the method.
- When calculating Newton-Cotes quadratures, therefore, the weighting function must be added.
