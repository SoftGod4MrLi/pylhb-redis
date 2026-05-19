import argparse
# Mr.Lee's Module
from .myredis import MyRedis

__all__ = [
    "MyRedis"
]

def main() -> None:
    parser = argparse.ArgumentParser(description="Mr.Lee's Redis Helpers")
    parser.add_argument('-v', '--version', action='store_true', help='show version')
    args = parser.parse_args()

    # show version
    if args.version:
        try:
            from importlib.metadata import version, PackageNotFoundError
            # 直接从包元数据获取版本号
            ver = version("pylhb-redis")
            print(f"pylhb-redis {ver}")
        except PackageNotFoundError:
            print("Package not found.")
        except ImportError:
            print("Import errored.")
        except:
            print("Other errored.")
        return
