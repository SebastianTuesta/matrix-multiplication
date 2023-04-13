1. LINUX PRACTICE
    1.1. Count word ocurrence
        grep -o unix test1.txt | wc -l
    1.2. Count word ocurrence case insensitive
        grep -oi unix test1.txt | wc -l
    1.3. Command execution every minute 
        while sleep 1; do grep -o ERROR error.txt | wc -l; done

2. PYTHON PRACTICE
    2.1. run pylint
        cd matrix_integer
        pylint src
    2.2. run pytest
        cd matrix_integer
        python -m pytest