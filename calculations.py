from data.values import Values
from numpy import mean


class CalculatedValues(Values):
    def get_b_value(self, X):
        return self._calculate_b(X)

    def _calculate_b(self, X_array):
        pass
        B_values = []

        for x in X_array:
            B_values.append(self._calculate_B_singular(x))

        return mean(B_values)


    def _calculate_Y_singular(self, x):
        m = self.get_m()
        c = self.get_c()

        result = m * x
        return result + c

    def _calculate_B_singular(self, x):
        return self._calculate_A_singular(x) + self._calculate_Y_singular(x)

    def _calculate_A_singular(self, x):
        return (1 / x) or (1 % x)

#Function 1:
#Y=mX+c
#Function 2:
#B=A+Y
#b=mean(B)
#Function 3:
#A=1X
#Function 4:
#C=X+b