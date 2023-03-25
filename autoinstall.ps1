# Check if pipenv is installed
if (!(Get-Command pipenv -ErrorAction SilentlyContinue)) {
    # Install pipenv
    pip install pipenv
}

# Create a new pipenv environment using the requirements.txt file
python -m pipenv install

# Create a batch file to activate the environment and run main.py
$batFilePath = "$env:USERPROFILE\Desktop\slideshow_maker.bat"
@"
@echo off
cd $PWD
call python -m pipenv run python main.py
"@ | Set-Content -Path $batFilePath -Encoding ASCII

# Output the path to the batch file
Write-Host "Batch file created at $batFilePath"
