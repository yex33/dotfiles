# Function for creating a backup file
# usage: backup file.txt
# result: copies file as file.txt.bak

function backup --argument filename
    cp $filename $filename.bak
end
