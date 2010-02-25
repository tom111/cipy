""" A CI-statement is a triple of disjoint sets of integers """
class CIStatement(object):
    def __init__(self, statement):
        # Todo: Check for no intersection
        self.A = statement[0]
        self.B = statement[1]
        self.C = statement[2]

    def __str__(self):
        return (str(self.A) + " \indep " + str(self.B) + " \given " + str(self.C))
