class DemandException(Exception):
    pass


class DemandNotFoundException(DemandException):
    pass


class DemandPermissionException(DemandException):
    pass


class DemandValidationException(DemandException):
    pass