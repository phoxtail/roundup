#!/usr/bin/env python
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
# $Id: version_check.py,v 1.2 2001-12-14 21:34:06 richard Exp $

import sys
if not hasattr(sys, 'version_info') or sys.version_info[:3] < (2,1,1):
    print "Content-Type: text/plain\n"
    print "Roundup requires Python 2.1.1 or newer."
    sys.exit(0)

#
# $Log: not supported by cvs2svn $
# Revision 1.1  2001/12/13 00:20:01  richard
#  . Centralised the python version check code, bumped version to 2.1.1 (really
#    needs to be 2.1.2, but that isn't released yet :)
#
#
#
# vim: set filetype=python ts=4 sw=4 et si
