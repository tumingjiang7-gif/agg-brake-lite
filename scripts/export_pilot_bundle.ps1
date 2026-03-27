$ErrorActionPreference = "Stop"

function Get-WslPath {
    param([string]$WindowsPath)

    $full = [System.IO.Path]::GetFullPath($WindowsPath)
    $drive = $full.Substring(0, 1).ToLowerInvariant()
    $rest = $full.Substring(2).Replace("\", "/")
    return "/mnt/$drive$rest"
}

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

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
    & $pythonCommand @pythonArgs .\scripts\export_pilot_bundle.py
    exit $LASTEXITCODE
}

if (-not (Get-Command wsl -ErrorAction SilentlyContinue)) {
    throw "No Windows Python command and no WSL were found. Install Python or enable WSL."
}

$wslRoot = Get-WslPath -WindowsPath $root
wsl bash -lc "cd '$wslRoot' && python3 ./scripts/export_pilot_bundle.py"
if ($LASTEXITCODE -ne 0) {
    throw "WSL bundle export failed."
}
