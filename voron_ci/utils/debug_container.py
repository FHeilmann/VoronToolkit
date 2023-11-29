import os

from voron_ci.utils.logging import init_logging

logger = init_logging(__name__)


def print_container_info() -> None:
    logger.setLevel("INFO")
    logger.info("## Debugging environment variables:\n")
    logger.info("\tGITHUB_OUTPUT=%s", os.environ.get("GITHUB_OUTPUT", ""))
    logger.info("\tGITHUB_STEP_SUMMARY=%s", os.environ.get("GITHUB_STEP_SUMMARY", ""))
    logger.info("\tGITHUB_REF=%s", os.environ.get("GITHUB_REF", ""))
    logger.info("\tGITHUB_REPOSITORY=%s", os.environ.get("GITHUB_REPOSITORY", ""))
    logger.info("\tGITHUB_TOKEN=%s", os.environ.get("GITHUB_TOKEN", ""))
