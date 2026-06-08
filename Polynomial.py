class Polynomial:

    def __init__(self, coeffs):
        self.coeffs = coeffs
#coeffs is a list of coefficients of the elements present


    #Help function for reference
    def help(self):

        functions = [
            ("display()", "Displays the polynomial in readable format e.g. 3x^2 + 2x^1 + 1"),
            ("evaluate(x)", "Evaluates the polynomial for a given value of x."),
            ("solution()", "Returns the root(s) of the polynomial. Works for linear and quadratic only."),
            ("degree()", "Returns the degree (highest power) of the polynomial."),
            ("derivative()", "Differentiates the polynomial and returns a new Polynomial."),
            ("integral()", "Integrates the polynomial and returns a new Polynomial."),
            ("add(other)", "Adds two polynomials and returns a new Polynomial."),
            ("subtract(other)", "Subtracts another polynomial from this one and returns a new Polynomial."),
            ("multiply(other)", "Multiplies two polynomials and returns a new Polynomial."),
    ]
    

    
        for name, description in functions:
            print(f"{name} : {description}")

    #Display the polynomial in proper format
    def display(self):
        y = ''
        for i in range(len(self.coeffs)):
            y += f'{self.coeffs[i]}x^{len(self.coeffs)-i-1} + '
        return y[:-3]

    #Evaluate the whole polynomial for a specific value
    def evaluate(self, x):
        ans = 0
        for i in range(len(self.coeffs)):
            ans += self.coeffs[i]*(x**(len(self.coeffs)-i-1))
        return ans

    #Find the solution of the polynomial
    def solution(self):
        #determinant value = (-b+-sqrt(b^2-4ac))/2a
        #determinant for linear = -b/a
        import math

        if len(self.coeffs) == 2:
            ans = -self.coeffs[1]/self.coeffs[0]
            return ans
        if len(self.coeffs) == 3:
            ans1 = ((-self.coeffs[1]) + (math.sqrt(self.coeffs[1]**2 - 4*self.coeffs[0]*self.coeffs[2])))/(2*self.coeffs[0])
            ans2 = ((-self.coeffs[1]) - (math.sqrt(self.coeffs[1]**2 - 4*self.coeffs[0]*self.coeffs[2])))/(2*self.coeffs[0])
            return ans1, ans2 if ans1 != ans2 else ans1
        else:
            print("This feature is limited for primary and secondary equations!")

    #Return the degree of the polynomial
    def degree(self):
        return len(self.coeffs) - 1

    #Differentiate the polynomial
    def derivative(self):
        new_list = []
        for i in range(len(self.coeffs)-1):
            element = self.coeffs[i] * (len(self.coeffs) - i - 1)
            new_list.append(element)

        return Polynomial(new_list)

    #Integrate the polynomial
    def integral(self):
        new_list = []

        for i in range(len(self.coeffs)):
            power = len(self.coeffs) - i
            if power != 0:
                element = self.coeffs[i] / power
                new_list.append(element)

        return Polynomial(new_list)

    #Add two different polynomials
    def add(self, other):
        a = self.coeffs[:]
        b = other.coeffs[:]

        while len(a) < len(b):
            a.insert(0, 0)

        while len(b) < len(a):
            b.insert(0, 0)

        new_list = []

        for i in range(len(a)):
            new_list.append(a[i] + b[i])

        return Polynomial(new_list)

    #Subtract two different modules
    def subtract(self, other):

        a = self.coeffs[:]
        b = other.coeffs[:]

        while len(a) < len(b):
            a.insert(0, 0)

        while len(b) < len(a):
            b.insert(0, 0)

        new_list = []

        for i in range(len(a)):
            new_list.append(a[i] - b[i])

        return Polynomial(new_list)

    #Multiply two different polynomials
    def multiply(self, other):
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)

        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i+j] += self.coeffs[i] * other.coeffs[j]

        return Polynomial(result)