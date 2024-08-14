import subprocess
import sys

def run_script(script_name):
    try:
        result = subprocess.run(
            ['python3', script_name],
            capture_output = True,
            text = True,
        )
        stdout = result.stdout
        stderr = result.stderr
        return_code = result.returncode

        return stdout, stderr, return_code
    
    except Exception as e:
        return str(e), None, -1

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 script_runner.py <script_to_run.py>")
        sys.exit(1)
    
    script_name = sys.argv[1]

    stdout, stderr, return_code = run_script(script_name)

    print("Standard Output")
    print(stdout)
    print("\n Standard Errror")
    print(stderr)
    print("\n Return Code")
    print(return_code)

if __name__ == "__main__":
    main()