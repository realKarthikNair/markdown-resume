@echo off
setlocal enabledelayedexpansion

:: Default values
set "INPUT="
set "OUTPUT="
set "SANITIZE=false"

:: Show help message
:show_help
echo Usage: build.bat -i ^<input_file^> -o ^<output_file^> [--sanitize true^|false]
echo.
echo Options:
echo   -i           Input markdown file (e.g., resume.md)
echo   -o           Output PDF file (e.g., resume.pdf)
echo   --sanitize   Whether to sanitize input before generating PDF (default: false)
echo   --help       Show this help message
echo.
echo Example usage:
echo build.bat -i resume.md -o resume.pdf --sanitize true
exit /b 1

:: Parse arguments
:parse_args
if "%~1"=="" goto end_parse
if "%~1"=="-i" (
    set "INPUT=%~2"
    shift
) else if "%~1"=="-o" (
    set "OUTPUT=%~2"
    shift
) else if "%~1"=="--sanitize" (
    set "SANITIZE=%~2"
    shift
) else if "%~1"=="--help" (
    call :show_help
    exit /b 0
) else (
    echo Unknown option: %~1
    call :show_help
    exit /b 1
)
shift
goto parse_args
:end_parse

:: Check required arguments
if "%INPUT%"=="" (
    echo Error: Input file not specified.
    call :show_help
    exit /b 1
)
if "%OUTPUT%"=="" (
    echo Error: Output file not specified.
    call :show_help
    exit /b 1
)

:: Sanitize if needed
if /i "%SANITIZE%"=="true" (
    set "SANITIZED=%INPUT:.md=_sanitized.md%"
    echo [*] Sanitizing %INPUT%...
    python sanitize.py -i "%INPUT%" -o "%SANITIZED%"
    set "INPUT=%SANITIZED%"
)

:: Generate PDF
echo [*] Generating PDF...
python generate.py -i "%INPUT%" -o "%OUTPUT%"

:: Clean up
if /i "%SANITIZE%"=="true" (
    echo [*] Cleaning up sanitized file...
    del "%INPUT%"
)

echo [+] Done. PDF saved to %OUTPUT%
