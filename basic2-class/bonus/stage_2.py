"""
Stage 2 of our fictional pipeline
"""

from subprocess import Popen, PIPE, STDOUT


def script_execute(date):
    """
    Code to run our mysterious and wierd script.
    This is the script throwing the error and breaking out pipeline, but we can do nothing to this one.

    DO NOT MODIFY THIS FUNCTION
    """
    output = Popen(["./mysterious_result_script.sh", date], stdout=PIPE, stderr=STDOUT)
    return output


def stage_execute(date: str):
    print("Executing stage 2..")
    output = script_execute(date=date)
    stdout, _ = output.communicate()
    return stdout.decode("utf-8")
