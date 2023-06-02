"""
Stage 1 of our fictional pipeline
"""

from subprocess import Popen, PIPE, STDOUT


def stage_execute(num_files: int, date: str) -> str:
    """
    Executes the stage 1.
    """
    print("Executing stage 1..")
    output = Popen(["./mysterious_generation_script.sh", str(num_files), date], stdout=PIPE, stderr=STDOUT)
    stdout, _ = output.communicate()
    return stdout.decode("utf-8")
