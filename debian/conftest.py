import sys
from importlib.metadata import Distribution, DistributionFinder
from pathlib import Path


class UninstalledDistributionFinder(DistributionFinder):
    """Find wadllib's metadata despite it not being installed."""

    @staticmethod
    def find_spec(fullname, path=None, target=None):
        return None

    @staticmethod
    def find_module(fullname, path):
        return None

    @staticmethod
    def invalidate_caches():
        pass

    @staticmethod
    def find_distributions(context=DistributionFinder.Context()):
        if context.name == "wadllib":
            return [Distribution.at(Path(__file__).parent / "wadllib")]


sys.meta_path.append(UninstalledDistributionFinder)
