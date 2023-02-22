import math
from sympy import *
import re


# Create Vector Class That Will Be The Blueprint For The Vector Instances That Will Be Created During Our Main Function
class Vector:

    # Initialize The Vector Instance With x, y, and z Components
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Find The Dot Product For Two Given Vectors, And Return A New Vector That Will Represent The Dot Product
    def find_dot(self, other_vector):
        return self.x * other_vector.x + self.y * other_vector.y + self.z * other_vector.z

    # Find The Cross Product Of Two Given Vectors And Return The Result Of A New Vector Which Is The Cross Product
    def cross_prod(self, other_vector):
        x = self.y * other_vector.z - self.z * other_vector.y
        y = -1 * (self.x * other_vector.z - self.z * other_vector.x)
        z = self.x * other_vector.y - self.y * other_vector.x
        return Vector(x, y, z)

    # With A Given Vector, Find The Magnitude And Return The Result In Its Most Simplified Form
    def magnitude(self):
        magnitude = sqrt(self.x**2 + self.y**2 + self.z**2)
        magnitude = simplify(magnitude)
        return pretty(magnitude)

    # With A Given Vector, Find The Unit Vector And Return It In The Format '< x / magnitude, y / magnitude, z / magnitude
    def unit_vector(self):
        mag = self.magnitude()
        return Vector(f'{self.x}/{mag}', f'{self.y}/{mag}', f'{self.z}/{mag}')

    # With Three Given Vectors, Find The Triple Scalar And Return A New Vector That Represents The Triple Scalar
    def triple_scalar(self, vector2, vector3):
        x = self.x * (vector2.y * vector3.z - vector2.z * vector3.y)
        y = -1 * (self.y * (vector2.x * vector3.z - vector2.z * vector3.x))
        z = self.z * (vector2.x * vector3.y - vector2.y * vector3.x)
        return Vector(x, y, z)

    # Check if the dot product of two given vectors is equal to the product of the magnitudes of
    # both vectors to determine whether they are parallel to each other
    def is_parallel(self, other_vector):
        mag1 = sqrt(self.x**2 + self.y**2 + self.z**2)
        mag2 = sqrt(other_vector.x**2 + other_vector.y**2 + other_vector.z**2)
        return self.find_dot(other_vector) == (mag1 * mag2)

    # Check if the dot product of two given vectors is equal to 0
    # to determine if the vectors are orthogonal to each other
    def is_orthogonal(self, other_vector):
        return self.find_dot(other_vector) == 0

    # If the two given vectors are neither parallel nor orthogonal, Find the angle between
    # the two vectors by taking the arccos of their dot product divided by the product of
    # their magnitudes then return the angle thats between them

    def find_angle(self, other_vector):
        dot_prod = self.find_dot(other_vector)
        mag1 = sqrt(self.x**2 + self.y**2 + self.z**2)
        mag2 = sqrt(other_vector.x**2 + other_vector.y**2 + other_vector.z**2)
        cos_theta = dot_prod / (mag1 * mag2)
        theta = math.acos(cos_theta)
        theta_degrees = math.degrees(theta)
        return round(theta_degrees, 4)

    # Determine the relationship of two vectors by using the previous class methods to find if the
    # Vectors are parallel, orthogonal or neither and returning what their relationship is
    def determine_relationship(self, other_vector):

        if self.is_parallel(other_vector):
            print(f"The Vectors {self} And {other_vector} Are Parallel")

        elif self.is_orthogonal(other_vector):
            print(f"The Vectors {self} And {other_vector} Are Orthogonal")

        else:
            print(
                f"The Vectors {self} And {other_vector} Are Neither Parallel Nor Orthogonal. The Angle Between The Two Vectors is {str(self.find_angle(other_vector))} Degrees.")

    # Create A String Instance Of The Vector Class
    def __str__(self):
        return f'<{self.x}, {self.y}, {self.z}>'


# Create an Expression class that acts as the blueprint for every expression given by the user
class Expression:
    x = symbols("X")

    def __init__(self, expression):
        self.expression = expression

    # Create a class method to take an User's expression and differentiate it.
    def take_deriv(self, variable):
        x = symbols(variable)
        expr = sympify(self.expression, locals={'x': symbols(f'{variable}')})
        deriv = expr.diff(x)
        return pretty(deriv)

    # Create a class method to take the User's expression and return its integral.
    def take_integral(self, variable, limits):
        x = symbols(variable)
        expr = sympify(self.expression, locals={'x': symbols(f"{variable}")})
        if limits is not None:
            lower_bound, upper_bound = limits
            integral = integrate(expr, (x, lower_bound, upper_bound))
            integral = round(integral, 4)
            return pretty(integral)
        elif limits is None:
            integral = integrate(expr, x)
            return pretty(integral)


# Main Function That Will Prompt The User For The Operation That Will Be Performed,
# And Take User Input For The Vector(s) Necessary To Complete The Operation
def main():

    # Create list Of Operations That Will Store The Operation Choices That Can Be Performed
    operations = ['dot product', '1', 'cross product', '2',
                  'magnitude', '3', 'unit vector', '4', 'triple scalar', '5', '6', 'take derivative of expression', '7', 'find angle between two vectors', '8', 'take integral', '9', 'quit', '10']

    # Ask The User What Operation They Would Like To Perform
    print("To Choose an Operation, You May Input The Name Of The Operation or Its Corresponding Number. \n")
    user_input = str(input(
        "\n 1. Dot Product \n 2. Cross Product \n 3. Magnitude \n 4. Unit Vector \n 5. Triple Scalar \n 6. Determine Vector Relationship. \n 7. Take Derivative Of Expression \n 8. Find Angle Between Two Vectors \n 9. Take Integral \n\n What Operation Would You Like Me To Perform For You?: \n").lower())

    # If The User's Input Is In The List Of Choices, Follow The Code Block Below
    if user_input in operations:

        # If The User's Input Is 'dot product' Take The Vector Components For The Vectors That Will Be Used In The Operation
        if user_input == 'dot product' or user_input == '1':
            x_1, y_1, z_1 = map(int, input(
                "Enter The x, y, and z Components In The Format x,y,z For Vector 1: \n").split(','))
            vector1 = Vector(x_1, y_1, z_1)
            x_2, y_2, z_2 = map(int, input(
                "Enter The x, y, And z Components In Th Format x,y,z For Vector 2: \n").split(','))
            vector2 = Vector(x_2, y_2, z_2)
            dot_prod = vector1.find_dot(vector2)
            print(f'The Dot Product Of {vector1} And {vector2} is {dot_prod}.')

        # If The User's Input Is 'cross product' Take The Vector Components For The Vectors That Will Be Used In The Operation
        elif user_input == 'cross product' or user_input == '2':
            x_1, y_1, z_1 = map(int, input(
                "Enter The x, y, and z Components In The Format x,y,z For Vector 1: \n").split(','))
            vector1 = Vector(x_1, y_1, z_1)
            x_2, y_2, z_2 = map(int, input(
                "Enter The x, y, And z Components In The Format x,y,z For Vector 2: \n").split(','))
            vector2 = Vector(x_2, y_2, z_2)
            cross_prod = vector1.cross_prod(vector2)
            print(
                f'The Cross Product Of {vector1} And {vector2} is {cross_prod}.')

        # If The User's Input Is 'magnitude', Grab The Vector Components Of The Vector That Will Be Used To Find The Magnitude.
        elif user_input == 'magnitude' or user_input == '3':
            x, y, z = map(int, input(
                "Enter The x, y, and z Components In The Format x,y,z For the Vector We Are Finding The Magnitude For: \n").split(','))
            vector = Vector(x, y, z)
            mag = vector.magnitude()
            print(f'The Magnitude Of {vector} Is {mag}.')

        # If User Chose 'unit vector', Grab the vector that will be used
        elif user_input == "unit vector" or user_input == "4":
            x, y, z = map(int, input(
                "Enter The x, y, and z Components In The Format x,y,z For the Vector We Will Use To Find The Unit Vector: \n").split(','))
            vector = Vector(x, y, z)
            u_vector = vector.unit_vector()
            print(f'The Unit Vector Of {vector} is {u_vector}.')

        elif user_input == "triple scalar" or user_input == "5":
            x_1, y_1, z_1 = map(int, input(
                "Enter The x, y, and z Components In The Format x,y,z For Vector 1: \n").split(','))
            vector1 = Vector(x_1, y_1, z_1)
            x_2, y_2, z_2 = map(int, input(
                "Enter The x, y, and z Components In The Format x,y,z For Vector 2: \n").split(','))
            vector2 = Vector(x_2, y_2, z_2)
            x_3, y_3, z_3 = map(int, input(
                "Enter The x, y, and z Components In The Format x,y,z For Vector 3: \n").split(','))
            vector3 = Vector(x_3, y_3, z_3)
            t_scalar = vector1.triple_scalar(vector2, vector3)
            print(
                f'The Triple Scalar For Vectors {vector1}, {vector2}, {vector3} Is: \n {t_scalar}.')

        elif user_input == '6':
            x_1, y_1, z_1 = map(int, input(
                "Enter The x, y, and z Components In Format x,y,z For Vector 1: \n").split(','))
            vector1 = Vector(x_1, y_1, z_1)
            x_2, y_2, z_2 = map(int, input(
                "Enter The x, y, and z Components In Format x,y,z For Vector 2: \n").split(','))
            vector2 = Vector(x_2, y_2, z_2)
            vector1.determine_relationship(vector2)

        elif user_input == 'take derivative of expression' or user_input == '7':
            expr = input(
                "Enter The Mathematical Expression You Would Like Me To Differentiate: \n")
            expression = Expression(expr)
            variable = input(
                "What Variable Are We Differentiating The Expression With Respect To: \n")
            result = expression.take_deriv(variable)
            print(f"The Derivative of {str(expr)} Is: \n {result}.")

        elif user_input == 'find angle between two vectors' or user_input == '8':
            x_1, y_1, z_1 = map(int, input(
                "Enter The x, y, and z Components For Vector 1: \n").split(','))
            vector1 = Vector(x_1, y_1, z_1)
            x_2, y_2, z_2 = map(int, input(
                'Enter The x, y, and z Components For Vector 2: \n').split(','))
            vector2 = Vector(x_2, y_2, z_2)
            result = vector1.find_angle(vector2)
            print(
                f"The Angle Between Vectors {vector1} and {vector2} Is {result}.")

        elif user_input == "take integral" or user_input == "9":
            integral_type = input(
                "What Kind Of Integral Would You Like To Perform? Indefinite or Definite? \n")
            if integral_type.lower() == "definite":
                lower_bound = float(input("Enter The Lower Bound: \n"))
                upper_bound = float(input("Enter The Upper Bound: \n"))
                limits = lower_bound, upper_bound
                expression = input(
                    "Enter The Expression You Would Like To Integrate: \n")
                variable = input(
                    "What Variable Are We Integrating With Respect To? \n")
                expr = Expression(expression)
                result = expr.take_integral(variable, limits)
                print(f"The Integral of {expression} Is: {result}.")

            elif integral_type.lower() == "indefinite":
                limits = None
                expression = input(
                    "Enter The Expression You Would Like To Integrate: \n")
                variable = input(
                    "What Variable Are We Integrating With Respect To? \n")
                expr = Expression(expression)
                result = expr.take_integral(variable, limits)
                print(f"The Integral of {expression} Is: \n {result}.")

        elif user_input == 'quit' or user_input == '10':
            print("Have A Good Day!")


main()
