from http import HTTPStatus

from src.shared.exceptions.base_exception import BaseException


class PreconditionFailedException(BaseException):

    def __init__(self, message=None):

        message = message or HTTPStatus.PRECONDITION_FAILED.phrase

        super().__init__(message=message, status_code=HTTPStatus.PRECONDITION_FAILED.value)