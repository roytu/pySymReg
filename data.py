class Data(object):
    def variance(self, other):
        """
        >>> a = Data([1, 1, 1, 1])
        >>> b = Data([1, 1, 1, 1])
        >>> a.variance(b)
        0
        >>> b = Data([1, 2, 2, 1])
        >>> a.variance(b)
        2
        """
        assert len(self.data) == len(other.data), "Error: Arrays in variance must have same length"
        return sum(map(lambda i: abs(self.data[i] - other.data[i]), range(len(self.data))))

    def derivative(self):
        """
        >>> d = Data([1, 3, 4, 5, 2, 3])
        >>> d.derivative()
        [2, 1, 1, -3, 1, 0]
        """
        deriv = []
        for i in range(len(self.data)-1):
            deriv.append(self.data[i+1] - self.data[i])
        deriv.append(0)
        return deriv

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '  '.join(map(str, self.data))
