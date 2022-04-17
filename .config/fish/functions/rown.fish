# Function for printing a row
# usage: seq 3 | rown 3
# output: 3

function rown --argument index
    sed -n "$index p"
end
