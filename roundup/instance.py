#
# Copyright (c) 2001 Bizar Software Pty Ltd (http://www.bizarsoftware.com.au/)
# This module is free software, and you may redistribute it and/or modify
# under the same terms as Python, so long as this copyright message and
# disclaimer are retained in their original form.
#
# IN NO EVENT SHALL BIZAR SOFTWARE PTY LTD BE LIABLE TO ANY PARTY FOR
# DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING
# OUT OF THE USE OF THIS CODE, EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# BIZAR SOFTWARE PTY LTD SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING,
# BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE.  THE CODE PROVIDED HEREUNDER IS ON AN "AS IS"
# BASIS, AND THERE IS NO OBLIGATION WHATSOEVER TO PROVIDE MAINTENANCE,
# SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
# 
# $Id: instance.py,v 1.4 2001-11-12 22:01:06 richard Exp $

''' Currently this module provides one function: open. This function opens
an instance.
'''

import imp, os

class Opener:
    def __init__(self):
        self.number = 0
        self.instances = {}

    def open(self, instance_home):
        '''Open the instance.

        Raise ValueError if the instance home doesn't exist.
        '''
        if not os.path.exists(instance_home):
            raise ValueError, 'no such directory: "%s"'%instance_home
        if self.instances.has_key(instance_home):
            return imp.load_package(self.instances[instance_home],
                instance_home)
        self.number = self.number + 1
        modname = '_roundup_instance_%s'%self.number
        self.instances[instance_home] = modname
        return imp.load_package(modname, instance_home)

opener = Opener()
open = opener.open

del Opener
del opener


#
# $Log: not supported by cvs2svn $
# Revision 1.3  2001/08/07 00:24:42  richard
# stupid typo
#
# Revision 1.2  2001/08/07 00:15:51  richard
# Added the copyright/license notice to (nearly) all files at request of
# Bizar Software.
#
# Revision 1.1  2001/08/05 07:43:52  richard
# Instances are now opened by a special function that generates a unique
# module name for the instances on import time.
#
#
#
# vim: set filetype=python ts=4 sw=4 et si
