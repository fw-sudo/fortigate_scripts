N = ('\n') # newline
Q = ('"')  # double quote
row = 0    # row

### Create a empty output txt file
with open('fortigate_csv_to_ippools_output.txt', 'w') as f:
	f.write('')

### Append first line to output
with open('fortigate_csv_to_ippools_output.txt', 'a') as f:
    f.write('config firewall ippool' + N)

### Read input CSV and assign each column to a variable
with open('fortigate_csv_to_ippools_input.csv', 'r') as f:
    for line in f:
        values = line.split(';')        
        
        # Add comment to each column
        # Must be in format col0, col1, col2, etc.
        
        col0 = values[0].replace(N, '') # ippool
        col1 = values[1].replace(N, '') # startip
        col2 = values[2].replace(N, '') # endip
        col3 = values[3].replace(N, '') # comment

        
        # First line is not added to the output
        if row >= 1:    
            with open('fortigate_csv_to_ippools_output.txt', 'a') as f:
                f.write('edit ' + Q + col0 + Q + N)
                f.write('set type overload' + N)
                f.write('set startip ' + Q + col1 + Q + N)
                f.write('set endip ' + Q + col2 + Q + N)
                f.write('set comment ' + Q + col3 + Q + N)
                f.write('next' + N)     
        row = row + 1       

### Append and 'end' to the output
with open('fortigate_csv_to_ippools_output.txt', 'a') as f:
    f.write('end' + N)