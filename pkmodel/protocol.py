#
# Protocol class - currently redundant
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, value=43):
        self.value = value

if __name__ == '__main__':
    unittest.main()
