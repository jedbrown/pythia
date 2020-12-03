#!/usr/bin/env python
#
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005 All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .Composition import Composition


class Binary(Composition):


    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        return


# version
__id__ = "$Id: Binary.py,v 1.1.1.1 2005/03/08 16:13:46 aivazis Exp $"

#
# End of file
