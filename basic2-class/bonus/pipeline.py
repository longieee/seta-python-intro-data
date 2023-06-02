import numpy as np
from datetime import datetime
import stage_1, stage_2

now = datetime.utcnow()
timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
date = now.strftime("%Y-%m-%d")


def generate_random_num_files() -> int:
    """
    Generating a random number of files for our fictional piepline to process.
    This function similates the real life scenarios that we might face
    DO NOT MODIFY THIS FUNCTION
    """
    dist = np.random.normal(loc=23.5, scale=8, size=1)
    return int(dist)


# Getting fake "real-world" input
num_files = generate_random_num_files()

# Main pipeline section
logs = "# ---------------------------------- Stage 1 --------------------------------- #\n"
stage1_results = stage_1.stage_execute(num_files=num_files, date=date)
logs += stage1_results

logs += "\n# ---------------------------------- Stage 2 --------------------------------- #\n"
stage_2_results = stage_2.stage_execute(date=date)
logs += stage_2_results

# Write log to files
with open(f"mysterious_process_logs/log-{timestamp}.txt", "a+") as f:
    f.write(logs)
