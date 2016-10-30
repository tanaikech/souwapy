"""
SOUWA means summing in Japanese.
"souwapy" can sum string elements in an array with the high speed.
The speed of souwapy with new algorithm is more than 1 digit faster
than that of the standard algorithm. You can see the detailed report
of this library
at [here](https://tanaikech.github.io/2016/10/13/improved-algorithms-for-summation-of-array-elements/).
If you are interested in this, I'm glad.

usage: getcsvdata(Array, Delimiter, End code)
ex. getcsvdata(ar, ",", "\\n")
"""

__author__ = "Kanshi TANAIKE (tanaike@hotmail.com)"
__copyright__ = "Copyright 2016, Kanshi TANAIKE"
__license__ = "MIT"
__version__ = "1.00"


class sou(object):
    """This is a base class of SOUWA."""

    def __init__(self):
        self.ar = []
        self.delimiter = ""
        self.endcode = ""
        self.sM = 3  # use standard method less than 3 digits for array elements

    def getcsvdata(self, ar, delim="", ec=""):
        """This is a main method of SOUWA."""

        self.ar = ar
        arlen = len(ar)
        arlen0 = len(str(ar[0]))
        self.delimiter = delim
        self.endcode = ec

        if arlen == 0:  # Array is empty.
            return "Array length is 0."
        elif arlen == 1:  # only one array element in Array
            return str(self.ar[0]) + self.endcode
        elif arlen0 == 1:  # 1 dimensional Array
            return self.delimiter.join(map(str, self.ar)) + self.endcode
        elif arlen == 1 and arlen0 >= 2:  # 1 dimensional Array
            return self.delimiter.join(map(str, self.ar)) + self.endcode
        elif arlen >= 2:  # more than 2 dimensional Array
            baseTheta = self.__getSeparate(self.ar, self.sM)
            baseThetalen = len(baseTheta)
            phi = 10  # phi = 10 for multiple of 10 from theoretical calculation
            if baseThetalen == 1:
                omegab = 1
            else:
                omegab = baseThetalen - 1 + self.sM

            result = [0 for i in range(baseThetalen)]

            poi = []
            poi.append([0, baseTheta[0]])
            pa = 0
            pb = 0
            for u in range(0, baseThetalen - 1):
                pa = poi[u][1]
                pb = poi[u][1] + baseTheta[u + 1]
                poi.append([pa, pb])

            souwaDat = ""
            theta = []
            for i in range(0, baseThetalen):
                omega = omegab - i - 1
                theta = self.ar[poi[i][0]:poi[i][1]]
                theta1 = []
                if omega == 0 or omega < self.sM:
                    result[i] = self.__Division_0(theta, self.delimiter, self.endcode)
                elif omega == 2:
                    theta1 = self.__Division_2(theta, phi, self.delimiter, self.endcode)
                    result[i] = self.__Division_4(theta1, phi)
                elif omega >= 3:
                    theta1 = self.__Division_2(theta, phi, self.delimiter, self.endcode)
                    for k in range(0, omega - 2):
                        theta2 = self.__Division_3(theta1, phi)
                        theta1 = theta2
                    result[i] = self.__Division_4(theta1, phi)
                theta = []
                souwaDat += result[i]
            return souwaDat
        return

    def __Division_0(self, theta, delim, ecode):
        string = ''
        for dat in theta:
            string += delim.join(dat) + ecode
        return string

    def __Division_1(self, theta, phi, delimiter, ecode):
        string = ''
        result = ''
        AP = 0
        thetalen = len(theta)
        for i in range(phi, thetalen + 1, phi):
            for j in range(AP, i):
                string += delimiter.join(theta[j]) + ecode
            AP = i
            result += string
            string = ''
        return result

    def __Division_2(self, theta, phi, delimiter, ecode):
        string = ''
        AP = 0
        thetalen = len(theta)
        Array = [0 for i in range(int(thetalen / phi))]
        ArrayP = 0
        for i in range(phi, thetalen + 1, phi):
            for j in range(AP, i):
                string += delimiter.join(theta[j]) + ecode
            AP = i
            Array[ArrayP] = string
            ArrayP += 1
            string = ''
        return Array

    def __Division_3(self, theta, phi):
        string = ''
        AP = 0
        thetalen = len(theta)
        Array = [0 for i in range(int(thetalen / phi))]
        ArrayP = 0
        for i in range(phi, thetalen + 1, phi):
            for j in range(AP, i):
                string += theta[j]
            AP = i
            Array[ArrayP] = string
            ArrayP += 1
            string = ''
        return Array

    def __Division_4(self, theta, phi):
        string = ''
        result = ''
        AP = 0
        thetalen = len(theta)
        for i in range(phi, thetalen + 1, phi):
            for j in range(AP, i):
                string += theta[j]
            AP = i
            result += string
            string = ''
        return result

    def __getSeparate(self, TArray, standardMethod):
        thetaLen = len(TArray)
        strthetaLen = str(thetaLen)
        mr = len(strthetaLen)
        if mr > standardMethod:
            theta_row = [0 for i in range(mr - standardMethod + 1)]
        else:
            theta_row = [""]

        if mr <= standardMethod:
            theta_row[0] = thetaLen
        else:
            for i in range(1, mr - standardMethod + 1):
                theta_row[i - 1] = int(strthetaLen[i - 1:i]) * pow(10, (mr - i))
            theta_row[i] = int(strthetaLen[mr - standardMethod:])
        return theta_row
