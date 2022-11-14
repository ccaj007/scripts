$dir = "G:\_xfer\new\Blue Bloods"

$folders = Get-ChildItem -Path $dir -Directory
foreach ($folder in $folders) {
    $new_folder = ($folder -split '\(')[0].Trim()
    rename-item -path $dir\$folder $new_folder
}
