
import subprocess

def run_program(command, input_data):
    result = subprocess.run(
        command, input=input_data.encode(),
        capture_output=True, text=True
    )
    return result.stdout.strip()

def test_case1():
    assert run_program(["python3", "questão1/main.py"], "2 3") == "5"

def test_case2():
    assert run_program(["python3", "questão1/main.py"], "10 20") == "30"
