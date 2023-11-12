# Prompt computer name
$computerName = Read-Host "Please enter the computer's name"

# Print computer name
Write-Host "You entered: $computerName"

# Confirm shutdown
$shutdownConfirm = Read-Host "Do you want to shutdown the computer? (Yes/No)"

# Validate shutdown
if ($shutdownConfirm -eq "Yes") {
    # Initiate shutdown
    Write-Host "Shutting down $computerName..."
    Stop-Computer -ComputerName $computerName -Force
} else {
    Write-Host "Shutdown cancelled."
}
