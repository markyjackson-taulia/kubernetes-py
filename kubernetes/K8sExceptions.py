#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.md', which is part of this source code package.
#


class UnauthorizedException(Exception):
    def __init__(self, *args, **kwargs):
        super(UnauthorizedException, self).__init__(*args, **kwargs)


class NotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        super(NotFoundException, self).__init__(*args, **kwargs)


class UnprocessableEntityException(Exception):
    def __init__(self, *args, **kwargs):
        super(UnprocessableEntityException, self).__init__(*args, **kwargs)


class BadRequestException(Exception):
    def __init__(self, *args, **kwargs):
        super(BadRequestException, self).__init__(*args, **kwargs)


class AlreadyExistsException(Exception):
    def __init__(self, *args, **kwargs):
        super(AlreadyExistsException, self).__init__(*args, **kwargs)


class TimedOutException(Exception):
    def __init__(self, *args, **kwargs):
        super(TimedOutException, self).__init__(*args, **kwargs)
