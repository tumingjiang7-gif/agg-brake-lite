$ErrorActionPreference = "Stop"

function Get-WslPath {
    param([string]$WindowsPath)

    $full = [System.IO.Path]::GetFullPath($WindowsPath)
    $drive = $full.Substring(0, 1).ToLowerInvariant()
    $rest = $full.Substring(2).Replace("\", "/")
    return "/mnt/$drive$rest"
}

function Invoke-WindowsPythonReleaseCheck {
    param(
        [string]$Root,
        [string]$PythonCommand,
        [string[]]$PythonArgs
    )

    Set-Location $Root

    if (Test-Path ".venv-release-check") {
        Remove-Item -Recurse -Force ".venv-release-check"
    }

    & $PythonCommand @PythonArgs -m venv .venv-release-check
    . .\.venv-release-check\Scripts\Activate.ps1

    & $PythonCommand @PythonArgs -m pip install --upgrade pip
    & $PythonCommand @PythonArgs -m pip install -e .
    & $PythonCommand @PythonArgs -m unittest discover -s tests -v
    & $PythonCommand @PythonArgs examples/basic_usage.py
    & $PythonCommand @PythonArgs -m pip install build
    & $PythonCommand @PythonArgs -m build

    deactivate
    Remove-Item -Recurse -Force ".venv-release-check"
    Write-Host "RELEASE_CHECK_OK"
}

$root = Split-Path -Parent $PSScriptRoot

$pythonCommand = $null
$pythonArgs = @()

if (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCommand = "py"
    $pythonArgs = @("-3")
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCommand = "python"
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $pythonCommand = "python3"
}

if ($pythonCommand) {
    Invoke-WindowsPythonReleaseCheck -Root $root -PythonCommand $pythonCommand -PythonArgs $pythonArgs
    exit 0
}

if (-not (Get-Command wsl -ErrorAction SilentlyContinue)) {
    throw "No Windows Python command and no WSL were found. Install Python or enable WSL."
}

$wslRoot = Get-WslPath -WindowsPath $root
wsl bash -lc "cd '$wslRoot' && bash ./scripts/release_check.sh"
if ($LASTEXITCODE -ne 0) {
    throw "WSL release check failed."
}

Write-Host "RELEASE_CHECK_OK"
