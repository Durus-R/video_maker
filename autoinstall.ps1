# Check if pipenv is installed
if (!(Get-Command pipenv -ErrorAction SilentlyContinue)) {
    # Install pipenv
    pip install pipenv
}

# Download the repository as a ZIP file
Invoke-WebRequest -Uri 'https://github.com/Durus-R/video_maker/archive/master.zip' -OutFile "$env:USERPROFILE\Downloads\repo.zip"

# Expand the ZIP file to the home directory
Expand-Archive "$env:USERPROFILE\Downloads\repo.zip" -DestinationPath $env:USERPROFILE

# Rename the extracted folder to "repo"
Rename-Item -Path "$env:USERPROFILE\video_maker-master" -NewName "slideshow_maker"

# Change to the repo directory
cd ~\repo

# Create a new pipenv environment using the requirements.txt file
pipenv install

# Create a batch file to activate the environment and run main.py
$batFilePath = "$env:USERPROFILE\Desktop\video_creator.bat"
@"
@echo off
cd $env:USERPROFILE\slideshow_maker
call pipenv shell
python main.py
"@ | Set-Content -Path $batFilePath -Encoding ASCII

# Output the path to the batch file
Write-Host "Batch file created at $batFilePath"
