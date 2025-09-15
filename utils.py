

from sys import executable
from subprocess import check_call, CalledProcessError, DEVNULL
from pkg_resources import get_distribution, DistributionNotFound


def install_package(package, version="upgrade"):
    result = False

    def try_install(args, suppress_stderr=False):
        try:
            stderr = DEVNULL if suppress_stderr else None
            check_call([executable, "-m", "pip", *args], stderr=stderr)
            return True
        except CalledProcessError:
            return False

    if version.lower() == "upgrade":
        args = ["install", package, "--upgrade"]
        result = try_install(args + ["--user"], suppress_stderr=True)
        if not result:
            result = try_install(args)
    else:
        try:
            installed_version = get_distribution(package).version
            if installed_version == version:
                return True
        except DistributionNotFound:
            pass
        install_version = f"{package}=={version}" if ">=" not in version else f"{package}{version}"
        args = ["install", install_version]
        if not try_install(args + ["--user"], suppress_stderr=True):
            result = try_install(args)

    return result
