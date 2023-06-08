import numpy as np
from kin_func_skeleton import prod_exp

#########################################
#               EXAMPLE                 #
#########################################

def scara_fk(theta):
    """
    An example implementation of a forward kinematics map.
    Feel free to use this as a template for your own implementations
    in this file.

    This function implements the forward kinematics map of the
    SCARA manipulator, following Example 3.1 from MLS (page 87).
    
    We take L0 = L1 = L2 = 1

    Arguments:
        theta: numpy.ndarray of size (4,), the values of the joint angles.
               theta[i] is the value of the ith joint, at which the
               FK map should be computed.
    Returns:
        - g (numpy.ndarray of shape (4,4)): the 4x4 configuration of the 
          end effector when the joints have been placed at the angles
          specified in theta.
        - xi_array (numpy.ndarray of shape (6, N)): an array with the twists
          stacked in its columns. This is used by the autograder to assign
          partial credit.
    """

    # Specify all twists.
    xi_1 = [0, 0, 0, 0, 0, 1]
    xi_2 = [1, 0, 0, 0, 0, 1]
    xi_3 = [2, 0, 0, 0, 0, 1]
    xi_4 = [0, 0, 1, 0, 0, 0]

    # Specify end effector configuration at theta = 0.
    gst0 = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 2],
                     [0, 0, 1, 1],
                     [0, 0, 0, 1]], dtype=np.float64)

    # Stack twists into an array that prod_exp can accept.
    xi_array = np.array([xi_1, xi_2, xi_3, xi_4], dtype=np.float64).T

    # Use product of exponentials formula to compute forward kinematics.
    g = np.matmul(prod_exp(xi_array, theta), gst0)

    # Return the required quantities.
    return g, xi_array


#########################################
#              HW PROBLEMS              #
#########################################

def fk_1(theta):
    """
    Problem 1

    Arguments:
        theta: numpy.ndarray of size (3,), the values of the joint angles.
               theta[i] is the value of the ith joint, at which the
               FK map should be computed.
    Returns:
        - g (numpy.ndarray of shape (4,4)): the 4x4 configuration of the 
          end effector when the joints have been placed at the angles
          specified in theta.
        - xi_array (numpy.ndarray of shape (6, N)): an array with the twists
          stacked in its columns. This is used by the autograder to assign
          partial credit.
    """
    # Specify all twists.
    xi_1 = [0, 0, 0, 0, 0, 0]
    xi_2 = [0, 0, 0, 0, 0, 0]
    xi_3 = [0, 0, 0, 0, 0, 0]

    # Specify end effector configuration at theta = 0.
    gst0 = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]], dtype=np.float64)

    # Stack twists into an array that prod_exp can accept.
    xi_array = np.array([xi_1, xi_2, xi_3], dtype=np.float64).T

    # Use product of exponentials formula to compute forward kinematics.
    # Make a call to prod_exp from kin_func_skeleton and remember to
    # incorporate gst0
    g = None

    # Return the required quantities.
    return g, xi_array

def fk_2(theta):
    """
    Problem 2

    Arguments:
        theta: numpy.ndarray of size (3,), the values of the joint angles.
               theta[i] is the value of the ith joint, at which the
               FK map should be computed.
    Returns:
        - g (numpy.ndarray of shape (4,4)): the 4x4 configuration of the 
          end effector when the joints have been placed at the angles
          specified in theta.
        - xi_array (numpy.ndarray of shape (6, N)): an array with the twists
          stacked in its columns. This is used by the autograder to assign
          partial credit.
    """
    # Specify all twists.
    xi_1 = [0, 0, 0, 0, 0, 0]
    xi_2 = [0, 0, 0, 0, 0, 0]
    xi_3 = [0, 0, 0, 0, 0, 0]

    # Specify end effector configuration at theta = 0.
    gst0 = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]], dtype=np.float64)

    # Stack twists into an array that prod_exp can accept.
    xi_array = np.array([xi_1, xi_2, xi_3], dtype=np.float64).T

    # Use product of exponentials formula to compute forward kinematics.
    # Make a call to prod_exp from kin_func_skeleton and remember to
    # incorporate gst0
    g = None

    # Return the required quantities.
    return g, xi_array

def fk_3(theta):
    """
    Problem 3

    Arguments:
        theta: numpy.ndarray of size (6,), the values of the joint angles.
               theta[i] is the value of the ith joint, at which the
               FK map should be computed.
    Returns:
        - g (numpy.ndarray of shape (4,4)): the 4x4 configuration of the 
          end effector when the joints have been placed at the angles
          specified in theta.
        - xi_array (numpy.ndarray of shape (6, N)): an array with the twists
          stacked in its columns. This is used by the autograder to assign
          partial credit.
    """
    # Specify all twists.
    xi_1 = [0, 0, 0, 0, 0, 0]
    xi_2 = [0, 0, 0, 0, 0, 0]
    xi_3 = [0, 0, 0, 0, 0, 0]
    xi_4 = [0, 0, 0, 0, 0, 0]
    xi_5 = [0, 0, 0, 0, 0, 0]
    xi_6 = [0, 0, 0, 0, 0, 0]

    # Specify end effector configuration at theta = 0.
    gst0 = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]], dtype=np.float64)

    # Stack twists into an array that prod_exp can accept.
    xi_array = np.array([xi_1, xi_2, xi_3, xi_4, xi_5, xi_6], dtype=np.float64).T

    # Use product of exponentials formula to compute forward kinematics.
    # Make a call to prod_exp from kin_func_skeleton and remember to
    # incorporate gst0
    g = None

    # Return the required quantities.
    return g, xi_array