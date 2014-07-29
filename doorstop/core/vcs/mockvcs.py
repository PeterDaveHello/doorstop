"""Plug-in module to simulate the storage of requirements in a repository."""


from doorstop import common
from doorstop.core.vcs.base import BaseWorkingCopy

log = common.logger(__name__)  # pylint: disable=C0103


class WorkingCopy(BaseWorkingCopy):  # pragma: no cover (integration test)

    """Simulated working copy."""

    DIRECTORY = '.mockvcs'

    def lock(self, path):
        log.info("simulated lock on: {}...".format(path))

    def save(self, message=None):
        log.info("simulated save")

    @property
    def ignores(self):
        return ("*/env/*", "*/apidocs/*", "*/build/lib/*")
