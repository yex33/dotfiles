# Function for taking the first 'n' lines
# usage: seq 10 | take 5
# results: prints only the first 5 lines
function take --argument number
    head -$number
end
