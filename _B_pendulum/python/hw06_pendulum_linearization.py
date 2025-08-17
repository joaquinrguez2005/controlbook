#%%
from hw03_pendulum_solving_for_state_variable_form import *

#%%
############################################################
### Defining vectors for x_dot, x, and u, then taking partial derivatives
############################################################


# defining derivative of states, states, and inputs symbolically
### for this first one, keep in mind that zdd_eom is actually a full
### row of equations, while zdd is just the symbolic variable itself. 
state_variable_form = Matrix([[zd], [thetad], [zdd_eom], [thetadd_eom]])
states = Matrix([[z], [theta], [zd], [thetad]])
inputs = Matrix([[F]])


# finding the jacobian with respect to states (A) and inputs (B)
A = state_variable_form.jacobian(states)
B = state_variable_form.jacobian(inputs)

# sub in values for equilibrium points (x_e, u_e) or (x_0, u_0)
A_lin = simplify(A.subs([(thetad,0.), (theta,0.), (zd,0.), (z,0.), (F, 0.)]))
B_lin = simplify(B.subs([(thetad,0.), (theta,0.), (zd,0.), (z,0.), (F, 0.)]))

display(Math(vlatex(A_lin)))
display(Math(vlatex(B_lin)))

#%%

# define 's' as symbolic variable for the Laplace domain
s = sp.symbols('s')
I = sp.eye(A_lin.shape[0])

#%%

# define C and D 
C = sp.Matrix([[1, 0, 0, 0],
               [0, 1, 0, 0]])

D = sp.Matrix([[0],
                [0]])


# calc H(s) 
H = C @ (s*I - A_lin).inv() @ B_lin + D

H = H.subs([(m1, 1), (m2, 1), (ell, 0.1), (b, 0.1)])
display(Math(vlatex((sp.cancel(H)))))



# %%
# TODO - this form of substitution is OK because they are all 0, however, substituting
# 0 (or any constant) for theta, will also make thetad zero. This is a known issue - (see "substitution" 
# at https://docs.sympy.org/latest/modules/physics/mechanics/advanced.html). Future 
# examples should substitute for dynamic symbols after the EOM are derived, and before
# substituting in the equilibrium points. It may be OK because velocity variables like
# thetad and zd should be zero at an equilibrium point, and would be for any constant value
# of the generalized coordinates in the state vector, but it is something to be aware of.

# see also use of "msubs" at link above for speed up in substitution in large expressions. 