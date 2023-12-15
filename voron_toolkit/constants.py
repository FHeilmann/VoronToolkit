from enum import Enum
from typing import NamedTuple

CI_PASSED_LABEL: str = "CI: Passed"
CI_FAILURE_LABEL: str = "CI: Issues identified"
CI_ERROR_LABEL: str = "Warning: CI Error"
PR_COMMENT_TAG: str = "<!-- voron_docker_toolkit -->"


class StepResultCodeStr(NamedTuple):
    result_code: int
    result_str: str


class StepIdName(NamedTuple):
    step_id: str
    step_name: str


class StepResult(StepResultCodeStr, Enum):
    SUCCESS = StepResultCodeStr(result_code=0, result_str="✅ SUCCESS")
    WARNING = StepResultCodeStr(result_code=1, result_str="⚠️ WARNING")
    FAILURE = StepResultCodeStr(result_code=2, result_str="❌ FAILURE")
    EXCEPTION = StepResultCodeStr(result_code=3, result_str="💀 EXCEPTION")


class StepIdentifier(StepIdName, Enum):
    CORRUPTION_CHECK = StepIdName(step_id="corruption_check", step_name="STL corruption checker")
    MOD_STRUCTURE_CHECK = StepIdName(step_id="mod_structure_check", step_name="Mod structure checker")
    README_GENERATOR = StepIdName(step_id="readme_generator", step_name="Readme generator")
    ROTATION_CHECK = StepIdName(step_id="rotation_check", step_name="STL rotation checker")
    WHITESPACE_CHECK = StepIdName(step_id="whitespace_check", step_name="Whitespace checker")


VORONUSERS_PR_COMMENT_SECTIONS: list[StepIdentifier] = [
    StepIdentifier.WHITESPACE_CHECK,
    StepIdentifier.MOD_STRUCTURE_CHECK,
    StepIdentifier.CORRUPTION_CHECK,
    StepIdentifier.ROTATION_CHECK,
]
