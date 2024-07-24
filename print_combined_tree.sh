#!/bin/bash

# Define the paths
paths=(
    "abc/bsasd/sdasd/asdasda"
    "abc/bsasd/sdasd/cfsas"
    "abc/xtg/bhj"
)

# Function to print paths as tree structure
print_tree() {
    local path=$1
    local indent=$2

    # Split path into components
    IFS='/' read -ra components <<< "$path"

    # Initialize variables
    local current_path=""
    local previous_path=""

    # Iterate through components to print tree structure
    for ((i=0; i<${#components[@]}; i++)); do
        current_path="$current_path/${components[i]}"
        # Check if this part of the path has been printed before
        if [[ "$current_path" == "$previous_path"* ]]; then
            # Print only new parts of the path
            printf "%*s- %s\n" $indent '' "${components[i]}"
        else
            # Print the entire path if it's new
            printf "%*s- %s\n" $indent '' "${components[i]}"
        fi
        indent=$((indent + 3))  # Increase indent for next level
        previous_path="$current_path"
    done
}

# Print header
echo "Combined Tree structure:"

# Loop through paths and print each as tree structure
for path in "${paths[@]}"; do
    print_tree "$path" 3  # Start indenting at 3 spaces
done
